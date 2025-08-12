import streamlit as st
import requests
import urllib.parse

st.set_page_config(page_title="My Search Engine", page_icon="🔍")

# CSS to center content and style like Google
st.markdown("""
<style>
    .main {
        max-width: 700px;
        margin: auto;
        padding-top: 150px;
        text-align: center;
        font-family: Arial, sans-serif;
    }
    .search-box > div {
        display: flex;
        justify-content: center;
    }
    input[type="text"] {
        width: 100%;
        max-width: 600px;
        padding: 15px 20px;
        font-size: 18px;
        border-radius: 24px;
        border: 1px solid #ddd;
        box-shadow: 0 2px 5px rgb(0 0 0 / 0.1);
        outline: none;
        transition: box-shadow 0.3s ease;
    }
    input[type="text"]:focus {
        box-shadow: 0 0 8px #4285f4;
        border-color: #4285f4;
    }
    .result {
        text-align: left;
        margin: 20px 0;
        padding: 15px;
        border-bottom: 1px solid #eee;
    }
    .result a {
        color: #1a0dab;
        font-size: 18px;
        text-decoration: none;
    }
    .result a:hover {
        text-decoration: underline;
    }
    .result-url {
        color: #006621;
        font-size: 14px;
        margin-top: 4px;
    }
</style>
""", unsafe_allow_html=True)

query_from_url = st.query_params.get("q", [""])[0]

with st.container():
    st.markdown('<div class="main">', unsafe_allow_html=True)
    st.markdown('<h1 style="font-weight:normal;">My Search Engine</h1>', unsafe_allow_html=True)
    
    query = st.text_input("", value=query_from_url, key="search_input", placeholder="Search the web")
    
    if query:
        url = f"https://api.duckduckgo.com/?q={urllib.parse.quote(query)}&format=json&no_html=1&skip_disambig=1"
        data = requests.get(url).json()
        results = data.get("RelatedTopics", [])
        
        if results:
            for r in results:
                if "Text" in r and "FirstURL" in r:
                    st.markdown(f'''
                        <div class="result">
                            <a href="{r["FirstURL"]}" target="_blank" rel="noopener noreferrer">{r["Text"]}</a><br>
                            <span class="result-url">{r["FirstURL"]}</span>
                        </div>''', unsafe_allow_html=True)
        else:
            st.markdown("<p>No results found.</p>", unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
