import streamlit as st
import pickle
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

# Page config
st.set_page_config(page_title="Movie Recommender", layout="wide")

# Custom CSS
st.markdown("""
    <style>
    body {
        background: linear-gradient(to right, #141e30, #243b55);
        color: white;
        
    }
    .title {
        font-size: 50px;
        font-weight: bold;
        text-align: center;
        color: #f5c518;
        margin-bottom: 30px;
    }
    .movie-card {
        background: linear-gradient(135deg, #ff512f, #dd2476);
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        color: white;
        box-shadow: 0px 0px 15px rgba(255,255,255,0.2);
        margin-bottom: 20px;
        transition: 0.3s;
    }
    .movie-card:hover {
        transform: scale(1.08);
        background: linear-gradient(135deg, #24c6dc, #514a9d);
        box-shadow: 0px 0px 25px rgba(255,255,255,0.3);
    }
    </style>
""", unsafe_allow_html=True)


# Load data
movies_df = pickle.load(open('df.pkl','rb'))
movies_list = movies_df['title'].values

indices = pickle.load(open('indices.pkl','rb'))
tfidf_matrix = pickle.load(open('tfidf_matrix.pkl','rb'))

# Recommendation function
def recommend(movie, n=10):
    if movie not in indices:
        return ['Movie not found']

    idx = indices[movie]
    sim_score = cosine_similarity(tfidf_matrix[idx], tfidf_matrix).flatten()
    similar_idx = sim_score.argsort()[::-1][1:n + 1]

    return movies_df['title'].iloc[similar_idx]

# Title
st.markdown('<div class="title">🎬 Movie Recommender System</div>', unsafe_allow_html=True)

# Center layout
col1, col2, col3 = st.columns([1,2,1])

with col2:
    selected_movie_name = st.selectbox("Select a movie", movies_list)
    recommend_btn = st.button("✨ Recommend")

if recommend_btn:
    recommendation = recommend(selected_movie_name)

    st.subheader("Recommended Movies 🍿")
    cols = st.columns(5)

    for i, name in enumerate(recommendation):
        with cols[i % 5]:
            st.markdown(f"""
            <div class="movie-card">
                <h4>{name}</h4>
            </div>
            """, unsafe_allow_html=True)



