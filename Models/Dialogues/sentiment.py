
# some tests on sentiment analysis

import data,utils

from nltk.sentiment.vader import SentimentIntensityAnalyzer

films = data.load_data('/Users/Juste/Documents/ComplexSystems/FilmsMining/Data/cornell_movie-dialogs_corpus/movie_lines.txt','/Users/Juste/Documents/ComplexSystems/FilmsMining/Data/cornell_movie-dialogs_corpus/movie_conversations.txt')

sid = SentimentIntensityAnalyzer()

sentiment_ts = {}

for film in films.keys() :
    negts=[];neuts=[];posts=[]
    for dialogue in films[film]:
        for sentence in dialogue :
            print sentence
            polarity = sid.polarity_scores(sentence)
            print(polarity)
            negts.append(polarity['neg'])
            neuts.append(polarity['neu'])
            posts.append(polarity['pos'])
    sentiment_ts[film+'_neg']=negts
    sentiment_ts[film+'_pos']=posts
    sentiment_ts[film+'_neu']=neuts

# normlize ts to have same length ?
# or better reading customively in R

utils.export_dico_ts_csv(sentiment_ts,'res/sentiment_ts_')
