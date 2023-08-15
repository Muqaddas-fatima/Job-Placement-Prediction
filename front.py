import streamlit as st
import joblib

# Initialize empty dictionary to store input values
data = {}

# Score inputs
data["ssc_p"] = st.slider("Enter SSC Percentage", 0.0, 100.0, step=0.1)
data["hsc_p"] = st.slider("Enter HSC Percentage", 0.0, 100.0, step=0.1)
# HSC Stream input
hsc_s = st.radio("Select HSC Stream",("Commerce", "Science", "Arts"))
data["hsc_s"] = 0 if hsc_s == "Commerce" else 1 if hsc_s == "Science" else 2
data["degree_p"] = st.slider("Enter Degree Percentage", 0.0, 100.0, step=0.1)
# Work Experience input
workex = st.radio("Do you have work experience?",("No", "Yes"))
data["workex"] = 0 if workex == "No" else 1
data["etest_p"] = st.slider("Enter Employability Test Percentage", 0.0, 100.0, step=0.1)
# Specialisation input
specialisation = st.radio("Select Specialisation",("Mkt&HR", "Mkt&Fin"))
data["specialisation"] = 0 if specialisation == "Mkt&HR" else 1
data["mba_p"] = st.slider("Enter MBA Percentage", 0.0, 100.0, step=0.1)

# load the model from disk
loaded_model = joblib.load(open('ran.pkl', 'rb'))
if st.button("Predict"):
 prediction = loaded_model.predict([list(data.values())])

if prediction == 1:
    st.success("GOT THE JOB")
else:
    st.error("DID NOT GET THE JOB")
