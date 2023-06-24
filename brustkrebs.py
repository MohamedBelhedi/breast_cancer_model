import streamlit as st
import pandas as pd
import numpy as np
import os
import datetime as dt
import time

# path=[]
# for dirname,_,filenames in os.walk('./Krebs/'):
#     for filename in filenames:
#         print(os.path.join(dirname,filename))
#         path.append(os.path.join(dirname,filename))

path="./Krebs/cancer.csv"
st.title("BrustKrebs Model")
now=dt.datetime.today()
today=now.strftime("%d.%m.%Y")
st.header(f"Heute ist der {today}")
def get_data(path):
    global df
    global data
    df=pd.read_csv(path)
    data=df.head()
    df=st.dataframe(data)
    return df,data


get_data(path)

def prepare_data():
    global X,y
    data.dropna(inplace=True)
    # st.dataframe(data.head())
    st.header("Isna Values")
    st.text(data.isna().sum())

    st.header("Preparing Data")

    data["outcome"]=data["diagnosis"]=="M"
   
    data.replace({False:0,True:1},inplace=True)
    st.dataframe(data)


    X=data[["radius_mean","texture_mean","perimeter_mean","area_mean","smoothness_mean"]]
    y=data["outcome"]
    return X,y
prepare_data()

st.header("Train Model & Imports")

def train_model():
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.model_selection import train_test_split
    from sklearn.metrics import mean_absolute_error
    from sklearn.pipeline import Pipeline
    from sklearn.preprocessing import MinMaxScaler
    global pred,X_train,y_train,text,text_input

    X_train,X_test,y_train,y_test=train_test_split(X,y,train_size=0.64,random_state=101,shuffle=True)

    model=KNeighborsClassifier(n_neighbors=1,n_jobs=5)
    model.fit(X_train,y_train)
    # "20.57,10.38,77.58,1203.0,0.08474"
    text_input=st.text_input("Gib die werte ein jeder einzelene Wert gefolgt vom ,")
    time.sleep(10)
    pred=model.predict([[str(text_input)]])
    print(pred)

    if pred==1:
        text="Aufgrund der angebenen Werte hättest du leider Krebs 😢"
    else:
        text="Keine Krebs"    
    pred=pd.DataFrame(pred,columns=["predction_oucomes"])
    return pred,text_input




train_model()
st.text(pred)
st.dataframe(X_train)
st.dataframe(pred)
st.header(f"die eigebenen Werte{text_input}")
st.title(text)
