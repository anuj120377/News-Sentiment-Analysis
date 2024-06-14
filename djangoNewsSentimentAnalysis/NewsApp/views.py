from django.shortcuts import render




import numpy as np
import tensorflow
import keras
from keras.models import load_model

import pickle
# Load the model from the file

model = load_model('./savedModels/model_NewsSentimentAnalysis.h5')

with open('./savedModels/tokenizer.pkl','rb') as file:
    tokenizer = pickle.load(file)

with open('./savedModels/stop_words.pkl','rb') as file:
    stop_words = pickle.load(file)

with open('./savedModels/stemmed_word_index.pkl','rb') as file:
    stemmed_word_index = pickle.load(file)


word_index = tokenizer.word_index
index_word = tokenizer.index_word

stemmed_index_word = {index:word for word,index in stemmed_word_index.items()}

#Dealing with Stop Words
def remove_stop_words(sequence):
    filtered_sequence = []
    for token in sequence:
        if index_word[token] not in stop_words:
            filtered_sequence.append(token)
    
    return filtered_sequence

import nltk
nltk.download('punkt')
from nltk.stem import PorterStemmer
portStem = PorterStemmer()


#Stemming
def stem_sequences(sequence):
    stemmed_sequence = []
    for token in sequence:
        word = portStem.stem(index_word[token])
        if word in stemmed_word_index:
            stemmed_sequence.append(stemmed_word_index[word])
        else:
            stemmed_sequence.append(stemmed_word_index['<unk>'])

    return stemmed_sequence

from keras.preprocessing.sequence import pad_sequences





def predictor(request):

    if request.method == 'POST':
        newsData = request.POST['news']
        newsSequence = tokenizer.texts_to_sequences([newsData])

        newsSequence = remove_stop_words(newsSequence[0])
        newsSequence = stem_sequences(newsSequence)
        
        newsSequence = pad_sequences([newsSequence],padding='post',maxlen=50)

        y_pred = model.predict(newsSequence)
        
        y_pred = np.argmax(y_pred, axis=1)[0]

        if y_pred==0:
            y_pred = "Negative"
        if y_pred==1:
            y_pred = "Neutral"
        if y_pred==2:
            y_pred = "Positive"

        
        return render(request,'main.html',{'sentiment' : y_pred})



    return render(request, 'main.html')




"""
def formInfo(request):
    newsData = request.GET['news']
    newsSequence = tokenizer.texts_to_sequences([newsData])

    newsSequence = remove_stop_words(newsSequence[0])
    newsSequence = stem_sequences(newsSequence)
    
    newsSequence = pad_sequences([newsSequence],padding='post',maxlen=50)

    y_pred = model.predict(newsSequence)
    
    y_pred = np.argmax(y_pred, axis=1)[0]

    if y_pred==0:
        y_pred = "Negative"
    if y_pred==1:
        y_pred = "Neutral"
    if y_pred==2:
        y_pred = "Positive"

    
    return render(request,'result.html',{'sentiment' : y_pred})

"""    