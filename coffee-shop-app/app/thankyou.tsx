import { Text, View } from 'react-native'
import React from 'react'
import { TouchableOpacity,GestureHandlerRootView } from 'react-native-gesture-handler'
import {router} from "expo-router";

const ThankyouPage = () => {
  return (
    <GestureHandlerRootView>
        <View className='w-full h-full items-center justify-center '>
        <Text className='text-3xl font-[Sora-SemiBold] text-center mx-10'>Thank you For Your Order</Text>

        <TouchableOpacity 
                className='  items-center justify-center '
                // style={{ backgroundColor: "#C67C4E" }}
                
                onPress={() => router.push("/(tabs)/home")}
              >
                <Text className="2-full rounded-2xl mt-6 py-3 px-4 text-xl color-white font-[Sora-Regular] bg-app_orange_color">
                    Return to Home Page
                    </Text> 
          </TouchableOpacity> 
        </View>
    </GestureHandlerRootView>
  )
}

export default ThankyouPage