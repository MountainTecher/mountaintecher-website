import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="AI Troubleshooter | MountainTecher", page_icon="📱")
st.title("📱 Smart Tech-Troubleshooter")
st.markdown("Instantly fix your smartphone battery, network, and software issues.")

phone_model = st.text_input("Enter Smartphone Model:")
issue = st.text_area("Describe the problem:")

if st.button("Generate Fix"):
    if not phone_model or not issue:
        st.warning("Please enter both details.")
    else:
        try:
            api_key = st.secrets["GEMINI_API_KEY"]
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel("gemini-3.6-flash")
            
            prompt = f"As an Elite Troubleshooter for 'MountainTecher', provide a fix for {phone_model} facing: {issue}. Give Root Cause, Quick Fix, and Advanced Settings Fix."
            
            with st.spinner("Analyzing issue..."):
                response = model.generate_content(prompt)
                
            st.success("Solution Ready!")
            st.markdown(response.text)
        except Exception as e:
            st.error(f"Error: {e}")
