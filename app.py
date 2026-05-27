import streamlit as st

st.title("Instagram Spam Detector")

comment = st.text_area("Enter Instagram Comment")

spam_keywords = [
    "money",
    "earn",
    "free",
    "click",
    "bio",
    "collab",
    "link",
    "follow",
    "dm now"
]

if st.button("Detect Spam"):

    if comment.strip() == "":
        st.warning("Please enter a comment.")

    else:

        comment_lower = comment.lower()

        is_spam = any(
            word in comment_lower
            for word in spam_keywords
        )

        if is_spam:
            st.error("⚠️ Spam Comment Detected")

        else:
            st.success("✅ Legitimate Comment")
