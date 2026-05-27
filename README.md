# Instagram Spam Detection using BERT

An AI-powered Instagram Spam Detection web application built using BERT, Streamlit, and Python.

## Project Overview

Social media platforms often contain spam comments posted by bots.  
This project uses Natural Language Processing (NLP) and the BERT transformer model to classify comments as:

- Spam
- Legitimate

The application is built with Streamlit and uses a fine-tuned BERT model trained on the YouTube Spam Collection Dataset.

---

## Features

- Detects spam Instagram comments
- Uses BERT transformer model
- Streamlit web interface
- Real-time prediction
- NLP-based classification

---

## Technologies Used

- Python
- BERT
- Transformers
- PyTorch
- Streamlit
- Google Colab
- VS Code

---

## Dataset

Dataset used:

YouTube Spam Collection Dataset

Source:
https://www.kaggle.com/datasets/ahsenwaheed/youtube-spam-dataset

---

## Project Structure

```bash
InstagramSpamDetector/
│
├── app.py
├── requirements.txt
├── bert_spam_model/
├── README.md
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/aaradhyistic/InstagramSpamDetector.git
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Run Application

```bash
streamlit run app.py
```

---

## Example Inputs

### Spam Comment

```text
Earn money online fast click this link
```

### Legitimate Comment

```text
Nice picture bro
```

---

## Model Information

The project uses a fine-tuned BERT model for spam classification.

Note:
Large model files may not be uploaded to GitHub due to GitHub file size limitations.

---

## Future Improvements

- Connect with Instagram API
- Deploy on Streamlit Cloud
- Use DistilBERT for lighter deployment
- Improve UI design
- Add live comment scraping

---

## Author

Aaradhya Tiwari
