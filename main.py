import streamlit as st
from scrape import scrape_site, split_dom_content, clean_content, extract_content


st.title("AI Web-Scraper")
url = st.text_input("Enter a site URL you want scraped")

if st.button("Scrape Site"):
    st.write("Scraping Website Now :D")

    result = scrape_site(url)
    body_content = extract_content(result)
    clean_content = clean_content(body_content)

    st.session_state.dom_content = clean_content

    with st.expander("View DOM Content"):
        st.text_area("Dom Content", clean_content, height=300)


if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe what you want parsed")

    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing the content")

            dom_chunks = split_dom_content(st.session_state.dom_content)
            