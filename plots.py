import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
chart=pd.DataFrame(np.random.randn(20,3),columns=['Line-1','Line-2','Line-3'])          #linechart
st.subheader("1.1 Line chart")
st.line_chart(chart)


st.subheader("1.2 Area chart")
st.area_chart(chart)                                                                      #areachart

st.subheader("1.3 Bar chart")
st.bar_chart(chart)


st.header("2) Data Visualization with Matplotlib & Seaborn")
st.subheader("2.1 Loading the dataframe")
a=pd.read_csv("C:\\Users\\vigna\\AppData\\Roaming\\JetBrains\\PyCharmCE2024.1\\scratches\\iris.csv")
st.dataframe(a)



st.subheader("Data Visualization with Matplotlib & Seaborn")
st.subheader("2.1 Distribution Plot with matplotlib")
fig=plt.figure(figsize=(15,8))
a["species"].value_counts().plot(kind='bar')
st.pyplot(fig)


st.subheader("2.1 Distribution Plot with matplotlib")
fig=plt.figure(figsize=(15,8))
sns.distplot(a["sepal_length"])
st.pyplot(fig)


st.header("3.1 Multiple Graphs")
col1,col2=st.columns(2)
with col1:
    col1.header("KDE =False")
    col1.write("KDE = False")
    fig1=plt.figure()
    sns.distplot(a["sepal_length"],kde=False)
    st.pyplot(fig1)


with col2:
    col2.header("KDE =False")
    col2.write("KDE = False")
    fig2=plt.figure()
    sns.distplot(a["sepal_length"],hist=False)
    st.pyplot(fig2)

st.header('4. Changing Style')
col1, col2 = st.columns(2)
with col1:
    fig = plt.figure()
    sns.set_style('darkgrid')
    sns.set_context('notebook')
    sns.distplot(a['petal_length'], hist = False)
    st.pyplot(fig)
with col2:
    fig = plt.figure()
    sns.set_theme(context = 'poster', style = 'darkgrid')
    sns.distplot(a['petal_length'], hist = False)
    st.pyplot(fig)

st.header('5. Exploring Different Graphs')
st.subheader('5.1 Scatter Plot')
fig,ax = plt.subplots(figsize = (15,8))
ax.scatter(*np.random.random(size = (2,100)))
st.pyplot(fig)

st.subheader('5.2 Count-Plot')
fig = plt.figure(figsize = (15,8))
sns.countplot(data = a, x = 'species')
st.pyplot(fig)

st.subheader('5.3 Box-Plot')
fig = plt.figure(figsize = (15,8))
sns.boxplot(data = a, x = 'species', y = 'petal_length')
st.pyplot(fig)

st.subheader('5.4 Violin-Plot')
fig = plt.figure(figsize = (15,8))
sns.violinplot(data = a, x = 'species', y = 'petal_length')
st.pyplot(fig)






