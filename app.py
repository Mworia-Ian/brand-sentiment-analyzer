import streamlit as st
from transformers import pipeline
import pandas as pd
import random
import plotly.express as px

# PAGE CONFIG 
st.set_page_config(
    page_title="AI Brand Sentiment Analyzer",
    page_icon="🏆",
    layout="wide"
)
st.title("🏆 AI Brand Sentiment Analyzer")
st.write(
    "Compare how people feel about two brands or organizations based on simulated online opinions. "
    "Each run generates new, realistic feedback and analyzes both **sentiment** and **emotion**."
)

#  LOAD MODELS 
@st.cache_resource
def load_models():
    sentiment = pipeline(
        "sentiment-analysis",model="distilbert/distilbert-base-uncased-finetuned-sst-2-english") # type: ignore
    emotion = pipeline(
        "text-classification",
        model="j-hartmann/emotion-english-distilroberta-base",
        top_k=1
    )
    return sentiment, emotion

sentiment_model, emotion_model = load_models()

#  GENERATE SAMPLE OPINIONS 
def simulate_opinions_clean(brand, n=8):
    pos_templates = [
       f"I recently tried {brand} and found it amazing. Would recommend it to others.",
       f"{brand} exceeded my expectations in terms of quality."
    ]
    neg_templates = [
       f"I recently tried {brand} and found it disappointing. I probably wouldn't use it again.",
       f"Overall, my experience with {brand} was terrible; needs serious improvement."
    ]
    neutral_templates = [
       f"Overall, my experience with {brand} was average.",
       f"People say {brand} has become increasingly common."
    ]
    samples = []
    for _ in range(n):
        tset = random.choices(["pos","neg","neutral"], weights=[0.4,0.3,0.3])[0]
        if tset == "pos":
            samples.append(random.choice(pos_templates))
        elif tset == "neg":
            samples.append(random.choice(neg_templates))
        else:
            samples.append(random.choice(neutral_templates))
    return samples


# ANALYSIS
def analyze_brand(brand):
    texts = simulate_opinions_clean(brand)
    sentiments = [sentiment_model(t)[0] for t in texts]
    emotions = []

    for t in texts:
        result = emotion_model(t)
        if result and isinstance(result, list) and isinstance(result[0], list):
            emotions.append(result[0][0]) # type: ignore
        else:
            emotions.append({"label": "Unknown", "score": 0})

    df = pd.DataFrame({
        "text": texts,
        "sentiment": [s["label"] for s in sentiments],
        # "sentiment_conf": [round(s["score"] * 100, 2) for s in sentiments],
        "emotion": [e["label"].capitalize() for e in emotions],
        # "emotion_conf": [round(e["score"] * 100, 2) for e in emotions],
    })
    return df

#COLOR HELPER 
def color_text(label):
    """Returns an HTML-colored version of the sentiment label."""
    if label == "POSITIVE":
        return f'<span style="color:#00C853; font-weight:bold;">{label}</span>'
    elif label == "NEGATIVE":
        return f'<span style="color:#D50000; font-weight:bold;">{label}</span>'
    else:
        return f'<span style="color:#9E9E9E; font-weight:bold;">{label}</span>'

# FORM 
with st.form("brand_form"):
    col1, col2 = st.columns(2)
    with col1:
        brand1 = st.text_input("Enter first brand name:")
    with col2:
        brand2 = st.text_input("Enter second brand name:")
    submitted = st.form_submit_button("Compare Brands 🚀")

# MAIN LOGIC
if submitted and brand1 and brand2:
    with st.spinner("Analyzing sentiments..."):
        df1 = analyze_brand(brand1)
        df2 = analyze_brand(brand2)

        # Summary Comparison
        st.subheader("📊 Sentiment Comparison")
        summary1 = df1["sentiment"].value_counts()
        summary2 = df2["sentiment"].value_counts()

        comparison = pd.DataFrame({
            "Sentiment": ["POSITIVE", "NEGATIVE", "NEUTRAL"],
            brand1: [summary1.get("POSITIVE", 0), summary1.get("NEGATIVE", 0), summary1.get("NEUTRAL", 0)],
            brand2: [summary2.get("POSITIVE", 0), summary2.get("NEGATIVE", 0), summary2.get("NEUTRAL", 0)]
        })
        st.dataframe(comparison, use_container_width=True)
        st.bar_chart(comparison.set_index("Sentiment"))

        #DETAILED VISUALS PER BRAND
        for brand, df in [(brand1, df1), (brand2, df2)]:
            st.subheader(f"🧾 Detailed Analysis — {brand}")

            # Sentiment Pie Chart
            fig_sent = px.pie(
                df,
                names="sentiment",
                title=f"{brand} Sentiment Distribution",
                color="sentiment",
                color_discrete_map={
                    "POSITIVE": "limegreen",
                    "NEGATIVE": "red",
                    "NEUTRAL": "gray"
                }
            )
            st.plotly_chart(fig_sent, use_container_width=True)

            # Emotion Bar Chart
            emo_counts = df["emotion"].value_counts().reset_index()
            emo_counts.columns = ["emotion", "count"]
            fig_emo = px.bar(
                emo_counts,
                x="emotion",
                y="count",
                title=f"{brand} Emotion Breakdown",
                color="emotion"
            )
            st.plotly_chart(fig_emo, use_container_width=True)

            # Color sentiment labels in table
            df_html = df.copy()
            df_html["sentiment"] = df_html["sentiment"].apply(color_text)
            st.markdown(df_html.to_html(escape=False, index=False), unsafe_allow_html=True)

st.markdown("---")
st.caption("✨ Powered by Hugging Face Transformers & Streamlit | Built by Ian Mworia")
