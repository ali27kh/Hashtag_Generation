from flask import Flask, render_template, request
import nltk
from nltk import word_tokenize, pos_tag

app = Flask(__name__)

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')

def extract_keywords(content):
    tokens = word_tokenize(content)
    tags = pos_tag(tokens)
    return [word.lower() for word, tag in tags if tag.startswith('NN') or tag == 'JJ']

def generate_hashtags(keywords, num_hashtags):
    unique_keywords = list(dict.fromkeys(keywords))
    filtered = [word for word in unique_keywords if len(word) > 3]
    sorted_keywords = sorted(filtered, key=len, reverse=True)
    return [f"#{word.capitalize()}" for word in sorted_keywords[:num_hashtags]]

def optimize_hashtags(content):
    num = 5 if len(word_tokenize(content)) > 20 else 3
    keywords = extract_keywords(content)
    return generate_hashtags(keywords, num)

@app.route('/', methods=['GET', 'POST'])
def index():
    hashtags = None

    if request.method == 'POST':
        description_text = request.form.get('description', '').strip()
        if description_text:
            hashtags = optimize_hashtags(description_text)
        else:
            hashtags = ["#NoDescription"]

    return render_template('index.html', hashtags=hashtags)

if __name__ == '__main__':
    app.run(debug=True, port=8080)
