import pandas as pd 
import numpy as np
from pathlib import Path  
import warnings

warnings.filterwarnings('ignore')
filepath = Path('out.csv')
df1_cols=['user_id','movie_id',"rating",'time']
df2_cols=['movie_id',"title"]
df1=pd.read_csv("u.data",sep="\t",names=df1_cols,usecols=range(3))
df2=pd.read_csv("u.item",sep="|",names=df2_cols,encoding='latin-1',usecols=range(2))

final_dataset=pd.merge(df1,df2)


movieRatings=final_dataset.pivot_table(index=['user_id'],columns=['title'],values='rating')

starWarsRatings=movieRatings['Star Wars (1977)']

similarMovies=movieRatings.corrwith(starWarsRatings)

similarMovies.dropna()

x=similarMovies.sort_values(ascending=False)



movieStats=final_dataset.groupby('title').agg({'rating': [np.size,np.mean]})




popularMovies=movieStats['rating']['size']>=100

filters=movieStats[popularMovies].sort_values([('rating','mean')],ascending=False)[:15]

properDf=movieStats[popularMovies].join(pd.DataFrame(similarMovies,columns=['similarity']))
print(properDf.sort_values(['similarity'],ascending=False)[:20])