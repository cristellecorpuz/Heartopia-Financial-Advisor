import streamlit as st

st.set_page_config(page_title="About & Credentials", page_icon="👩‍💻")

st.title("👩‍💻 About & Credentials")
st.write(
    "This is an AI-powered Retrieval-Augmented Generation (RAG) pipeline designed "
    "to calculate profit margins and retrieve item data for Heartopia."
)

st.divider()

st.subheader("Developer")
st.markdown("**Cassy**") 
st.markdown("🐙 [GitHub](https://github.com/your-username)")
st.markdown("💼 [LinkedIn](https://linkedin.com/in/your-profile)")
st.markdown("📧 [Gmail](mailto:your.email@gmail.com)")

st.divider()

st.subheader("Acknowledgments")
st.markdown(
    "Database kindly provided by: **[AthenaMM](https://docs.google.com/spreadsheets/d/1Q4CBSoHHnrpl44-ID-zawwmx2agqbezOahdjzRR642g/edit)**"
    "You can contribute to the database by clicking the link and following through instructions. Thank you!")
