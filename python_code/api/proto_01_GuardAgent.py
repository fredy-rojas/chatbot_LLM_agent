from agents import (GuardAgent,
                    ClassificationAgent,
                    DetailsAgent,
                    RecommendationAgent,
                    OrderTakingAgent,
                    AgentProtocol)
import os
from typing import Dict


def main():

    #==================================================================================
    # Instiantiation of GuardAgent class
    guard_agent = GuardAgent()

    
    messages = []
    while True:

        print(f"\n\nPrint Conversation messages: ..................... ")
        for message in messages:
            # if messages is empty, loop not happen, range=0
            print(f"{message['role']}:-- {message['content']}")
        
        # _____________________________________________________________
        # Get user input >>>>>>>>>>>>>>>>>>>>> START OF CONVERSATION
        prompt = input("User: ")
        print(f"..................... \n")


        messages.append({"role": "user", "content": prompt})
        # print(f"\nMessage with user query: {messages}\n")

        # _____________________________________________________________
        # Get GuardAgent's response
        guard_agent_response = guard_agent.get_response(messages)
        # print(f"\n\n{ guard_agent_response}\n\n")
        print(f"\nGuard respond: {guard_agent_response['memory']['guard_decision']}\n")
        if guard_agent_response["memory"]["guard_decision"] == "not allowed":
            messages.append(guard_agent_response)
            continue

        print(f"\n\n{ guard_agent_response}")
    

if __name__ == "__main__": 
    main()