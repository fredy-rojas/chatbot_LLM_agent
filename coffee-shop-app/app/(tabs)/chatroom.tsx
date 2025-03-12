import { Alert, Text, TouchableOpacity, View } from 'react-native';
import React, { useEffect, useRef, useState } from 'react';
import { GestureHandlerRootView, TextInput } from 'react-native-gesture-handler';
import PageHeader from '@/components/PageHeader';
import {MessageInterface} from '@/types/types';
import { widthPercentageToDP as wp, heightPercentageToDP as hp } from 'react-native-responsive-screen'
import { Feather } from '@expo/vector-icons';
import {  useCart } from '@/components/CartContext'
import MessageList  from '@/components/MessageList'
import {callChatBotAPI } from '@/services/chatBot'

const chatroom = () => {
  const {addToCart, emptyCart} = useCart();
  const [messages, setMessages] = useState<MessageInterface[]>([]);
  const [isTyping, setIsTyping] = useState<boolean>(false);
  const inputRef = useRef<TextInput>(null)
  const textRef = useRef('')

  const handleSendMessage = async () => {
    let message = textRef.current.trim();
    if (!message) return;
    try {
        // Add the user message to the list of messages
        let InputMessages = [...messages, { content:message, role: 'user' }];
        setMessages(InputMessages);
        textRef.current = ''
        if(inputRef) inputRef?.current?.clear();
        // CALL CHATBOT API
        setIsTyping(true)
        // await new Promise(resolve => setTimeout(resolve, 5000))
        let resposnseMessage = await callChatBotAPI(InputMessages)
        // setMessages([...InputMessages, {content: 'I am bot', role: 'assistant'}])
        setIsTyping(false)
        setMessages([...InputMessages, resposnseMessage])
        
        
        if (resposnseMessage) {
            if (resposnseMessage.memory ) {
                if (resposnseMessage.memory.order) {
                    emptyCart()
                    resposnseMessage.memory.order.forEach((item: any) => {
                    addToCart(item.item, item.quantity)
                    });
                }
            }
        }
        
    } catch(err:any ) {
        Alert.alert('Message', err.message)
    }
  }
  return (
    <GestureHandlerRootView>
      <PageHeader title="AI Barista" showHeaderRight={false} bgColor='#F9F9F9'/>
      

      <View className='flex-1 justify-between bg-neutral-100 overflow-visible'>
        <View className='flex-1'>
          <MessageList
            messages= {messages}
            isTyping={isTyping}
          />
        </View>
        <View className='flex-row mx-3 justify-between border p-2 bg-white border-neutral-300 rounded-full pl-5'>
          <TextInput
            ref={inputRef}
            onChangeText={value=> textRef.current = value}
            placeholder='type a message...'
            style={{fontSize: hp(2)}}
            className='flex-1 mr-2'
          />
          <TouchableOpacity
            onPress = {handleSendMessage}
            className='bg-neutral-200 rounded-full p-2 mr-[1px'>
            <Feather  name='send' size={hp(3)} color='#737373'/>
          </TouchableOpacity>
        </View>
      </View>
    </GestureHandlerRootView>
  )
}
export default chatroom