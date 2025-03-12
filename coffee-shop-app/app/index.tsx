import { Text, View, StatusBar } from "react-native";
import { SafeAreaView } from "react-native";
// import { SafeAreaView } from "react-native-safe-area-context";
import { ImageBackground } from "react-native";
import { TouchableOpacity } from "react-native"; // it can be used without GestureHandlerRootView when I use TouchableOpacity from "react-native"
// import { GestureHandlerRootView, TouchableOpacity} from "react-native-gesture-handler";
import { GestureHandlerRootView } from "react-native-gesture-handler";
import {router} from "expo-router";

import "../global.css"

// export default function Index() {
//   return (
//     <View
//       style={{
//         flex: 1,
//         justifyContent: "center",
//         alignItems: "center",
//       }}
//     >
//       <Text>Edit app/index.tsx to edit this screen.</Text>
//     </View>
//   );
// }

// export default function App() {
export default function Index() {
  return (
    //<View>
    <GestureHandlerRootView>
      {/* <StatusBar translucent backgroundColor="transparent" barStyle="light-content" /> */}
      {/* <SafeAreaView className="w-full h-full bg-transparent" edges={["top"]}> */}
      <SafeAreaView>
      
        <ImageBackground 
            className="w-full h-full items-center"
            source={require('../assets/images/index_bg_image.png')}
          >
          <View className="flex h-[60%]" />
            <View className="flex w-[80%]">
              <Text className="text-white text-4xl text-center font-[Sora-SemiBold]">
                Fall in love with Panamanian Coffee
              </Text>

              <Text className="pt-3 text-[#A2A2A2] text-center font-[Sora-Regular]">
                Welcome to our cozy corner, where every cup is design for you..
              </Text>

              <TouchableOpacity 
                className="bg-[#C67C4E] mt-10 p-3 rounded-lg items-center" 
                onPress = {() => router.push("./(tabs)/home")}
              >
                <Text className="text-xl text-white font-[Sora-SemiBold]">Get Started</Text> 
              </TouchableOpacity> 

            </View>
        </ImageBackground>

      </SafeAreaView>
    
    </GestureHandlerRootView>
    //</View>
  );
}