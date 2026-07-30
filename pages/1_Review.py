import streamlit as st
import csv
import os
from datetime import datetime

st.set_page_config(page_title="App Review", page_icon="📝")

st.title("📝 App Review & Suggestions")
st.write("Help me improve this application! Let me know what features you want to see or if you found any bugs or if you want to contribute to the data, refer to Credentials.")

with st.form("review_form", clear_on_submit=True):
    user_name = st.text_input("Name (Optional)")
    feedback_text = st.text_area("Your Feedback / Suggestions", height=150)
    
    submitted = st.form_submit_button("Submit Review")
    
    if submitted:
        if not feedback_text.strip():
            st.error("Please enter some feedback before submitting.")
        else:
            # Save to a new CSV file
            file_exists = os.path.isfile("app_reviews.csv")
            with open("app_reviews.csv", "a", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                if not file_exists:
                    writer.writerow(["Timestamp", "Name", "Feedback"])
                
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                name = user_name if user_name else "Anonymous"
                writer.writerow([timestamp, name, feedback_text])
                
            st.success("Thank you for your feedback! It has been recorded.")