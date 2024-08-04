import streamlit as st
import pandas as pd

st.subheader("Uploading the CSV file")
df = st.file_uploader("Upload the CSV file : ", type=['csv', 'xlsx'])                                     #Uploading and Loading


st.subheader("Loading the CSV file")
df=pd.read_csv("C:/Users/vigna/Desktop/jupyter/Products.csv")                                             #Files
if df is not None:
       st.table(df.head())


st.subheader("Dealing With Images Directly")
st.image("C:\\Users\\vigna\\AppData\\Roaming\\JetBrains\\PyCharmCE2023.3\\scratches\\img.png")            #Images


st.subheader("Dealing With Images while uploading")
img=st.file_uploader("Upload the Image file : ",type=['png','jpeg'])
if img is not None:
    st.image(img)


st.subheader("Working with videos")
video1=st.file_uploader("Upload the vedio files : ",type=['mkv','mp4','mp3'])                              #Videos
if  video1 is not None:
    st.video(video1,start_time=5)



st.subheader("Working with Audio")
audio1=st.file_uploader("Upload the Audio files : ",type=['mkv','mp4','mp3'])                              #Videos
if  audio1 is not None:
    st.audio(audio1.read())
