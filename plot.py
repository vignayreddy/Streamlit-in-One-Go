import streamlit as st
import pandas as pd
import numpy as np
import streamlit as st
import altair as alt
import plotly.express as px
import plotly.figure_factory as ff

#Altair Scatter Plot

st.header("1. Altair Scatter Plot")
a=pd.DataFrame(np.random.randn(500,5),columns=['a','b','c','d','e'])
chart=alt.Chart(a).mark_circle().encode(x='a',y='b',size='c',tooltip=['a','b','c','d','e'])
st.altair_chart(chart)



st.header("2. Interactive Charts")
st.subheader("2.1 Line chart")
a=pd.read_csv("C:\\Users\\vigna\\AppData\\Roaming\\JetBrains\\PyCharmCE2024.1\\scratches\\lang_data.csv")
lang_list=a.columns.tolist()

lang_choices=st.multiselect("Choose your language",lang_list)
b=a[lang_choices]
st.line_chart(b)



st.subheader("2.2 Area Chart")
st.area_chart(b)


st.header("3. Data Visualization with plotly")
st.subheader("3.1 Displaying the dataset")
a=pd.read_csv("C:\\Users\\vigna\\AppData\\Roaming\\JetBrains\\PyCharmCE2024.1\\scratches\\tips.csv")
st.dataframe(a.head())


st.subheader("3.2 Pie Chart")
fig=px.pie(a,values="total_bill",names="time")
st.plotly_chart(fig)




st.subheader("3.3 Pie Chart with multiple parameters")
fig=px.pie(a,values="total_bill",names="day",opacity= .7,color_discrete_sequence=px.colors.sequential.RdBu)
st.plotly_chart(fig)


#Histogram2
x1=np.random.randn(200)
x2=np.random.randn(200)
x3=np.random.randn(200)

hist_data=[x1,x2,x3]
group_labels=["Group - 1","Group - 2","Group - 3"]
fig=ff.create_distplot(hist_data,group_labels,bin_size=[.1,.25,.5])
st.plotly_chart(fig)



