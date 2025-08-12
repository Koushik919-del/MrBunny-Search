import streamlit as st

# Set page config for wider layout
st.set_page_config(page_title="My Search Engine", layout="wide")

# CSS styles for Google-like look and positioning
st.markdown("""
<style>
/* Remove Streamlit default padding */
.main {
    padding-top: 0rem;
    padding-left: 2rem;
    padding-right: 2rem;
}

/* Center everything vertically and horizontally */
body, html, #root > div {
    height: 100%;
    margin: 0;
}

.search-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-top: 15vh;
}

/* Google style title */
.title {
    font-family: Arial, sans-serif;
    font-weight: 400;
    font-size: 5rem;
    color: #4285F4;
    margin-bottom: 1rem;
}

/* Search input */
input[type="text"] {
    width: 500px;
    padding: 10px 15px;
    font-size: 1.2rem;
    border: 1px solid #dfe1e5;
    border-radius: 24px;
    box-shadow: none;
    outline: none;
    transition: box-shadow 0.3s ease;
}

input[type="text"]:focus {
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

# Main container for title and search box
st.markdown('<div class="search-container">', unsafe_allow_html=True)

st.markdown('<div class="title">Google</div>', unsafe_allow_html=True)

# Search form
with st.form(key='search_form'):
    query = st.text_input('', placeholder='Search Google or type a URL')
    submitted = st.form_submit_button('Google Search')

st.markdown('</div>', unsafe_allow_html=True)

if submitted:
    st.write(f'You searched for: {query}')
