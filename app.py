import streamlit as st
import torch

from transformers import (
    BertTokenizer,
    BertForSequenceClassification
)

# Load tokenizer
tokenizer = BertTokenizer.from_pretrained(
    "bert_spam_model"
)

# Load model
model = BertForSequenceClassification.from_pretrained(
    "bert_spam_model"
)

# Device setup
device = torch.device(
    "cuda" if torch.cuda.is_available() else "cpu"
)

model.to(device)

# App title
st.title("Instagram Spam Detector")

st.write(
    "Enter an Instagram comment to check whether it is spam or legitimate."
)

# User input
comment = st.text_area("Enter Comment")

# Prediction button
if st.button("Detect Spam"):
    
    if comment.strip() == "":
        
        st.warning("Please enter a comment.")
    
    else:
        
        # Tokenize text
        inputs = tokenizer(
            comment,
            return_tensors="pt",
            truncation=True,
            padding=True,
            max_length=128
        )

        # Move tensors to device
        inputs = {
            key: value.to(device)
            for key, value in inputs.items()
        }

        # Prediction
        with torch.no_grad():
            outputs = model(**inputs)

        prediction = torch.argmax(
            outputs.logits,
            dim=1
        )

        # Output
        if prediction.item() == 1:
            
            st.error("⚠️ Spam Comment Detected")
        
        else:
            
            st.success("✅ Legitimate Comment")