import {Text, View } from 'react-native';
import React from 'react';
import AntDesign from '@expo/vector-icons/AntDesign';
import Entypo from '@expo/vector-icons/Entypo';
import { TouchableOpacity } from "react-native-gesture-handler";


// 
const SearchArea = () => {
  return (
    <View
        className='w-full items-center bg-[#222222] pb-6 bg-[#222222]' 
        // style={{ backgroundColor: "#222222" }}
        >
        
        <View className='flex w-[90%] pt-8'>

            <Text className='text-[#A2A2A2] text-sm font-[Sora-Regular]'>
                Location
            </Text>

            <Text className='text-white text font-[Sora-Regular]'>
                Parnell, Auckland.
            </Text>

        
            <View className='w-full mt-5 flex-row justify-between'>
                <View 
                className="flex  w-[80%] h-14 px-4 bg-[#A2A2A2] rounded-2xl focus:border-secondary justify-center"
                // style={{ backgroundColor: 'gray', marginBottom: 16}}
                >
                    <AntDesign name="search1" size={24} color="white" />
                </View>
                
                <TouchableOpacity>
                    <View className="flex w-14 h-14 bg-app_orange_color rounded-2xl items-center justify-center">
                        <Entypo name="sound-mix" size={24} color="white" />
                    </View>
                </TouchableOpacity>
            </View>

        </View>
        
    </View>
  )
}

export default SearchArea
