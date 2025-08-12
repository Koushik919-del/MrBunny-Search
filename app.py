import streamlit as st
import requests
import urllib.parse

st.set_page_config(page_title="My Search Engine", page_icon="🔍")

params = st.experimental_get_query_params()
query_from_url = params.get("q", [""])[0]

st.title("🔍 My Search Engine")
query = st.text_input("Type your search here:", query_from_url)

if query:
    url = f"https://api.duckduckgo.com/?q={urllib.parse.quote(query)}&format=json&no_html=1&skip_disambig=1"
    data = requests.get(url).json()
    results = data.get("RelatedTopics", [])
    
    if results:
        for r in results:
            if "Text" in r and "FirstURL" in r:
                st.write(f"[{r['Text']}]({r['FirstURL']})")
    else:
        st.write("No results found.")
