import numpy as np
import pickle
import streamlit as st

# #loading the saved model
loaded_model = pickle.load(open(r"C:\Users\USER\Desktop\Gomycode\financial_model_v2.pkl", "rb"))

def Financial_prediction(input_data):
    input_data = (4, 26,  1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0)

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array so the model will understand i am making prediction foe one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

    # making prediction on the loaded model
    prediction = loaded_model.predict(input_data_reshaped)

    if prediction[0] == 0:
        return("has bank account")
    else:
        return("no bank account")
    
def main():
    # giving the app a title
    st.title("Financial_Prediction Web App")

    # getting the input data from user

    household_size = st.text_input("household_size")                                           
    age_of_respondent = st.text_input("age_of_respondent")                                     
    cellphone_access_Yes = st.text_input("cellphone_access_Yes")                                
    gender_of_respondent_Male = st.text_input("gender_of_respondent_Male")                             
    marital_status_Dont  = st.text_input("marital_status_Dont know")                          
    marital_status_Married = st.text_input("marital_status_Married/Living together")             
    marital_status_Single = st.text_input("marital_status_Single/Never Married")                
    marital_status_Widowed = st.text_input("marital_status_Widowed")                             
    education_level_Other = st.text_input("education_level_Other/Dont know/RTA")               
    education_level_Primary = st.text_input("education_level_Primary education")                  
    education_level_Secondary = st.text_input("education_level_Secondary education")                
    education_level_Tertiary = st.text_input("education_level_Tertiary education")                 
    education_level_Vocational = ("education_level_Vocational/Specialised training")


     # code for prediction
    performance = ""

    # creating a button for prediction

    if st.button("bank_account_Yes"):
        performance = Financial_prediction(
            {household_size, age_of_respondent, cellphone_access_Yes,
            gender_of_respondent_Male, marital_status_Dont,
            marital_status_Married,
            marital_status_Single, marital_status_Widowed,
            education_level_Other,
            education_level_Primary,
            education_level_Secondary,
            education_level_Tertiary,
            education_level_Vocational})
        st.success(performance)
        

if __name__ == "__main__":
    main()               

        


    

