from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import data_scraper as ds
import os.path


# gather_data saves the data to the file if none is found or it's empty.

if(not os.path.isfile("firstCheck.txt") or os.path.getsize("firstCheck.txt") == 0):
    ds.scrape(3)

# Preprocessing the data from the file
def data_preprocessing():
    inputFile = []
    with open('firstCheck.txt', 'r') as f:
        file = f.read().split('\n')
        for pair in file:
            pairList = pair.split("|")[:-1]
            if(len(pairList) == 2):
                cleanedPair = []
                for p in pairList:
                    cleanedPair.append(p.strip('b')[0:-1])            
                inputFile.append(cleanedPair)
                
    # Converting the input into a pandas frame
    convo_frame = pd.Series(dict(inputFile)).to_frame().reset_index()
    convo_frame.columns = ['q','a']
    return convo_frame

vectorizer = TfidfVectorizer(ngram_range=(1,3))

# Learning
def fitting():
    frame = data_preprocessing()  
    return (vectorizer.fit_transform(frame['q']), frame)

# Method that chooses the most similar question to the question given and returns
# the answer for it.
    
vec, convo_frame = fitting()

def get_response(q):
    my_q = vectorizer.transform([q])
    cs = cosine_similarity(my_q, vec)
    rs = pd.Series(cs[0]).sort_values(ascending=False)
    rsi = rs.index[0]
    return convo_frame.iloc[rsi]['a']
                  