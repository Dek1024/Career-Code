import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('white')
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import confusion_matrix,classification_report

yelp = pd.read_csv("yelp.csv")
yelp.head()
yelp.info()
yelp.describe()

yelp["text length"] = yelp["text"].apply(len)
g = sns.FacetGrid(yelp,col="stars")
g.map(plt.hist,'text length',bins = 50)
plt.show()
sns.boxplot(x = "stars",y = "text length",data = yelp,palette = "rainbow")
plt.show()
sns.countplot(x = "stars",data= yelp, palette="rainbow")
plt.show()
answer = yelp.groupby(["stars"]).mean(numeric_only=True)
heat = answer.corr()
sns.heatmap(data=heat,cmap = 'coolwarm',annot=True)
plt.show()
yelp_class = yelp[(yelp.stars == 1) | (yelp.stars == 5)]
X = yelp_class['text']
y = yelp_class['stars']
from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer()
X = cv.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3,random_state=101)
cv = CountVectorizer()
nb = MultinomialNB()
nb.fit(X_train,y_train)
nb.fit(X_train,y_train)
predictions = nb.predict(X_test)

print(confusion_matrix(y_test,predictions))
print("\n")
print(classification_report(y_test,predictions))