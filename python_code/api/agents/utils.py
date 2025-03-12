def get_chatbot_response(client,model_name,messages,
                         temperature=0, top_p=0.8,max_tokens=2000):
    """
    Description:
    -----------
        Wrapper for client.chat.completion.create().
        
    Parameters:
    -----------
        client: Object create by OpenAI Python API
        model_name: model name used in RunPod
        messages: list of dictionaries, each dictionary contain key role and content.
        temperature: level of randoness for the model.

    """

    input_messages = []
    for message in messages:
        input_messages.append({"role": message["role"], "content": message["content"]})

    response = client.chat.completions.create(
        model=model_name,
        messages=input_messages,
        temperature=temperature,
        top_p=top_p,
        max_tokens=max_tokens,
    ).choices[0].message.content
    
    return response


def get_embedding(embedding_client,embedding_model,text_input):
    """
    Parameteres:
    ------------
        embedding_client: instance object after creating a client with OpenAI Python API/ 
        embedding_model: name of the model use for embedding, it need to match with the Severless endpoint in runpod
        text_input: text that will be transform into an embedding vector. 

    Return:
    -------
        embedings: a list of lists: [[embedding_vector1], [embedding_vector2]]
    """
    output = embedding_client.embeddings.create(input=text_input,
                                                model=embedding_model)
    
    embedings = []
    for embedding_object in output.data:
        embedings.append(embedding_object.embedding)

    return embedings


def double_check_json_output(client,model_name,json_string):
    prompt = f""" You will first remember how a correct JSON formant is and then you will check this json string and correct any mistakes that will make it invalid. Then you will return the corrected json string. Nothing else. 
    If the Json is correct just return it.

    If there is any text before order after the json string, remove it. 
    Do NOT return a single letter outside of the json string.
    Make sure that each key is enclosed in double quotes.
    The first thing you write should be a curly brace of the json and the last character your write should be the closing curly brace. 

    You should check the json string for the following text between triple backticks: 
    ```
    {json_string} 
    ```
    """

    messages = [{"role": "user", "content": prompt}]
    response = get_chatbot_response(client,model_name,messages)
    response = response.replace("`", "") # just in cases where the LLM return backticks. 

    return response