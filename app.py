import streamlit as st

st.set_page_config(page_title="My Search Engine", layout="wide")

st.markdown("""
<style>
body, html, #root > div {
    height: 100%;
    margin: 0;
    font-family: Arial, sans-serif;
    background: white;
}

/* Top right navigation */
.top-nav {
    display: flex;
    justify-content: flex-end;
    padding: 15px 30px;
    font-size: 14px;
    color: #444;
    gap: 20px;
    align-items: center;
    position: fixed;
    width: 100%;
    top: 0;
    background: white;
    z-index: 10;
}

.top-nav a {
    color: #444;
    text-decoration: none;
    font-weight: 500;
}

.top-nav a:hover {
    text-decoration: underline;
}

/* Apps icon */
.apps-icon {
    width: 24px;
    height: 24px;
    cursor: pointer;
    display: grid;
    grid-template-columns: repeat(3, 6px);
    grid-template-rows: repeat(3, 6px);
    gap: 4px;
}

.apps-icon div {
    background-color: #666;
    border-radius: 2px;
}

/* Center content */
.center-content {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100vh;
    padding-top: 60px; /* for fixed top nav */
}

/* Title */
.title {
    font-size: 4rem;
    color: #222;
    margin-bottom: 30px;
    font-weight: 700;
}

/* Search input */
.search-input {
    width: 500px;
    max-width: 90vw;
    padding: 12px 20px;
    font-size: 18px;
    border: 1px solid #ccc;
    border-radius: 28px;
    box-shadow: 0 2px 6px rgb(0 0 0 / 0.1);
    outline: none;
    transition: box-shadow 0.3s ease;
    text-align: center;
}

.search-input:focus {
    box-shadow: 0 0 8px rgba(0, 120, 215, 0.8);
    border-color: #0078d7;
}
</style>
""", unsafe_allow_html=True)

top_nav_html = """
<div class="top-nav">
    <a href="#">About</a>
    <a href="#">Help</a>
    <div class="apps-icon" title="Apps">
        <div></div><div></div><div></div>
        <div></div><div></div><div></div>
        <div></div><div></div><div></div>
    </div>
</div>
"""

st.markdown(top_nav_html, unsafe_allow_html=True)

st.markdown('<div class="center-content">', unsafe_allow_html=True)
st.markdown('<div class="title">Searchly</div>', unsafe_allow_html=True)

query = st.text_input("", placeholder="Search the web or enter a URL", key="search", label_visibility="hidden", help="Press Enter to search")

st.markdown('</div>', unsafe_allow_html=True)

if query:
    st.write(f'You searched for: {query}')
