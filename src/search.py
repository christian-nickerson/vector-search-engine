from decimal import Decimal

import streamlit as st

from client.api import APIClient

BUILD_STATE_KEY = "built-db"

if BUILD_STATE_KEY not in st.session_state:
    st.session_state[BUILD_STATE_KEY] = False


def sub_title(title: str) -> None:
    """display product subtitle

    :param title: text to display
    """
    st.markdown(f"### {title}")


def price(currency: str, price: Decimal) -> None:
    """display product price

    :param currency: Currency to display
    :param price: price to display
    """
    symbol = "\\$" if currency == "USD" else ""
    st.markdown(f"Price ({currency}): **{symbol}{price}**")


def availability(availability: str) -> None:
    """display product availability

    :param availability: availability status
    """
    if availability == "InStock":
        text = f":green[{availability}]"
    else:
        text = f":red[{availability}]"
    st.markdown(f"Availability: **{text}**")


def sizes(sizes: str | None) -> None:
    """display available sizes

    :param sizes: string of sizes available (| separated)
    """
    if sizes:
        list_of_sizes = sizes.split(" | ")
        st.selectbox("Available sizes:", list_of_sizes)


def colour(colours: str | None) -> None:
    """display available colours

    :param colours: string of colours available (/ separated)
    """
    if colours:
        list_of_colours = colours.split("/")
        st.selectbox("Available colours:", list_of_colours)


def images(image_url: str) -> None:
    """display product image

    :param image_url: string of image urls (| separated)
    """
    if image_url != "":
        list_of_images = image_url.split(" | ")
        st.image(list_of_images[0])


def display_product(result: dict) -> None:
    """Display a product

    :param result: GraphQL data to display
    """
    with st.container():
        st.header(result["name"])
        col1, col2 = st.columns(2)
        with col1:
            sub_title(result["subTitle"])
            price(result["currency"], result["price"])
            availability(result["availability"])
            sizes(result["availableSizes"])
            colour(result["color"])
        with col2:
            images(result["images"])
        st.write(result["description"])
        st.divider()


client = APIClient()
st.title("Nike Product Search")

if not st.session_state[BUILD_STATE_KEY]:
    with st.spinner("Building the database..."):
        client.build_db()
        st.session_state[BUILD_STATE_KEY] = True

search_text = st.text_input("Search for a product", placeholder="A soccer jacket")
st.divider()

if search_text:
    results = client.search_query(search_text)
    for result in results["data"]["search"]:
        display_product(result)
