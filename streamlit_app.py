import streamlit as st
from ai_modules.writer import spin_text

st.set_page_config(page_title="📚 Book Chapter Rewriter", layout="centered")

st.title("📚 Automated Book Chapter Rewriter")
st.markdown("Upload a `.txt` file and get an AI-rewritten version using Gemini.")

uploaded_file = st.file_uploader("📂 Upload your chapter (.txt)", type=["txt"])

if uploaded_file is not None:
    input_text = uploaded_file.read().decode("utf-8")
    
    st.subheader("📖 Original Chapter Content")
    st.text_area("Original Text", input_text, height=300)

    if st.button("🔁 Rewrite with Gemini AI"):
        with st.spinner("Rewriting in progress..."):
            rewritten = spin_text(input_text)
        st.success("✅ Chapter rewritten successfully!")
        st.subheader("📝 Rewritten Chapter")
        st.text_area("Rewritten Text", rewritten, height=300)

        st.download_button("💾 Download Rewritten Chapter", data=rewritten, file_name="chapter1_rewritten.txt", mime="text/plain")
