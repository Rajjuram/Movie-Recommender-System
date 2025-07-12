# Movie Recommender System

A content-based movie recommendation engine built using Python, Streamlit, and the OMDb API. Given a movie title, it suggests five similar movies based on precomputed similarity scores and displays their posters using OMDb.

## Dataset
click here:- https://www.kaggle.com/datasets/aayushmishra1512/apple-complete-stock-data19802020

---

## Features

- Recommends 5 similar movies for any selected title.
- Uses cosine similarity on movie vectors.
- Displays movie posters using the OMDb API.
- Fast and lightweight UI using Streamlit.
- Works offline using precomputed model files.

---

## Project Structure

movie-recommender-system/
│
├── app.py # Streamlit frontend app
├── .env # Stores your OMDb API key securely
├── model/
│ ├── movie_list.pkl # Movie metadata (titles & IDs)
│ └── similarity.pkl # Precomputed cosine similarity matrix
├── requirements.txt # Python package dependencies
└── README.md # Project documentation (this file)

yaml
Copy
Edit

---

## How to Run the App

### 1. Clone the Repository

```bash
git clone https://github.com/Rajjuram/Movie-Recommender-System
2. Create a Virtual Environment (Recommended)
bash
Copy
Edit
python -m venv env
env\Scripts\activate     # On Windows
# OR
source env/bin/activate  # On macOS/Linux
3. Install Required Packages
bash
Copy
Edit
pip install -r requirements.txt
4. Get Your OMDb API Key
Go to http://www.omdbapi.com/apikey.aspx

Register for a free API key.

Create a .env file in the root directory:

env
Copy
Edit
OMDB_API_KEY=your_actual_api_key_here
5. Run the Streamlit App
bash
Copy
Edit
streamlit run app.py
Sample Output

How It Works
User selects a movie from the dropdown list.

The app looks up similar movies using a cosine similarity matrix.

The titles and poster images of the top 5 matches are displayed.

Requirements
Python 3.7+

Libraries: streamlit, pickle, requests, dotenv, urllib

Technologies Used
Python

Streamlit – Web app framework

OMDb API – Movie data and posters

scikit-learn – (Used offline to compute similarity matrix)

Pickle – For saving model objects

Troubleshooting
Poster not showing?
Make sure your .env file is correctly set up with a working OMDb API key.

Check if you're exceeding the free usage limits of OMDb (1,000 requests/day).

Future Improvements
Add genre-based or hybrid recommendations

Integrate user ratings and filtering

Add search and filter functionality

---

# References
OMDb API Documentation

Streamlit Documentation

scikit-learn Cosine Similarity

TMDb (The Movie Database) – for original movie datasets

Python urllib Documentation

Dotenv – Python Environment Variables

---
