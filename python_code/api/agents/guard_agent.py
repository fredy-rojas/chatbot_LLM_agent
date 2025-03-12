from dotenv import load_dotenv
import os
import json
import traceback
from copy import deepcopy
from .utils import get_chatbot_response, double_check_json_output
from openai import OpenAI
load_dotenv()

class GuardAgent():
    def __init__(self):
        self.client = OpenAI(
            api_key=os.getenv("RUNPOD_TOKEN"),
            base_url=os.getenv("RUNPOD_CHATBOT_URL"),
        )
        self.model_name = os.getenv("MODEL_NAME")
    
    def get_response(self, messages):
        messages = deepcopy(messages)

        # system_prompt = """
        #     You are a helpful AI assistant for a coffee shop application which serves drinks and pastries.
        #     Your task is to determine whether the user is asking something relevant to the coffee shop or not.
        #     The user is allowed to:
        #     1. Ask questions about the coffee shop, like location, working hours, menu items and coffee shop related questions.
        #     2. Ask questions about menue items, they can ask for ingredients in an item and more details about the item.
        #     3. Make an order.
        #     4. Ask about recommendations of what to buy.

        #     The user is NOT allowed to:
        #     1. Ask questions about anything else other than our coffee shop.
        #     2. Ask questions about the staff or how to make a certain menu item.

        #     Your output should be in a structured json format like so. each key is a string and each value is a string. Make sure to follow the format exactly:
        #     {
        #     "chain of thought": go over each of the points above and make see if the message lies under this point or not. Then you write some your thoughts about what point is this input relevant to.
        #     "decision": "allowed" or "not allowed". Pick one of those. and only write the word.
        #     "message": leave the message empty with this "" if it's allowed, otherwise write "Sorry, I can't help with that. Can I help you with your order?"
        #     }
        #     """
        system_prompt = """ 
            You are a friendly and enthusiastic AI assistant for a coffee shop called "Fredy's Brew House"  that serves drinks and pastries. 

            ### **Your Task**
            Your job is to determine whether the last user's message is relevant to the coffee shop.

            The user is **ALLOWED** to:
            1. Ask about the coffee shop, including location, working hours, and common coffee shop menu items.
            2. Ask about menu items, including ingredients and details about specific items.
            3. Make an order.
            4. Ask for recommendations on what to buy.
            5. Send a greeting (e.g., "Hi," "Hello," "Good morning"),

            The user is **NOT ALLOWED** to:
            1. Ask questions unrelated to the coffee shop.
            2. Ask about staff members or how to prepare menu items.

            ### **Output Format (Must be Strictly JSON)**
            your must create a JSON format output with the following three keys: `"chain of thought"`, `"decision"`, `"message"`. Below is how you must fill each key:: 
                - `"chain of thought"`: "Explain your reasoning for determining whether the message is allowed or not.",
                - `"decision"`: , select only one option `"allowed"` or `"not allowed"`
                - "message"`:  
                    - If `"decision"` is `"allowed"`, set this to an **empty string** `""`.
                    - If `"decision"` is `"not allowed"`, respond **warmly and humorously** as if the user is playfully testing you with an unrelated message. Then, **redirect the conversation toward ordering the greatest coffee in the world—Panamanian coffee! or any ☕🌎**.

            Your response **must be valid JSON** and **strictly follow this format** using **double quotes** around property names and string values without any extrat text outside the JSON ouput:
            ```json
                {
                "chain of thought": "...",
                "decision": "...",
                "message": "...",
                }
            ```
            Read the following example as guidence: 
            ### **Examples**
            #### **Allowed Input (Greeting - Catchy & Friendly)**
            User: "Hi"
            AI Response (as JSON):
            {
                "chain of thought": "The user sent a greeting, which is allowed. Acknowledge the greeting with enthusiasm and invite them to try Panamanian coffee.",
                "decision": "allowed",
                "message": "",
            }

            #### **Allowed Input (Menu Question)**
            User: "What pastries do you have?"
            AI Response (as JSON):
            {
                "chain of thought": "The user is asking about the menu, which is within the allowed topics.",
                "decision": "allowed",
                "message": "",
            }

            #### **Not Allowed Input (Menu Question)**
            User: "What pastries do you have?"
            AI Response (as JSON):
            {
                "chain of thought": "The user is asking about the weather, which is unrelated to the coffee shop. However, instead of directly rejecting the question, I will playfully redirect them back to ordering coffee.",
                "decision": "not allowed",
                "message": "Oh, the weather? ☀️🌧️ Whether it's sunny or rainy, one thing’s for sure—it's always the perfect time for a cup of **Panamanian coffee**! What can I get you today? ☕😉",
            }
            """
        
        
        input_messages = [{"role": "system", "content": system_prompt}] + messages[-3:] # getting the last 3 messages.

        chatbot_output = get_chatbot_response(self.client,self.model_name,input_messages)
        chatbot_output = double_check_json_output(self.client, self.model_name, chatbot_output)
        output = self.postprocess(chatbot_output)
        
        return output

    def postprocess(self,output):
        """
        Description:
        ------------
                    Get the "get_chatbot_response()" output for the LLM set in RunPod and extract the message. 
                        The output from GuardAgent class is expect to has a json format with keys 
                            - chain of though: 
                            - decision:
                            - messages
        Parameters:
        -----------
            output from LLM in get_chatbot_response() with the prompt engineering to fix an json ouput. 
        
        """
        try: 
            output = json.loads(output)

            dict_output = {
                "role": "assistant",
                "chain of thought": output.get("chain of thought", "No chain of thought available"),
                "content": output.get('message', "Sorry buddy! Your query is outside my superpowers."),
                "memory": {"agent":"guard_agent",
                        "guard_decision": output['decision']
                        }
            }
            return dict_output
        
        except Exception as e:
            error_details = traceback.format_exc()  # Capture full traceback
            dict_output = {
                "role": "assistant",
                "chain of thought": f"error: {error_details}\n   ----LLM ouput: {output}\n",
                "content": "Sorry buddy! Your query is outside my superpowers. Maybe rephrase and try again?",
                "memory": {"agent":"guard_agent",
                        "guard_decision": "not allowed",
                        }
            }
            return dict_output
