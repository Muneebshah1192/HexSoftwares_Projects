# 🎧 Resonance | Premium AI Music Engine

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)
![scikit-learn](https://img.shields.io/badge/scikit--learn-Machine%20Learning-orange.svg)
![License](https://img.shields.io/badge/License-MIT-purple.svg)

**Resonance** is a high-performance **AI-powered music recommendation system** that analyzes acoustic signatures and metadata of thousands of songs to recommend tracks with similar sonic profiles.

Instead of simple genre matching, the system uses **machine learning and vector similarity** to find mathematically similar songs.

---

# ✨ Key Features

### 🎼 Acoustic Feature Analysis
Resonance analyzes real audio features including:

- Danceability
- Energy
- Musical Key
- Genre metadata

It combines **numerical audio features** with **TF-IDF vectorized text metadata** for intelligent recommendations.

---

### ⚡ Deep-Pool Matrix Compression
Traditional similarity matrices can become extremely large.

Example:
```
15000 x 15000 similarity matrix ≈ 1.5GB
```

To optimize performance, the system compresses this matrix into a **deep-pool dictionary (~500MB)** enabling:

- Faster recommendations
- Lower RAM usage
- High performance even on lightweight servers

---

### 🔀 Dynamic Recommendation Engine

Instead of always returning the same songs:

1. The system finds the **Top 30 closest matches**
2. It **randomly shuffles them**
3. Displays **6 unique recommendations**

This creates a **Spotify-like discovery experience**.

---

### 🔎 Ultra Fast Search

The UI uses **Tom Select JavaScript library** to create a searchable dropdown for **10,000+ songs** without browser lag.

---

### 🎧 Instant Music Playback

Each recommendation includes an **embedded Spotify player**, allowing users to instantly preview songs.

---

### 🎨 Premium UI Design

The interface includes:

- Animated gradient background
- CSS music equalizer logo
- Floating recommendation cards
- Smooth animation effects

---

# 🏗️ System Architecture

The project consists of **two pipelines**.

---

## 1️⃣ Model Training (Google Colab)

Steps performed:

1. Load Spotify dataset
2. Clean and preprocess data
3. Apply **TF-IDF Vectorization**
4. Normalize audio features using **MinMaxScaler**
5. One-Hot Encode musical keys
6. Compute **Cosine Similarity**
7. Compress similarity matrix

Generated files:

```
music_dict.pkl
similarity_deep.pkl
```

---

## 2️⃣ Web Application (Flask)

The Flask backend:

- Loads precomputed model files
- Processes search queries
- Sends recommendations to frontend
- Renders the UI

---

# 📦 Large File Downloads

Due to **GitHub's file size limitations**, the following large files are **hosted on Google Drive instead of the repository**.

These files are required to run the project.

### 📥 Download Links

**Music Dictionary File**

```
music_dict.pkl
```

Download:
https://drive.google.com/file/d/1SYdiKNaUBgaOCYm4UnyghC2-_gkAB-Zx/view?usp=sharing

---

**Similarity Matrix File**

```
similarity_deep.pkl
```

Download:
https://drive.google.com/file/d/1GWak6tPIYp_PUsO_Vn1hG62ZvYeOq1h_/view?usp=sharing

---

**Spotify Dataset**

```
spotify_data.csv
```

Download:
https://drive.google.com/file/d/1Q0DJWzmCDFAdJkcAOtFLUXT08_dmwOid/view?usp=sharing

---

### ⚠️ Important Note

To reduce file size and speed up downloads:

All files are **uploaded as ZIP archives**.

After downloading:

1. Extract the ZIP files
2. Place the extracted files in the **project root directory**

Final directory should look like:

```
resonance-music-ai/

app.py
music_dict.pkl
similarity_deep.pkl
spotify_data.csv
```

---

# 🚀 Installation & Local Setup

## Prerequisites

Install:

- Python 3.8+
- Git

---

## Step 1 — Clone Repository

```bash
git clone https://github.com/yourusername/resonance-music-ai.git

cd resonance-music-ai
```

---

## Step 2 — Install Dependencies

```bash
pip install flask pandas scikit-learn
```

or

```bash
pip install -r requirements.txt
```

---

## Step 3 — Download Model Files

Download the files from the **Google Drive links above**.

Extract them and place them in the project directory.

---

## Step 4 — Run the Application

```bash
python app.py
```

Open your browser:

```
http://127.0.0.1:5000
```

---

# 🗂️ Project Structure

```
resonance-music-ai/

app.py
Model_Training.ipynb
requirements.txt

templates/
    index.html

static/
    css
    js
    images

.gitignore
README.md
```

---

# 🔮 Future Improvements

### 🎵 Spotify API Integration
Use **Spotify API (Spotipy)** to fetch real-time audio features.

---

### 🎛️ Music Filter Controls
Add sliders for:

- Energy
- Danceability
- Tempo
- Mood

---

### 👤 User Accounts
Allow users to:

- Log in
- Save playlists
- Build personal libraries

---

### 📱 Mobile Optimization
Convert the platform into a **Progressive Web App (PWA)**.

---

# 👨‍💻 Author

**Syed Muneeb Haider Shah**

- Freelance Web Developer  
- AI Automation Engineer  
- Music Producer & Beat Maker

If you like this project, consider giving the repository a ⭐.

---

# 📜 License

MIT License  
Free to use, modify, and distribute.
