import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle

#Load all the instances that are required 
 with open('model.pkl','rb') as file:
     model=pickle.load(file)
 with open('scaler.pkl','rb') as file:
     model=pickle.load(file)
 with open('pca.pkl','rb') as file:
     model=pickle.load(file)
     
     
def prediction(input_data):
    scaled_data=scaler.transform(input_data)
    pca_data=pca.transform(scaled_data)
    pred=model.predict(pca_data)[0]
     if pred==0:
         return 'Developed'
     elif pred==1:
         return 'Developing'
     else:
         return 'Under Developed'
def main()
   st.title("HELP International Foundation')
    st.sunheader('''This application helps to classify the country on basis of its scio-economic and health factors''')
    chld_mor=st.text_input('Enter child Mortality rate')
    lf_exp = st.text_input("Enter Average Life Expectancy")
    tot_fer = st.text_input("Enter Average Total Fertility")
    export = st.text_input("Enter the % of GDP Spent on Export")
    imports = st.text_input("Enter the % of GDP Spent on Imports")
    health = st.text_input("Enter the % of GDP Spent on Health")
    gdp = st.text_input("Enter the GDP per Capita")
    income = st.text_input("Enter the Net Income per Person")
    inflation = st.text_input("Enter the Inflation Rate")
    input_data = [[chld_mor,export,health,imports,income,inflation,lf_exp,tot_fer,gdp]]
    if st.button('predict'):
        response=prediction(inp_list)
        st.success(response)
if __name__=='__main__':
  main() 
