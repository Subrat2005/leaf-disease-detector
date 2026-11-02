import requests
import streamlit as st

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Leaf Disease Detection", page_icon="🌿")

st.title("🌿 Leaf Disease Detection")
st.write("Upload a clear photo of a plant leaf to check for disease.")

uploaded_file = st.file_uploader("Upload leaf image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Your image", width=300)

    if st.button("Detect Disease"):
        with st.spinner("Analyzing..."):
            files = {
                "file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)
            }
            try:
                response = requests.post(f"{API_URL}/detect", files=files, timeout=60)
            except requests.exceptions.RequestException:
                st.error("Could not reach the API. Is the backend running?")
                st.stop()

        if response.status_code != 200:
            st.error(response.json().get("detail", "Something went wrong"))
        else:
            result = response.json()

            if not result.get("valid_leaf"):
                st.warning("This doesn't look like a plant leaf. " + result.get("reason", ""))
            elif result.get("disease_detected"):
                st.error(f"Disease detected: {result.get('disease_name')}")
                st.write("**Severity:**", result.get("severity"))

                st.subheader("Symptoms")
                for symptom in result.get("symptoms", []):
                    st.write("-", symptom)

                st.subheader("Treatment")
                for step in result.get("treatment", []):
                    st.write("-", step)
            else:
                st.success("The leaf looks healthy! 🌱")

        st.caption("AI-generated result. Not a substitute for expert diagnosis.")