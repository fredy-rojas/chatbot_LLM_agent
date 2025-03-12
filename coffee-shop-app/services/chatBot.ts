import axios from 'axios';
import { MessageInterface } from '@/types/types';
import { API_KEY, API_URL } from '@/config/runpodConfigs';

async function callChatBotAPI(messages: MessageInterface[]): Promise<MessageInterface> {
    try {
        const response = await axios.post(API_URL, {
            input: { messages }
        }, {
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${API_KEY}`
            }
        });
        
        let output = response.data;
        let outputMessage: MessageInterface = output['output'];
        // console.log(outputMessage)

         // Log the full API response
        console.log("-----------Full API Response:", JSON.stringify(response.data, null, 2));

        return outputMessage;

// //=======================
//         // Step 1: Send the request
//         const response = await axios.post(API_URL, {
//             input: { messages }
//         }, {
//             headers: {
//                 'Content-Type': 'application/json',
//                 'Authorization': `Bearer ${API_KEY}`
//             }
//         });

//         console.log("Initial API Response:", JSON.stringify(response.data, null, 2));

//         // Extract the request ID
//         const requestId = response.data.id;
//         if (!requestId) {
//             throw new Error("RunPod did not return a valid request ID.");
//         }

//         // Step 2: Poll for results
//         let status = "IN_PROGRESS";
//         let result = null;
//         let retries = 0;
//         const maxRetries = 20; // Avoid infinite loops (adjust if needed)

//         while (status === "IN_PROGRESS" && retries < maxRetries) {
//             await new Promise(res => setTimeout(res, 5000)); // Wait 5 seconds before polling

//             const pollResponse = await axios.get(`${API_URL}/${requestId}`, {
//                 headers: {
//                     'Authorization': `Bearer ${API_KEY}`
//                 }
//             });

//             console.log("Polling API Response:", JSON.stringify(pollResponse.data, null, 2));

//             status = pollResponse.data.status;
//             if (status === "COMPLETED") {
//                 result = pollResponse.data.output;
//                 break;
//             }

//             retries++;
//         }

//         if (!result) {
//             throw new Error("RunPod response did not contain output.");
//         }

//         console.log("Final Output:", JSON.stringify(result, null, 2));
//         return result;

//====================================================================================
    } catch (error) {
        console.error('Error calling the API:', error);
        throw error;
    }
}

export { callChatBotAPI };