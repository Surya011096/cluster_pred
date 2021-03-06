import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle

df = pd.read_excel('E:/kmeans/train.xlsx')
X = df[['Component 1','Component 2','Component 3','Component 4',
             'Component 5','Component 6', 'Component 7','Component 8','Component 9']]
from sklearn.cluster import KMeans
kmeans = KMeans( n_clusters = 4, init='k-means++')
kmeans.fit(X.iloc[:,:9])
pred_x = kmeans.predict(X.iloc[:,:9])
frame = pd.DataFrame(X.iloc[:,:9])
frame['cluster'] = pred_x
print(frame)
pickle.dump(kmeans, open('model.pkl','wb'))
model = pickle.load(open('model.pkl','rb'))
df1= pd.read_excel('E:/kmeans/test.xlsx')
X1=df1[['Component 1','Component 2','Component 3','Component 4',
             'Component 5','Component 6', 'Component 7','Component 8','Component 9']]
kmeans.fit(X1.iloc[:,:9])
pred_x1 = kmeans.predict(X1.iloc[:,:9])
frame1= pd.DataFrame(X1.iloc[:,:9])
frame1['cluster']=pred_x1
print(frame1.head(2))

resultData = frame1.head(10)


