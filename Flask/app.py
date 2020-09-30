import joblib
from flask import Flask, request, render_template, Response, redirect, url_for
import clean_predict
import pandas as pd
import numpy as np
from wordcloud import WordCloud   
import matplotlib.pyplot as plt
from werkzeug.utils import secure_filename
import os
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
from sklearn.decomposition import PCA
from time import sleep

UPLOAD_FOLDER = r'D:\FinalProject\Flask\temp'
ALLOWED_EXTENSION = set(['csv', 'xlsx'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSION

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods= ['POST'])
def hasil():
    if request.method == 'POST':
        input = request.form  
        product = str(input['product']) 
        file = request.files['file']

        if 'file' not in request.files:
            flash('No file part')
            return render_template('index.html')
                
        if file.filename == '':
            flash('No selected file')
            return render_template('index.html')
                
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
        return render_template('index.html')

@app.route('/predict', methods = ['POST'])
def predict():
    if request.method == 'POST':
        product = request.form['product']
        review = os.listdir(r'D:\FinalProject\Flask\temp')[0]
        df = pd.read_csv(r'D:\FinalProject\Flask\temp\{}'.format(review))
        # ---- Text Preprocessing ----
        df['clean'] = df['Review']#.apply(clean_predict)
        pipe = Pipeline([('count', CountVectorizer(vocabulary=bow)),
                 ('tfid', TfidfTransformer())]).fit(df['clean'])
        x = pipe.transform(df['clean']).toarray()
        pca = PCA(n_components=100)
        x = pca.fit_transform(x)

        # ---- Predict ----
        predict = list(model.predict(x)) 
        count = []
        sen_pct = []
        for i in range(-1,2):
            pred_count = predict.count(i)
            count.append(pred_count)
            sen_pct.append(round(pred_count/len(predict)*100, 2))
        
        # ---
        review = pd.DataFrame({'review': df['clean'].values, 'sentiment': predict})

        # --- WordCloud Prep ---
        def word_frequency(text):
            wordList = text.split()
            # generate frequencey of word to dictionary 
            wordFreq = {word : wordList.count(word) for word in wordList}
            return wordFreq

        def wordcloud_freq_pos(word_freq,title,figure_size = (10,5)):
            wordcloud.generate_from_frequencies(word_freq)
            plt.figure(figsize=figure_size)
            plt.imshow(wordcloud)
            plt.axis('off')
            plt.title(title)
            plt.savefig(r'D:\FinalProject\Flask\static\wordcloud_pos.jpg')
        
        def wordcloud_freq_neg(word_freq,title,figure_size = (10,5)):
            wordcloud.generate_from_frequencies(word_freq)
            plt.figure(figsize=figure_size)
            plt.imshow(wordcloud)
            plt.axis('off')
            plt.title(title)
            plt.savefig(r'D:\FinalProject\Flask\static\wordcloud_neg.jpg')

        # ---- WordCloud Positive ----   
        review_pos = " ".join(review[review['sentiment'] == 1]['review'].dropna())
        review_pos = word_frequency(review_pos)
        # review_pos = {'a': 2, 'ff': 2} 
        zipping = list(zip(review_pos.values(), review_pos.keys()))
        zipping.sort()
        review_pos = {}
        for values, keys in zipping[-30:]:
            review_pos[keys] = values
        wordcloud = WordCloud(width = 5000,
                            height = 2500,
                            colormap ='inferno',
                            background_color='white')
        wordcloud_freq_pos(review_pos, f'Most Frequent Words in the Latest Positive Reviews for {product}')

        # ---- Wordcloud Neg ---
        review_neg = " ".join(review[review['sentiment'] == -1]['review'].dropna())
        review_neg = word_frequency(review_neg)
        # review_neg = {'a': 2, 'ff': 2} 
        zipping = list(zip(review_neg.values(), review_neg.keys()))
        zipping.sort()
        review_neg = {}
        for values, keys in zipping[-30:]:
            review_neg[keys] = values
        wordcloud = WordCloud(width = 5000,
                            height = 2500,
                            colormap ='Blues',
                            background_color='black')
        wordcloud_freq_neg(review_neg, f'Most Frequent Words in the Latest Negative Reviews for {product}')
        sleep(20)
    
        return render_template('predict.html', data = product.title(), series = count, pct = sen_pct)


@app.route('/dataset', methods = ['POST', 'GET'])
def data(chartID = 'chart_ID', chart_type = 'count', chart_height = 500):
    if request.method == 'POST':  
        df = pd.read_csv(r'D:\FinalProject\DataBase\Input\01. SkincareReview.csv')
        dfhead = df.head()   
        
        barh = df.groupby('Brand').mean()['Rating'].sort_values(ascending = False)[:11].sort_values() 
        print(barh.index)
        print(barh.values)
        
        return render_template('dataset.html', tables= [dfhead.to_html(classes = 'data', header = 'true')], titles=df.columns.values)



if __name__ == '__main__':
    model = joblib.load(r'D:\FinalProject\DataBase\Output\model')
    bow = joblib.load(r'D:\FinalProject\DataBase\Output\Output For Modelling\bow')
    app.run(debug = True)
