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
    # Instiantiation of Agent class
    guard_agent = GuardAgent()
    Classification_Agent = ClassificationAgent()
    recommendation_agent = RecommendationAgent('recommendation_objects/apriori_recommendations.json',
                                               'recommendation_objects/popularity_recommendation.csv'
                                               )

    #==================================================================================
    agent_dict: Dict[str, AgentProtocol] = {
        "details_agent": DetailsAgent(),
        "order_taking_agent": OrderTakingAgent(recommendation_agent),
        "recommendation_agent": recommendation_agent,
    }


    
    messages = []
    while True:

        print(f"\n\n.....................\nPrint Conversation messages:\n------------------------ ")
        for message in messages:
            # if messages is empty, loop not happen, range=0
            print(f"{message['role']}:-- {message['content']}")
        
        # _____________________________________________________________
        # Get user input >>>>>>>>>>>>>>>>>>>>> START OF CONVERSATION
        prompt = input("\nUser: ")
        print(f"____________________________________________________\n")


        messages.append({"role": "user", "content": prompt})
        # print(f"\nMessage with user query: {messages}\n")

        # _____________________________________________________________
        # Get GuardAgent's response
        guard_agent_response = guard_agent.get_response(messages)
        print(f"\n\n{ guard_agent_response}\n\n")
        print(f"\nGuard respond: {guard_agent_response['memory']['guard_decision']}\n")
        if guard_agent_response["memory"]["guard_decision"] == "not allowed":
            messages.append(guard_agent_response)
            continue

        # _____________________________________________________________
        # Get ClassificationAgent's response
        classification_agent_response = Classification_Agent.get_response(messages)
        chosen_agent = classification_agent_response["memory"]["classification_decision"]
        print("Classification agent choosing: ", chosen_agent,"\n")

        # _____________________________________________________________
        # Get the chosen agent's response
        agent = agent_dict[chosen_agent]
        response = agent.get_response(messages)
        print(f"Agent response:\n{response}\n")


        # _____________________________________________________________
        messages.append(response)

if __name__ == "__main__": 
    main()