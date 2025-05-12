import streamlit as st
import pickle
import numpy as np

final_rating = pickle.load(open('popular.pkl','rb'))
pt = pickle.load(open('pt.pkl','rb'))
similarity_array = pickle.load(open('sa.pkl','rb'))

st.set_page_config('Book-Recommender',layout='centered',page_icon='📚')
st.title('📚Books Recommender System')
selected_book = st.selectbox('Select Book',final_rating['Book-Title'])

def fetch_poster(suggestion):
    book_name = []
    ids_index = []
    poster_url = []

    for book_id in suggestion:
        book_name.append(pt.index[book_id])

    for name in book_name:
        ids = np.where(final_rating['Book-Title'] == name)[0][0]
        ids_index.append(ids)

    for idx in ids_index:
        url = final_rating.iloc[idx]['Image-URL-M']
        poster_url.append(url)

    return poster_url
def recommend(book):
    sug_books = []
    index = np.where(pt.index==book)[0][0]
    distances = sorted(list(enumerate(similarity_array[index])),key=lambda x:x[1],reverse=True)[1:6]
    suggestion = [i[0] for i in distances]
    
    poster_url = fetch_poster(suggestion)
    
    for i in range(len(suggestion)):
            books = pt.index[suggestion[i]]
            sug_books.append(books)
    return sug_books , poster_url



if st.button("Recommend"):
    sug_books,pos_url1 = recommend(selected_book)
    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        st.text(sug_books[0])
        st.image(pos_url1[0])
    with col2:
        st.text(sug_books[1])
        st.image(pos_url1[1])

    with col3:
        st.text(sug_books[2])
        st.image(pos_url1[2])
    with col4:
        st.text(sug_books[3])
        st.image(pos_url1[3])
    with col5:
        st.text(sug_books[4])
        st.image(pos_url1[4])