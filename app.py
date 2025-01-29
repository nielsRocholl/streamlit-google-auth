import streamlit as st
from auth import Authenticator

st.title("Streamlit Google Auth")

allowed_users = st.secrets["ALLOWED_USERS"].split(",")

authenticator = Authenticator(
    allowed_users=allowed_users,
    token_key=st.secrets["TOKEN_KEY"],
    client_secret=st.secrets["CLIENT_SECRET"],  # Changed from secret_path
    redirect_uri="https://g-signin.streamlit.app/"  # Updated for production
)

# Sidebar auth components
with st.sidebar:
    if st.session_state.get("connected"):
        if st.button("Log out", use_container_width=True):
            authenticator.logout()
            st.rerun()
    else:
        auth_url = authenticator.get_auth_url()  # New helper method
        st.link_button("Login with Google", auth_url, use_container_width=True)

# Main content
authenticator.check_auth()

if st.session_state.get("connected"):
    st.write(f"Welcome! {st.session_state['user_info'].get('email')}")
else:
    st.write("You need to log in first...")
