import pandas as pd
import glob

data_paths = glob.glob('./crawling/*')
print(data_paths)

romance1 = pd.read_csv('./crawling/movie_genre_romance_1-30.csv')
romance2 = pd.read_csv('./crawling/movie_genre_romance_31-60.csv')
romance3 = pd.read_csv('./crawling/movie_genre_romance_remain.csv')
romance4 = pd.read_csv('./crawling/movie_genre_romance_61-90_addition.csv')
romance5 = pd.read_csv('./crawling/movie_genre_romance_91-120_addition.csv')
romance6 = pd.read_csv('./crawling/movie_genre_romance_remain_addition.csv')

crime1 = pd.read_csv('./crawling/movie_genre_crime_1-30.csv')
crime2 = pd.read_csv('./crawling/movie_genre_crime_31-60.csv')
crime3 = pd.read_csv('./crawling/movie_genre_crime_remain.csv')
crime4 = pd.read_csv('./crawling/movie_genre_crime_61-90_addition.csv')
crime5 = pd.read_csv('./crawling/movie_genre_crime_91-120_addition.csv')
crime6 = pd.read_csv('./crawling/movie_genre_crime_121-150_addition.csv')
crime7 = pd.read_csv('./crawling/movie_genre_crime_remain_addition.csv')

docu1 = pd.read_csv('./crawling/movie_genre_documentary_1-30.csv')
docu2 = pd.read_csv('./crawling/movie_genre_documentary_31-60.csv')
docu3 = pd.read_csv('./crawling/movie_genre_documentary_61-90.csv')
docu4 = pd.read_csv('./crawling/movie_genre_documentary_61-90_addition.csv')
docu5 = pd.read_csv('./crawling/movie_genre_documentary_91-120_addition.csv')
docu6 = pd.read_csv('./crawling/movie_genre_documentary_121-150_addition.csv')



df = pd.concat([romance1, romance2, romance3, romance4, romance5, romance6], ignore_index=True)
df2 = pd.concat([crime1, crime2, crime3, crime4, crime5, crime6, crime7], ignore_index=True)
df3 = pd.concat([docu1, docu2, docu3, docu4, docu5, docu6], ignore_index=True)

df.to_csv('./crawling/movie_genre_romance.csv', index = False)
df2.to_csv('./crawling/movie_genre_crime.csv', index = False)
df3.to_csv('./crawling/movie_genre_documentary.csv', index = False)