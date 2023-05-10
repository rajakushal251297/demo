import requests
import pandas as pd
import streamlit as st
import pyttsx3

    
    
    
cities=pd.read_csv("in.csv")
city_name=cities["City"]
city_name_list=list(city_name)

   
page_bg_img ='''
<style>
.stApp {
background-image: url("https://c4.wallpaperflare.com/wallpaper/175/524/956/digital-digital-art-artwork-fantasy-art-drawing-hd-wallpaper-preview.jpg");
background-size: cover;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)


st.title("𝓕𝓲𝓷𝓭 𝓦𝓮𝓪𝓽𝓱𝓮𝓻 𝓓𝓮𝓽𝓪𝓲𝓵𝓼 𝓕𝓻𝓸𝓶 𝓒𝓲𝓽𝔂 𝓝𝓪𝓶𝓮")
option=st.selectbox("˜”*°• Search City Name •°*”˜",city_name_list)

apikey="f58c5b8ed2de30d34d40aeea453d15fc"
try:
    data=requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={option}&appid={apikey}").json()
    temp=int(data["main"]["temp"])-273
    Cityname = data["name"]
    Temprature = str(temp)+" °C"
    Currentcondition = data["weather"][0]['description']
    Windspeed = data["wind"]["speed"]
    Humidity = data["main"]["humidity"]
    
except Exception as e:
    Cityname = "Not found"
    Temprature = "Not found"
    Currentcondition = "Not found"
    Windspeed = "Not found"
    Humidity = "Not found"
    

    
if st.button("𝐒𝐞𝐚𝐫𝐜𝐡"):
    st.markdown(f"""𝓒𝓲𝓽𝔂 𝓷𝓪𝓶𝓮 : :blue[{Cityname}]\n""")
    st.markdown(f"""𝓣𝓮𝓶𝓹𝓻𝓪𝓽𝓾𝓻𝓮 : :green[{Temprature}]\n """)
    st.markdown(f"""𝓒𝓾𝓻𝓻𝓮𝓷𝓽 𝓬𝓸𝓷𝓭𝓲𝓽𝓲𝓸𝓷 : :orange[{Currentcondition}]\n """)
    st.markdown(f"""𝓦𝓲𝓷𝓭 𝓼𝓹𝓮𝓮𝓭 : :red[{Windspeed}]\n """)
    st.markdown(f"""𝓗𝓾𝓶𝓲𝓭𝓲𝓽𝔂 : :violet[{Humidity}] """)
    print(f"city : {Cityname}")
    print(f"temprature : {Temprature}")
    engine = pyttsx3.init()
    engine.setProperty('rate', 125)
    voices = engine.getProperty('voices') 
    engine.setProperty('voice', voices[1].id)
    engine.say(f"the temprature of {Cityname} is {Temprature}")
    engine.runAndWait()
    










