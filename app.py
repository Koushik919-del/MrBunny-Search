import streamlit as st
import requests
import urllib.parse

st.set_page_config(page_title="My Search Engine", page_icon="🔍", layout="wide")

# CSS styles for layout, search bar, results, and menu
st.markdown("""
<style>
/* Reset margins */
body, .css-1d391kg {
    margin: 0;
    padding: 0;
    font-family: Arial, sans-serif;
}

/* Container for everything, centered */
.main {
    max-width: 700px;
    margin: 150px auto 50px;
    text-align: center;
}

/* Title styling */
h1 {
    font-weight: normal;
    margin-bottom: 40px;
}

/* Search box */
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

/* Search results */
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

/* Top-left 3x3 dots menu container */
.menu-icon {
    position: fixed;
    top: 15px;
    left: 15px;
    width: 36px;
    height: 36px;
    cursor: pointer;
    display: grid;
    grid-template-columns: repeat(3, 8px);
    grid-template-rows: repeat(3, 8px);
    gap: 4px;
    z-index: 1000;
}
.menu-icon div {
    background-color: #555;
    border-radius: 50%;
}

/* Popup menu for shortcuts */
.menu-popup {
    position: fixed;
    top: 60px;
    left: 15px;
    background: white;
    border: 1px solid #ddd;
    box-shadow: 0 4px 12px rgba(0,0,0,0.1);
    border-radius: 8px;
    padding: 10px;
    display: none;
    width: 180px;
    z-index: 1000;
}

/* Show popup when active */
.menu-popup.active {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 10px;
}

/* Shortcut tiles */
.shortcut {
    width: 40px;
    height: 40px;
    background: #f1f1f1;
    border-radius: 8px;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 10px;
    color: #333;
    text-decoration: none;
    user-select: none;
    flex-direction: column;
    font-weight: bold;
}
.shortcut:hover {
    background: #e2e2e2;
    color: #4285f4;
}

/* Shortcut label */
.shortcut-label {
    font-size: 9px;
    margin-top: 4px;
}
</style>
""", unsafe_allow_html=True)

# JavaScript for toggling the menu popup
st.markdown("""
<script>
const menuIcon = document.querySelector('.menu-icon');
const menuPopup = document.querySelector('.menu-popup');

menuIcon?.addEventListener('click', () => {
    if (menuPopup.classList.contains('active')) {
        menuPopup.classList.remove('active');
    } else {
        menuPopup.classList.add('active');
    }
});

// Close the menu if clicking outside
document.addEventListener('click', (e) => {
    if (!menuIcon.contains(e.target) && !menuPopup.contains(e.target)) {
        menuPopup.classList.remove('active');
    }
});
</script>
""", unsafe_allow_html=True)

# Render the 3x3 dots menu
st.markdown("""
<div class="menu-icon">
    <div></div><div></div><div></div>
    <div></div><div></div><div></div>
    <div></div><div></div><div></div>
</div>
<div class="menu-popup" id="menuPopup">
    <a href="https://mrbunny-ai.streamlit.app" target="_blank" class="shortcut" title="MrBunny AI">
        🐰<div class="shortcut-label">MrBunny</div>
    </a>
    <a href="https://nova-translate.streamlit.app" target="_blank" class="shortcut" title="Nova Translate">
        🌐<div class="shortcut-label">Nova</div>
    </a>
    <!-- Add more shortcuts here if you want -->
</div>
""", unsafe_allow_html=True)

# Main app container
query_from_url = st.query_params.get("q", [""])[0]

with st.container():
    st.markdown('<div class="main">', unsafe_allow_html=True)
    st.markdown('<h1>My Search Engine</h1>', unsafe_allow_html=True)
    
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
