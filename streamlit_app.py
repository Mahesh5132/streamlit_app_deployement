import streamlit as st

def main():
    st.set_page_config(page_title="My Streamlit App", layout="centered")
    
    st.title("Welcome to My Streamlit App")
    
    st.sidebar.header("Navigation")
    page = st.sidebar.selectbox("Choose a page", ["Home", "About"])
    
    if page == "Home":
        st.header("Home Page")
        st.write("This is the home page of the Streamlit app.")
        user_input = st.text_input("Enter some text:")
        if st.button("Submit"):
            st.write(f"You entered: {user_input}")
    
    elif page == "About":
        st.header("About Page")
        st.write("This is a simple Streamlit app demonstrating basic features.")
        
if __name__ == "__main__":
    main()