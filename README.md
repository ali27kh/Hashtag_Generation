# 📌 Hashtag Generation

## 📌 Project Overview
This project generates **relevant hashtags** from input text using **NLP techniques** with **spaCy**, **NLTK**, and a **Flask interface** for real-time testing. It extracts key nouns and adjectives, filters them, and formats them into hashtags for social media use. The system dynamically adjusts the number of hashtags based on text length, ensuring concise and effective output.

---

## 📂 Dataset
- **Input**: Raw text provided by the user.
- **Output**: List of hashtags (e.g., `#Keyword`) based on extracted nouns and adjectives.

---

## 🔍 Project Workflow

### **1. spaCy-Based Hashtag Generation**
Extract keywords (nouns, proper nouns, adjectives) and generate hashtags.

```python
import spacy

nlp = spacy.load("en_core_web_sm")

def optimize_hashtags_spacy(text):
    doc = nlp(text)
    keywords = [token.text.lower() for token in doc if token.pos_ in ("NOUN", "PROPN", "ADJ")]
    unique_keywords = list(dict.fromkeys(keywords))
    filtered = [word for word in unique_keywords if len(word) > 3]
    num = 5 if len(text.split()) > 20 else 3
    return [f"#{word.capitalize()}" for word in sorted(filtered, key=len, reverse=True)[:num]]
```

### **2. NLTK-Based Hashtag Generation**
Tokenize, tag, and generate hashtags from nouns and adjectives.

```python
import nltk
from nltk import word_tokenize, pos_tag

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def optimize_hashtags(content):
    tokens = word_tokenize(content)
    tags = pos_tag(tokens)
    keywords = [word.lower() for word, tag in tags if tag.startswith('NN') or tag == 'JJ']
    unique_keywords = list(dict.fromkeys(keywords))
    filtered = [word for word in unique_keywords if len(word) > 3]
    num = 5 if len(word_tokenize(content)) > 20 else 3
    return [f"#{word.capitalize()}" for word in sorted(filtered, key=len, reverse=True)[:num]]
```

### **3. Flask Interface for Testing (NLTK)**
Web interface to input text and generate hashtags in real-time.

```python
from flask import Flask, render_template, request
import nltk
from nltk import word_tokenize, pos_tag

app = Flask(__name__)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def optimize_hashtags(content):
    tokens = word_tokenize(content)
    tags = pos_tag(tokens)
    keywords = [word.lower() for word, tag in tags if tag.startswith('NN') or tag == 'JJ']
    unique_keywords = list(dict.fromkeys(keywords))
    filtered = [word for word in unique_keywords if len(word) > 3]
    num = 5 if len(word_tokenize(content)) > 20 else 3
    return [f"#{word.capitalize()}" for word in sorted(filtered, key=len, reverse=True)[:num]]

@app.route('/', methods=['GET', 'POST'])
def index():
    hashtags = None
    if request.method == 'POST':
        description_text = request.form.get('description', '').strip()
        hashtags = optimize_hashtags(description_text) if description_text else ["#NoDescription"]
    return render_template('index.html', hashtags=hashtags)

if __name__ == '__main__':
    app.run(debug=True, port=8080)
```

---

## 📊 Results
- **Output**: Generates 3-5 hashtags based on text length, e.g., `#MachineLearning`, `#SocialMedia`.
  
- **Test Video**:

  https://github.com/user-attachments/assets/8a610e94-a726-476a-8dca-fc182cd267bc

---

## 📦 Requirements
```bash
pip install spacy nltk flask
python -m spacy download en_core_web_sm
```

---

## ▶️ How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/hashtag-generation.git
   cd hashtag-generation
   ```
2. Create and activate virtual environment:
   ```bash
   python -m venv venv
   .\venv\Scripts\Activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Flask app:
   ```bash
   python app.py
   ```
   Access at `http://127.0.0.1:8080/` to input text and generate hashtags.

---

## 📌 Key Insights
- **spaCy** provides robust POS tagging for precise keyword extraction.
- **NLTK** offers a lightweight alternative for simpler setups.
- **Flask interface** enables real-time hashtag generation with user input.
- Dynamic hashtag count (3 for short text, 5 for longer) ensures relevance.

---

## 📜 License
MIT License
