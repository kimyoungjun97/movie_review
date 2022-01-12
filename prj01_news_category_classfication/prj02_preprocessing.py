import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from konlpy.tag import Okt
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.preprocessing import LabelEncoder
from keras.utils import to_categorical
import pickle

pd.set_option('display.unicode.east_asian_width', True)
df = pd.read_csv('../prj02/crawling/movie_genre_all.csv', index_col=False)
df.dropna(inplace=True)
print(df.head())
print(df.info())

X = df['summary']
Y = df['genre']

encoder = LabelEncoder()
labeled_Y = encoder.fit_transform(Y)
label = encoder.classes_
print(labeled_Y[0])
print(label)
with open('./models/encoder.pickle', 'wb') as f:
    pickle.dump(encoder, f)
onehot_Y = to_categorical(labeled_Y)
print(onehot_Y)

#okt = Okt()
# print(type(X))
# okt_morph_X = okt.morphs(X[1], stem=True)
# print(X[1])
# print(okt_morph_X)

# okt_nouns_X = okt.nouns(X[2])
# print(X[2])
# print(okt_nouns_X)

#for i in range(len(X)):
#    X[i] = okt.morphs(X[i], stem=True)
#print(X)




stopwords = pd.read_csv('../../PRJ_Movie_for_you-1/crawling_data/stopwords.csv', index_col=0)
print(stopwords.head())

okt = Okt()
for i in range(len(X)):
    try:
        X[i] = okt.morphs(X[i], stem=True)
        words = []
        for word in X[i]:
            if len(word) > 1:
                if word not in list(stopwords['stopword']):
                    words.append(word)
    except KeyError:
        pass
    X[i] = ' '.join(words)
    print(X[i])

#for j in range(len(X)): #학습 시킨 모든 데이터
#    words = []
#    for i in range(len(X[j])):
#        if len(X[j][i]) > 1:
#            if X[j][i] not in list(stopwords['stopword']):
#                words.append(X[j][i])
#    X[j] = ' '.join(words)
#print(X)

token = Tokenizer()
token.fit_on_texts(X)
tokened_X = token.texts_to_sequences(X)
print(tokened_X[:5])

with open('./models/movie_genre_token_2000.pickle', 'wb') as f:
    pickle.dump(token, f)
print(token.index_word)

wordsize = len(token.word_index) + 1
print(wordsize)
print(token.index_word)

Max = 2000
for i in range(len(tokened_X)):
    if Max < len(tokened_X[i]):
        tokened_X[i] = tokened_X[i][:Max]

X_pad = pad_sequences(tokened_X, Max)
print(X_pad[:10])

X_train, X_test, Y_train, Y_test = train_test_split(X_pad, onehot_Y, test_size=0.1)
print(X_train.shape, Y_train.shape)
print(X_test.shape, Y_train.shape)

xy = X_train, X_test, Y_train, Y_test
np.save('./crawling/movie_genre_data_max_{}_wordsize_{}'.format(Max, wordsize), xy)