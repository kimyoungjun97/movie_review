import pickle

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from konlpy.tag import Okt
from tensorflow.keras.preprocessing.text import *
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.preprocessing import LabelEncoder
from keras.utils import to_categorical #onehot 인코딩할 때 사용


pd.set_option('display.unicode.east_asian_width', True)
df = pd.read_csv('./crawling/naver_news.csv')
#print(df.head())
#print(df.info())

X = df['title']
Y = df['category']

encoder = LabelEncoder()
labeled_Y = encoder.fit_transform(Y) #np의 어레이 타입으로 바뀜
label = encoder.classes_
#print(labeled_Y[0])
#print(label)

with open('./models/encoder.pickle', 'wb') as f:
    pickle.dump(encoder, f)
onehot_Y = to_categorical(labeled_Y)
#print(onehot_Y)

#형태소 분리
okt = Okt()
print(type(X))
okt_morph_X = okt.morphs(X[0], stem=True)
print(X[0])
print(okt_morph_X)

#okt_pos_X = okt.pos(X[0])
#print(X[0])
#print(okt_pos_X)

#okt_nouns_X = okt.nouns(X[0])
#print(X[0])
#print(okt_nouns_X)

#okt_phrases_X = okt.phrases(X[0])
#print(X[0])
#print(okt_phrases_X)

for i in range(len(X)):
    X[i] = okt.morphs(X[i])

stopwords = pd.read_csv('../../PRJ_Movie_for_you-1/crawling_data/stopwords.csv', index_col=0)

for j in range(len(X)):
    words = []
    for i in range(len(X[j])):
        if len(X[j][i]) > 1:
            if len(X[j][i]) not in list(stopwords['stopword']):
                words.append(X[j][i])
    X[j] = ' '.join(words)
print(X)

token = Tokenizer()
token.fit_on_texts(X)
tokend_X = token.texts_to_sequences(X)
print(tokend_X[:5])       #단어를 숫자로 변경

with open('./models/news_token.pickle', 'wb') as f:
    pickle.dump(token, f)

wordsize = len(token.word_index) + 1
print(wordsize)
print(token.index_word)

max = 0
for i in range(len(tokend_X)):
    if max < len(tokend_X[i]):
        max = len(tokend_X[i])
print(max)

X_pad = pad_sequences(tokend_X, max)
print(X_pad[:10])

X_train, X_test, Y_train, Y_test = train_test_split(X_pad, onehot_Y, test_size=0.1)
print(X_train.shape, Y_train.shape)
print(X_test.shape, Y_test.shape)

xy = X_train, X_test, Y_train, Y_test
np.save('./crawling/news_data_max_{}_size_{}'.format(max, wordsize), xy)
