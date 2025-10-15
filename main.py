import streamlit as st

st.title("AI Web-Scraper")
url = st.text_input("Enter a site URL you want scraped")

if st.button("Scrape Site"):
    st.write("Scraping Website Now :D")