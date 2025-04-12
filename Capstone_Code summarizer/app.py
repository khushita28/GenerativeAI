import streamlit as st
from groq_client import summarize_code
from hf_client import summarize_with_hf_api

# Streamlit app config
st.set_page_config(page_title="Code Summarizer", layout="wide", page_icon="🧠")
st.title("🧠 Code Summarizer")
st.caption("Powered by Groq's LLaMA 3.3 and Hugging Face's Codet5p")

# Layout: Left for input, Right for output
left, right = st.columns([1, 2], gap="large")

with left:
    st.header("📥 Input")
    
    model_choice = st.selectbox("Choose Model", ["Groq LLaMA 3.3", "Hugging Face CodeT5p"])
    input_mode = st.radio("Input Method", ["Paste Code", "Upload File"])

    code = ""
    if input_mode == "Upload File":
        uploaded_file = st.file_uploader("Upload a code file", type=["py", "js", "java", "cpp", "txt"])
        if uploaded_file:
            code = uploaded_file.read().decode("utf-8")
    elif input_mode == "Paste Code":
        code = st.text_area("Paste your code here", height=300)

    submitted = st.button("✨ Summarize Code")

with right:
    st.header("🧠 Summary")
    
    if submitted:
        if code.strip():
            with st.spinner("Generating summary..."):
                if model_choice == "Groq LLaMA 3.3":
                    summary = summarize_code(code)
                else:
                    summary = summarize_with_hf_api(code)

            st.subheader("📄 Summary Result")
            st.success(summary)
            st.download_button("📥 Download Summary", summary, file_name="code_summary.txt")
        else:
            st.warning("⚠️ Please provide code input before summarizing.")
