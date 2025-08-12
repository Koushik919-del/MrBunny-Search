import streamlit as st

st.set_page_config(page_title="My Search Engine", layout="wide")

st.markdown("""
<style>
/* Remove default Streamlit padding */
.main {
    padding-top: 0rem;
    padding-left: 2rem;
    padding-right: 2rem;
}

/* Body and html full height */
body, html, #root > div {
    height: 100%;
    margin: 0;
}

/* Top search bar container */
.top-bar {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    background: white;
    border-bottom: 1px solid #ddd;
    padding: 10px 20px;
    display: flex;
    justify-content: center;
    z-index: 1000;
}

/* Top search input */
.top-bar input[type="text"] {
    width: 600px;
    padding: 8px 12px;
    font-size: 1rem;
    border: 1px solid #dfe1e5;
    border-radius: 20px;
    outline: none;
    box-shadow: none;
    transition: box-shadow 0.3s ease;
}

.top-bar input[type="text"]:focus {
    box-shadow: 0 0 5px rgba(66, 133, 244, 0.8);
    border-color: #4285F4;
}

/* Center container for title and main search */
.center-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-top: 20vh; /* push content down */
}

/* Google style title */
.title {
    font-family: Arial, sans-serif;
    font-weight: 400;
    font-size: 5rem;
    color: #4285F4;
    margin-bottom: 1.5rem;
}

/* Main middle search input */
.center-container input[type="text"] {
    width: 350px;
    padding: 10px 15px;
    font-size: 1.2rem;
    border: 1px solid #dfe1e5;
    border-radius: 24px;
    box-shadow: none;
    outline: none;
    transition: box-shadow 0.3s ease;
    text-align: center;
}

.center-container input[type="text"]:focus {
    box-shadow: 0 0 5px rgba(66, 133, 244, 0.8);
    border-color: #4285F4;
}

/* Search button */
button {
    margin-left: 10px;
    padding: 10px 20px;
    font-size: 1rem;
    background-color: #f8f9fa;
    border: 1px solid #f8f9fa;
    border-radius: 4px;
    cursor: pointer;
    color: #3c4043;
    box-shadow: 0 1px 1px rgb(0 0 0 / 0.1);
    transition: background-color 0.2s ease;
}

button:hover {
    background-color: #f1f3f4;
    border: 1px solid #c6c6c6;
}

/* Top left 3x3 grid icon */
.grid-icon {
    position: fixed;
    top: 15px;
    left: 15px;
    width: 32px;
    height: 32px;
    cursor: pointer;
    display: flex;
    flex-wrap: wrap;
    gap: 4px;
    z-index: 1100;
}

.grid-icon div {
    background-color: #5f6368;
    width: 8px;
    height: 8px;
    border-radius: 2px;
}
</style>
""", unsafe_allow_html=True)

# 3x3 grid icon HTML
grid_html = """
<div class="grid-icon" title="Apps">
  <div></div><div></div><div></div>
  <div></div><div></div><div></div>
  <div></div><div></div><div></div>
</div>
"""
st.markdown(grid_html, unsafe_allow_html=True)

# Top search bar form
with st.form(key='top_search_form'):
    st.markdown('<div class="top-bar">', unsafe_allow_html=True)
    top_query = st.text_input('', placeholder='Search Google or type a URL', key='top_search')
    top_submitted = st.form_submit_button('Search')
    st.markdown('</div>', unsafe_allow_html=True)

# Center content with Google title and smaller search box
st.markdown('<div class="center-container">', unsafe_allow_html=True)
st.markdown('<div class="title">Google</div>', unsafe_allow_html=True)

with st.form(key='center_search_form'):
    center_query = st.text_input('', placeholder='Search Google or type a URL', key='center_search')
    center_submitted = st.form_submit_button('Google Search')
st.markdown('</div>', unsafe_allow_html=True)

# Show what was searched from either bar
if top_submitted and top_query.strip() != '':
    st.write(f'You searched (top bar): {top_query}')

if center_submitted and center_query.strip() != '':
    st.write(f'You searched (center bar): {center_query}')
