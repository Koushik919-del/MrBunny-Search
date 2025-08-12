import streamlit as st

st.set_page_config(page_title="Google", layout="wide")

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
    color: #5f6368;
    gap: 20px;
    align-items: center;
    position: fixed;
    width: 100%;
    top: 0;
    background: white;
    z-index: 10;
}

.top-nav a {
    color: #5f6368;
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
    background-color: #5f6368;
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

/* Google logo */
.google-logo {
    width: 272px;
    height: 92px;
    margin-bottom: 20px;
}

/* Search input */
.search-input {
    width: 500px;
    max-width: 90vw;
    padding: 12px 20px;
    font-size: 16px;
    border: 1px solid #dfe1e5;
    border-radius: 24px;
    box-shadow: 0 1px 6px rgb(32 33 36 / 28%);
    outline: none;
    transition: box-shadow 0.3s ease;
    text-align: center;
}

.search-input:focus {
    box-shadow: 0 0 5px rgba(66, 133, 244, 0.8);
    border-color: #4285F4;
}
</style>
""", unsafe_allow_html=True)

top_nav_html = """
<div class="top-nav">
    <a href="https://mail.google.com" target="_blank" rel="noopener noreferrer">Gmail</a>
    <a href="https://www.google.com/imghp" target="_blank" rel="noopener noreferrer">Images</a>
    <div class="apps-icon" title="Google apps">
        <div></div><div></div><div></div>
        <div></div><div></div><div></div>
        <div></div><div></div><div></div>
    </div>
</div>
"""

st.markdown(top_nav_html, unsafe_allow_html=True)

st.markdown("""
<div class="center-content">
    <img class="google-logo" src="https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png" alt="Google Logo" />
</div>
""", unsafe_allow_html=True)

query = st.text_input("", placeholder="Search Google or type a URL", key="search", label_visibility="hidden")

if query:
    st.write(f'You searched for: {query}')
