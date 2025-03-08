# import pandas as pd
import streamlit as st

st.set_page_config(page_title="UTM Generator", page_icon="📝")

st.title("UTM URL Builder")
st.write("This tool allows you to easily add campaign parameters to URLs so you can measure in :blue[Google Analytics].")

if "utm_url" not in st.session_state:
    st.session_state.utm_url = ""
    st.session_state.utm_id = ""
    st.session_state.utm_src = ""
    st.session_state.utm_medium = ""
    st.session_state.utm_name = ""
    st.session_state.utm_term = ""
    st.session_state.utm_content = ""

utm_url = st.text_input("Website URL* *(required)*", st.session_state.utm_url)
utm_id = st.text_input("Campaign ID", st.session_state.utm_id)
utm_src = st.text_input("Campaign Source* *(required)*", st.session_state.utm_src)
utm_medium = st.text_input("Campaign Medium* *(required)*", st.session_state.utm_medium)
utm_name = st.text_input("Campaign Name", st.session_state.utm_name)
utm_term = st.text_input("Campaign Term", st.session_state.utm_term)
utm_content = st.text_input("Campaign Content", st.session_state.utm_content)

generate_utm = st.button("Generate UTM")

if generate_utm:
    utm_params = {
        "utm_source": utm_src,
        "utm_medium": utm_medium,
        "utm_campaign": utm_name,
        "utm_id": utm_id,
        "utm_term": utm_term,
        "utm_content": utm_content
    }

    filtered_params = {k: v for k, v in utm_params.items() if v}

    if utm_url and filtered_params:
        utm_query = "&".join([f"{k}={v}" for k, v in filtered_params.items()])
        final_url = f"{utm_url}?{utm_query}"
        st.write(final_url)

        st.session_state.utm_url = ""
        st.session_state.utm_id = ""
        st.session_state.utm_src = ""
        st.session_state.utm_medium = ""
        st.session_state.utm_name = ""
        st.session_state.utm_term = ""
        st.session_state.utm_content = ""

        st.rerun()
    else:
        st.error("Please enter a valid Website URL and required UTM parameters.")

    add_to_csv = st.button("Add to Database")