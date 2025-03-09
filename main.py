# import pandas as pd
import streamlit as st

st.set_page_config(page_title="UTM Generator", page_icon="📝")

st.title("UTM URL Builder")
st.write("This tool allows you to easily add campaign parameters to URLs so you can measure in :blue[Google Analytics].")


utm_url = st.text_input("Website URL* *(required)*")
utm_id = st.text_input("Campaign ID")
utm_src = st.selectbox("Campaign Source* *(required)*", ("facebook", "instagram", "twitter", "newsletter","tiktok"))
utm_medium = st.selectbox("Campaign Medium* *(required)*", ("social_media", "email", "push_notification", "website", "fb_ads", "google_ads", "tiktok_ads"))
utm_name = st.selectbox("Campaign Name* *(required)*", ("organic", "paid"))
utm_term = st.text_input("Campaign Term")
utm_content = st.text_input("Campaign Content")

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


    add_to_csv = st.button("Add to Database")