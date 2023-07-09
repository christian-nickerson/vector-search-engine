import streamlit as st

from client.api import APIClient

BUILD_STATE_KEY = "built-db"
client = APIClient()

# def show_product(name: str, sub_title: str, in_stock: str):


if BUILD_STATE_KEY not in st.session_state:
    st.session_state[BUILD_STATE_KEY] = False

st.title("Nike Product Search")

if not st.session_state[BUILD_STATE_KEY]:
    with st.spinner("Building the database..."):
        client.build_db()
        st.session_state[BUILD_STATE_KEY] = True

search_text = st.text_input("Search for a product", placeholder="A soccer jacket")

if search_text:
    with st.spinner("Searching the database..."):
        results = client.search_query(search_text)
    for result in results["data"]["search"]:
        with st.container():
            st.write(result)
            st.divider()
