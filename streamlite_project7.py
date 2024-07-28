import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Data Analysis")

st.subheader("Data analysis using the streamlite and the python")


#upload the dataset
upload=st.file_uploader("Upload your dataset (in CSV format)")
if upload is not None:
  data=pd.read_csv(upload)
  

# show dataset
if upload is not None:
  if st.checkbox("preview Dataset"):
    if st.button("Head"):
      st.write(data.head())
    if st.button("tail"):
        st.write(data.tail())
        
#to check the datatype of each column
if upload is not None:
  if st.checkbox("Datatype of each column"):
    st.text("Datatypes")
    st.write(data.dtypes)
    
#Find the Shape of our dataset("NUmber of rows and the number of columns")
if upload is not None:
  if st.checkbox("Shape of the Dataset"):
    st.text("Dataset Shape")
    st.write("The dataset has the",data.shape[0]," rows","and",data.shape[1]," columns")
    
#To check the shape with the radio button
if upload is not None:
  data_shape= st.radio("What dimension do you want to check ?",("Rows","Columns"))
  if data_shape=="Rows":
    st.text("Number of Rows")
    st.write(data.shape[0])
  else:
    st.text("Number of columns:")
    st.write(data.shape[1])
  
  
#Find the null values un the dataset
  null_values_present = data.isnull().values.any()
  st.write(f"Null values present: {null_values_present}")
    
  if null_values_present:
        st.write('The dataset contains null values.')

        if st.checkbox("null values"):
            plt.figure(figsize=(10, 6))
            sns.heatmap(data.isnull(), cbar=False, cmap="viridis")
            st.pyplot(plt.gcf())
  else:
        st.success('The dataset does not contain any null values.')
        
#find the duplicate value in the data set and remove
  if st.checkbox("Duplicated value"):
    duplicated_value=data.duplicated().any()
    if duplicated_value==True:
      st.warning("This dataset contains the Duplicate value")
      dup=st.selectbox("Do you want to removr the duplicated value?",("Select one","yes","No"))
      if dup=="yes":
        data=data.drop_duplicates()
        st.success("Duplicated values are removed")
      if dup=="No":
        st.text("ok No problrm")  
    else:
      st.success("Congratulation!!!, No duplicate values")  

# Get the overall statistics
if upload is not None:
  if st.checkbox("Summary of the dataset"):
    st.write(data.describe(include="all"))
    
#About the section
if st.button("About App"):
  st.text("Built in streamlit")
  st.text("Thanks to streamlit")
  
#By
if st.checkbox("By"):
  st.success("Anish Subedi")
