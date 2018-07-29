from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from data_scraper import gather_data
import pandas as pd

# Use data scraper only if file with the data does not exist

convo_frame = gather_data(20)
vectorizer = TfidfVectorizer(ngram_range=(1,3))
vec = vectorizer.fit_transform(convo_frame['q'])

# Method that chooses the most similar question to the question given and returns
# the answer for it.

def get_response(q):
    my_q = vectorizer.transform([q])
    cs = cosine_similarity(my_q, vec)
    rs = pd.Series(cs[0]).sort_values(ascending=False)
    rsi = rs.index[0]
    return convo_frame.iloc[rsi]['a']
                  