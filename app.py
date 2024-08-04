import streamlit as st
import pandas as pd

st.title("Title -> Geeks for Geeks")                                    #Title
st.header("Header-> Geeks for Geeks")                                   #Header
st.subheader("Subheader -> Geeks for Geeks")                            #Subheader
st.text("Text -> Geeks for Geeks")                                      #Text


st.markdown("# Hi")
st.markdown("## Hi")
st.markdown("### Hi")
st.markdown("#### Hi")                                                   #Markdown
st.markdown("##### Hi")




st.markdown('**GFG** is an Ed-Tech')                                     #Bold
st.markdown("__GFG__ is an Ed-Tech")                                     #Bold

st.markdown('***GFG*** is an Ed-Tech')                                     #Bold-Italic
st.markdown("___GFG___ is an Ed-Tech")                                     #Bold-Italic






st.success("Success")                                                    #Success
st.info("Information")                                                   #Info
st.warning("Warning")                                                    #Warning
st.error("Error")                                                        #Error

st.markdown("- First Point")
st.markdown("- Second Point")                                           #Bullets


exp=ZeroDivisionError("Division not possible with 0")                    #Exception
st.exception(exp)


st.help(ZeroDivisionError)                                               #Help
st.write("range(1,10)")                                                  #Write
st.write(range(1,10))
st.write("1+2+3")
st.write(1+2+3)



st.code("x=10\n"
       'for i in range(x):\n'                                             #Code
             'print(i)\n'
       )


st.checkbox("Male")                                                        #Checkbox-----No checkbox should be of same name
st.checkbox("Female")
if(st.checkbox("Adult")):
    st.write("You are an adult!")                                           #Checkbox with Validation



radioButton=st.radio("Select : ",('Male','Female',"Other"))
if(radioButton=='Male'):
    st.write("You're a Male")
elif(radioButton=='Female'):                                               #Radio Button
    st.write("You're a Female")
elif(radioButton=='Other'):
    st.write("You're an Other Gender")



st.subheader("Select Box")
selectBox=st.selectbox("Data Science: ",["Data Analysis",
                               "Web Scraping","Machine Learning","Deep Learning",
                               "Natural Language Processing","Computer Vision",                 #SelectBox
                               "Image Processing"])
st.write("You have selected : ",selectBox)


st.subheader("Multi Select Box")
multiselBox=st.multiselect("Data Science: ",["Data Analysis",
                               "Web Scraping","Machine Learning","Deep Learning",
                               "Natural Language Processing","Computer Vision",                 #SelectBox
                               "Image Processing"])                                                                                              #MultiSelectBox


st.write("You have selected : ",len(multiselBox),"Courses",multiselBox)                         #MultiSelection




st.subheader("Button")
if(st.button("Click Me")):                                                                      #Button
    st.write("Thanks for Clicking me")


st.subheader("Slider")
vol=st.slider("Select the volume: ",0,10,step=1)                                                #Slider
st.write("Volume is : ",vol)



st.subheader("Text Input")
name=st.text_input("Username : ")                                                               #Text_Input
password=st.text_input("Password : ",type="password")



st.subheader("Text Area")
textArea=st.text_area("Write Something Intresting about yourself")                             #Text-Area
st.write(textArea)



st.subheader("Input Number")
st.number_input("Select Your age",18,110)                                                             #Input-Number

st.subheader("Input Date")                                                                      #Input-Date
st.date_input("Date")

st.subheader("Input Time")                                                                      #Input-Time
st.time_input("Time")

