import streamlit as st
import pandas as pd
import plotly.express as px
import os

st.set_page_config(page_title="Monitoring Dashboard", page_icon="📊", layout="wide")
st.title("📊 LLM Monitoring Dashboard")
st.caption("Real-time metrics for the Heartopia RAG pipeline.")

#LOAD DATA
@st.cache_data(ttl=30)
def load_feedback_data():
    if os.path.exists("feedback.csv"):
        df = pd.read_csv("feedback.csv")
        df['Timestamp'] = pd.to_datetime(df['Timestamp'])
        return df
    return pd.DataFrame()

df = load_feedback_data()

if df.empty:
    st.info("No feedback data available yet. Go to the main app and submit some ratings!")
else:
    #TOP METRICS
    total_queries = len(df)
    thumbs_up = len(df[df['Rating'] == 'Thumbs Up'])
    approval_rate = (thumbs_up / total_queries) * 100 if total_queries > 0 else 0
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Queries", total_queries)
    col2.metric("Positive Ratings", thumbs_up)
    col3.metric("Approval Rate", f"{approval_rate:.1f}%")
    
    st.divider()
    
    #CHARTS
    colA, colB, colC = st.columns(3)
    
    with colA:
        st.subheader("Rating Distribution")
        fig_pie = px.pie(df, names='Rating', color='Rating', 
                         color_discrete_map={'Thumbs Up':'#00cc96', 'Thumbs Down':'#ef553b'})
        st.plotly_chart(fig_pie, use_container_width=True)
        
    with colB:
        st.subheader("Queries Over Time")
        df['Date'] = df['Timestamp'].dt.date
        daily_counts = df.groupby('Date').size().reset_index(name='Count')
        fig_line = px.line(daily_counts, x='Date', y='Count', markers=True)
        st.plotly_chart(fig_line, use_container_width=True)

    with colC:
        st.subheader("Tokens Used Per Day")
        daily_tokens = df.groupby('Date')['Tokens'].sum().reset_index()
        fig_bar = px.bar(daily_tokens, x='Date', y='Tokens', color_discrete_sequence=['#636efa'])
        st.plotly_chart(fig_bar, use_container_width=True)

    st.divider()
    
    st.subheader("Recent Queries & Retrieved Context")
    display_df = df.sort_values(by="Timestamp", ascending=False).head(15)
    
    st.dataframe(
        display_df,
        use_container_width=True,
        column_config={
            "Context": st.column_config.TextColumn("Retrieved Context", width="large"),
            "Question": st.column_config.TextColumn("Question", width="medium"),
            "Answer": st.column_config.TextColumn("Answer", width="medium")
        }
    )