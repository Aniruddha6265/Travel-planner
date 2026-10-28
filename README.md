# ✈️ Personalized Travel Itinerary Planner

An AI-powered travel planning app built with **Streamlit**. Tell it your vibe, budget, and interests, and it recommends destinations, builds an optimized day-by-day itinerary, lets you swap out activities you don't like, and exports everything as an offline PDF guide.

> Skill Wallet Capstone Project 4

🔗 **Live demo:** _add your Streamlit app link here_

---

## ✨ Features

- **🧭 Smart Destination Recommender** – Suggests the top 3 cities that match your preferences.
- **📅 Itinerary Generator** – Day-by-day plans (morning sightseeing, lunch, afternoon leisure, evening dining) with geographic clustering, itemized costs, and cumulative budget tracking.
- **🎨 Vibe Customizer** – Swap a single activity or regenerate an entire day without wiping the rest of your plan.
- **💼 Trip Manager & PDF Export** – Save, load, and delete trips, and download a clean offline PDF travel guide (includes emergency contacts).
- **🎭 Demo Mode** – Try the full app instantly with pre-built sample data. No API key needed.
- **🔌 Two LLM providers** – Choose between **Google Gemini** and **Groq**. Both offer free tiers.

---

## 🚀 Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the app

```bash
streamlit run app.py
```

The app opens at `http://localhost:8501`.

---

## 🔑 API Keys (optional)

The app works out of the box in **Demo Mode**. For live AI-generated results:

1. Get a free API key:
   - **Gemini:** [aistudio.google.com](https://aistudio.google.com)
   - **Groq:** [console.groq.com](https://console.groq.com)
2. Open the app sidebar, choose your provider, and paste the key into the **API Key** field.
3. Demo Mode switches off automatically once a key is entered.

Your key is entered at runtime and is **never stored in the code or repository**.

---

## 🗂️ Project Structure

```
├── app.py                # Main entry point
├── config.py             # Session state setup & API key sidebar
├── llm_client.py         # Unified Gemini / Groq / Demo client
├── demo_data.py          # Sample data for Demo Mode
├── pdf_export.py         # PDF generation (fpdf2)
├── trip_store.py         # Save / load trips
├── ui_styles.py          # Custom CSS
├── requirements.txt      # Python dependencies
├── .streamlit/
│   └── config.toml       # Theme settings
└── tabs/
    ├── tab_preferences.py   # Sidebar trip preference form
    ├── tab_recommender.py   # Tab 1: Destination recommender
    ├── tab_itinerary.py     # Tab 2: Itinerary generator
    ├── tab_customizer.py    # Tab 3: Vibe customizer & activity swap
    └── tab_manager.py       # Tab 4: Trip manager & PDF export
```

---

## ☁️ Deploy on Streamlit Community Cloud

1. Push this project to a public GitHub repository (with `app.py` and `requirements.txt` at the repo root).
2. Go to [share.streamlit.io](https://share.streamlit.io) and click **New app**.
3. Select your repository and branch, and set the main file to `app.py`.
4. Click **Deploy**.

> **Note:** Saved trips are stored in session state with a local `saved_trips.json` backup. On Streamlit Cloud, this file resets when the app restarts, so saved trips are not permanent there. Download the PDF to keep your itinerary.

---

## 🛠️ Tech Stack

| Purpose | Tool |
|---|---|
| Web UI | [Streamlit](https://streamlit.io) |
| LLM providers | Google Gemini (`google-generativeai`), Groq (`groq`) |
| PDF export | [fpdf2](https://py-pdf.github.io/fpdf2/) |
| Language | Python 3 |

---

## 🧭 How to Use

1. Fill in your **trip preferences** in the sidebar (destination, vibe, duration, budget, travel party, pace, interests).
2. Open **Destination Recommender** to get city suggestions.
3. Open **Itinerary Generator** to create your day-by-day plan.
4. Use **Vibe Customizer** to swap activities or regenerate a day.
5. Open **Trip Manager & PDF** to save your trip and download the PDF.

---

## 📄 License

This project is for educational purposes. Add a license of your choice (e.g., MIT) if you plan to share or reuse it.
