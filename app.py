import streamlit as st

st.set_page_config(page_title="Google", layout="wide")

# CSS for Google homepage style
st.markdown("""
<style>
/* Reset and body */
body, html, #root > div {
    height: 100%;
    margin: 0;
    font-family: Arial, sans-serif;
    background: white;
}

/* Container for the whole page */
.page {
    display: flex;
    flex-direction: column;
    height: 100vh;
}

/* Top navigation bar on right side */
.top-nav {
    display: flex;
    justify-content: flex-end;
    padding: 15px 30px;
    font-size: 14px;
    color: #5f6368;
    gap: 20px;
    align-items: center;
}

/* Links in top nav */
.top-nav a {
    color: #5f6368;
    text-decoration: none;
    font-weight: 500;
    cursor: pointer;
}
.top-nav a:hover {
    text-decoration: underline;
}

/* Apps grid icon */
.apps-icon {
    width: 32px;
    height: 32px;
    cursor: pointer;
    display: grid;
    grid-template-columns: repeat(3, 8px);
    grid-template-rows: repeat(3, 8px);
    gap: 6px;
}

.apps-icon div {
    background-color: #5f6368;
    border-radius: 2px;
}

/* Profile avatar circle */
.profile-avatar {
    width: 32px;
    height: 32px;
    border-radius: 50%;
    background-color: #4285f4;
    color: white;
    font-weight: bold;
    display: flex;
    justify-content: center;
    align-items: center;
    font-size: 14px;
    user-select: none;
}

/* Center container for logo and search */
.center-content {
    flex-grow: 1;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
}

/* Google logo */
.google-logo {
    width: 272px;
    height: 92px;
    margin-bottom: 20px;
}

/* Search box container */
.search-container {
    display: flex;
    justify-content: center;
    width: 100%;
    max-width: 584px;
    border: 1px solid #dfe1e5;
    box-shadow: 0 1px 6px rgb(32 33 36 / 28%);
    border-radius: 24px;
    padding: 0 15px;
    height: 44px;
    margin-bottom: 30px;
}

.search-container input {
    flex-grow: 1;
    border: none;
    outline: none;
    font-size: 16px;
    padding: 0 10px;
    height: 100%;
}

/* Buttons container */
.buttons {
    display: flex;
    justify-content: center;
    gap: 10px;
}

.buttons button {
    background-color: #f8f9fa;
    border: 1px solid #f8f9fa;
    border-radius: 4px;
    color: #3c4043;
    font-size: 14px;
    padding: 10px 16px;
    cursor: pointer;
    box-shadow: 0 1px 1px rgb(0 0 0 / 0.1);
    transition: background-color 0.2s ease;
}

.buttons button:hover {
    border: 1px solid #c6c6c6;
    background-color: #f1f3f4;
}

/* Footer */
.footer {
    font-size: 14px;
    color: #70757a;
    padding: 15px 30px;
    border-top: 1px solid #e4e4e4;
    display: flex;
    justify-content: space-between;
    flex-wrap: wrap;
}

/* Footer left and right sections */
.footer div {
    margin: 5px 0;
}
.footer a {
    color: #70757a;
    text-decoration: none;
    margin: 0 8px;
}
.footer a:hover {
    text-decoration: underline;
}
</style>
""", unsafe_allow_html=True)

# HTML for Google logo from official source
google_logo = """
<img class="google-logo" src="https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png" alt="Google Logo" />
"""

# Top nav with Gmail, Images, apps icon, and profile avatar
top_nav_html = """
<div class="top-nav">
    <a href="https://mail.google.com" target="_blank" rel="noopener noreferrer">Gmail</a>
    <a href="https://www.google.com/imghp" target="_blank" rel="noopener noreferrer">Images</a>
    <div class="apps-icon" title="Google apps">
        <div></div><div></div><div></div>
        <div></div><div></div><div></div>
        <div></div><div></div><div></div>
    </div>
    <div class="profile-avatar" title="Profile">K</div>
</div>
"""

# Search input form (submit on Enter)
search_form_html = """
<form action="" method="get" onsubmit="return false;">
    <div class="search-container">
        <input type="text" id="searchInput" placeholder="Search Google or type a URL" autocomplete="off" />
    </div>
    <div class="buttons">
        <button type="submit" onclick="submitSearch()">Google Search</button>
        <button type="submit" onclick="feelingLucky()">I'm Feeling Lucky</button>
    </div>
</form>

<script>
    const input = document.getElementById('searchInput');
    input.addEventListener('keydown', function(event) {
        if(event.key === 'Enter') {
            submitSearch();
        }
    });

    function submitSearch() {
        const query = input.value.trim();
        if (query.length > 0) {
            alert("You searched for: " + query);
            // Here you can add code to actually do a search
        }
    }
    function feelingLucky() {
        const query = input.value.trim();
        if (query.length > 0) {
            alert("I'm Feeling Lucky search for: " + query);
            // Here you can add code for "I'm Feeling Lucky"
        }
    }
</script>
"""

footer_html = """
<div class="footer">
    <div>United States</div>
    <div>
        <a href="#">Advertising</a>
        <a href="#">Business</a>
        <a href="#">About</a>
        <a href="#">Privacy</a>
        <a href="#">Terms</a>
        <a href="#">Settings</a>
    </div>
</div>
"""

# Build full page
st.markdown('<div class="page">', unsafe_allow_html=True)
st.markdown(top_nav_html, unsafe_allow_html=True)
st.markdown(google_logo, unsafe_allow_html=True)
st.markdown(search_form_html, unsafe_allow_html=True)
st.markdown(footer_html, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
