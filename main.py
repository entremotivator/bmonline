import streamlit as st

def main():
    st.set_page_config(page_title="Enhanced Multi-Page App", layout="wide")
    
    st.sidebar.title("Navigation")
    st.sidebar.markdown("### Pages:")
    st.sidebar.info("""
    - **Credit Letter Generator**
    - **Contact Generator**
    """)

    st.title("Welcome to the Enhanced Streamlit App!")
    st.markdown("""
    This application offers the following functionalities:
    - **Credit Letter Generator**: Create professional credit dispute letters.
    - **Contact Generator**: Generate detailed contact information.

    Use the sidebar to navigate between the pages.
    """)

if __name__ == "__main__":
    main()
