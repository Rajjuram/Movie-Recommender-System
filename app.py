import pickle
import streamlit as st
import requests
import heapq
import os
import urllib.parse
from dotenv import load_dotenv

# Load OMDb key
load_dotenv()
omdb_api_key = os.getenv("OMDB_API_KEY")

# OMDb Poster Fetcher
def fetch_poster(title):
    encoded = urllib.parse.quote(title)
    url = f"http://www.omdbapi.com/?t={encoded}&apikey={omdb_api_key}"
    try:
        response = requests.get(url, timeout=5)
        data = response.json()
        if data.get("Poster") and data["Poster"] != "N/A":
            return data["Poster"]
    except Exception as e:
        print(f"OMDb fetch failed for '{title}':", e)
    return "https://via.placeholder.com/300x450?text=No+Poster"

# Recommendation logic
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = heapq.nlargest(6, enumerate(similarity[index]), key=lambda x: x[1])
    recommended_names = []
    recommended_posters = []

    for i in distances[1:6]:
        title = movies.iloc[i[0]].title
        recommended_names.append(title)
        recommended_posters.append(fetch_poster(title))
    
    return recommended_names, recommended_posters

# Streamlit UI
st.set_page_config(page_title="Movie Recommender", layout="wide")
st.title("Movie Recommender System")
st.markdown("##### Select a movie to get recommendations")

# Load model files
movies = pickle.load(open('model/movie_list.pkl', 'rb'))
similarity = pickle.load(open('model/similarity.pkl', 'rb'))

# Movie select
selected_movie = st.selectbox("Choose a movie:", movies['title'].values)

# Recommend button
if st.button("Show Recommendation"):
    with st.spinner("Finding best matches..."):
        names, posters = recommend(selected_movie)
    cols = st.columns(5)
    for idx, col in enumerate(cols):
        with col:
            st.text(names[idx])
            st.image(posters[idx])
