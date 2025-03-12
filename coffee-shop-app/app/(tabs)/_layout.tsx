import { StyleSheet, Text, View } from 'react-native'
import React from 'react'
import { Tabs } from "expo-router";
import Entypo from '@expo/vector-icons/Entypo';
import { FontAwesome6 } from '@expo/vector-icons';
import PageHeader from '@/components/PageHeader'; 
// //------------------


// export default function TabsLayout() {
//   return (
//     <Tabs>
//       <Tabs.Screen name="home" options={{ title: "Home" }} />
//       <Tabs.Screen name="settings" options={{ title: "Settings" }} />
//     </Tabs>
//   );
// }
//==========================================

const TabsLayout = () => {
    return (
        <>
            <Tabs
                screenOptions={{
                    tabBarActiveTintColor: '#C67C4E',
                    }}
            >
            <Tabs.Screen
                    name="home" 
                    options={{  
                        headerShown: false,
                        
                        // tabBarStyle: { display: 'none' },
                        title: "Home",
                        tabBarIcon: ({color}) => (
                            <Entypo name="home" size={24} color={color} />
                        ),
                    }}

                />
                <Tabs.Screen
                    name="order"
                    options={{ 
                        headerShown: true,
                        tabBarStyle: { display: 'none' },
                        title: "Cart",
                        tabBarIcon: ({color}) => (
                            <Entypo name="shopping-cart" size={24} color={color} />
                        )
                    }}
                />
                <Tabs.Screen
                    name="chatroom" 
                    options={{ 
                        headerShown: true, 
                        tabBarStyle: { display: 'none' },
                        title: "AI Barista",
                        tabBarIcon: ({color }) => (
                            <FontAwesome6 name="robot" size={24} color={color} />
                        ),
                    }}
                />

            </Tabs>
        </>



    );
  };
  
export default TabsLayout;
const style = StyleSheet.create({})