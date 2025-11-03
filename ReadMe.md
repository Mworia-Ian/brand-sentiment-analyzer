# 🏆 AI Brand Sentiment Analyzer

_An AI-powered toolkit that compares how people feel about different brands or organizations._

---

### 🔍 Overview

The **AI Brand Sentiment Analyzer** is an interactive web app that compares how people feel about different brands or organizations. It simulates realistic online comments, performs **sentiment** and **emotion** analysis using Hugging Face Transformers, and visualizes the results with Streamlit and Plotly.

You can view and interact with the live app here:
👉 https://brand-sentiment-analyzer-gndc7pamezhbnbszciygwv.streamlit.app/

Watch a short demo of the project on YouTube:
🎥 https://youtu.be/I40rKeM5Fx0

This project demonstrates how Generative AI can help beginners learn, experiment, and build meaningful solutions using **open-source**, **zero-cost tools**. It was developed as part of my Moringa School AI Capstone Project.

---

### ⚙️ Key Features

- 🧠 Dual-layer analysis — sentiment (positive/negative/neutral) + emotion (joy, sadness, surprise, etc.)
- 🎨 Interactive visualizations with **Plotly** (pie and bar charts)
- 💬 Dynamic, realistic opinion generation (simulated data, no API cost)
- 🚀 Instant brand-to-brand comparison
- 🌙 Dark-theme-friendly design
- 💾 Fully offline — no API keys or paid models required

---

### 🧰 Tech Stack

| Tool                            | Purpose            |
| ------------------------------- | ------------------ |
| **Python 3.10+**                | Core language      |
| **Streamlit**                   | UI and dashboard   |
| **Transformers (Hugging Face)** | NLP pipelines      |
| **Torch**                       | Model runtime      |
| **Plotly**                      | Interactive charts |
| **Pandas**                      | Data handling      |

---

### 🧪 How It Works

1. User enters two brand names.
2. The app generates realistic opinion samples about each brand.
3. Each opinion is analyzed by two AI models:
   - Sentiment model → classifies overall tone
   - Emotion model → identifies underlying feeling
4. Results are displayed as:
   - Sentiment comparison table and bar chart
   - Per-brand pie and emotion charts
   - Colored sentiment tables (green = positive, red = negative, grey = neutral)

---

### 🚀 Getting Started

#### 1️⃣ Clone the repository

```bash
git clone https://github.com/IanMworia/brand-sentiment-analyzer.git
cd brand-sentiment-analyzer
```

#### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

#### 3️⃣ Run the app

```bash
streamlit run app.py
```

Then open your browser at 👉 [http://localhost:8501](http://localhost:8501)

---

### 🧾 Example Output

| text                                                       | sentiment   | emotion     |
| ---------------------------------------------------------- | ----------- | ----------- |
| _Moringa School exceeded my expectations in transparency._ | 🟢 POSITIVE | 😮 Surprise |
| _I think Moringa School could improve on quality._         | 🔴 NEGATIVE | 😐 Neutral  |
| _Overall, my experience with Moringa School was average._  | ⚪ NEUTRAL  | 😐 Neutral  |

📊 Results are visualized through interactive charts for easy brand-to-brand comparison.

---

### 📂 Project Structure

```
brand-sentiment-analyzer/
├── app.py                # Streamlit app
├── requirements.txt      # Dependencies
├── README.md             # Project overview (this file)
└── toolkit.md / .pdf     # Full Moringa submission with reflections & evaluation
```

---

### 🌟 Future Improvements

- 🕸️ Real data scraping from Twitter/Reddit (with user consent)
- 💾 “Download as PDF” sentiment report
- 📅 Sentiment-over-time graph
- 💬 Multilingual model support
- ☁️ Optional cloud deployment (Hugging Face Spaces / Streamlit Cloud)

---

### ✍️ Author

**Ian Mworia**  
💼 Software Developer | AI Enthusiast  
📍 Nairobi, Kenya  
🔗 [LinkedIn](https://www.linkedin.com/in/ian-mworia/) · [GitHub](https://github.com/Mworia-Ian)

---

### 📜 License

This project is open source and available under the [MIT License](LICENSE) — free to use, learn from, and improve.

---

### 🧠 Acknowledgments

- **Moringa School** — for mentorship and structure
- **Hugging Face** — for free, high-quality open models
- **Streamlit** — for making Python apps easy to build and share
