import streamlit as st
import pandas as pd

st.header("Synergy's Movies Recommendation System")


movies = pd.DataFrame({
    'title': ['The Shawshank Redemption', 'The Godfather', 'The Dark Knight', 
              'Pulp Fiction', 'Forrest Gump', 'Inception', 'The Matrix'],
    'movie_id': [278, 238, 155, 680, 13, 27205, 603]  # TMDB IDs
})

movie_list = movies['title'].values
selected_movie = st.selectbox('Type or select a movie to get recommendation', movie_list)

if st.button('Show recommendation'):
    st.success(f"Similar to '{selected_movie}': Try 'The Godfather Part II' or 'Goodfellas'")
    
    # Display sample posters 
    st.write("Sample posters would display here with your full code")