# -*- coding: utf-8 -*-
"""classification-bank-nb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1VNlzZSuLLVBBBzNHcuPn9VM7q2I1OI7d
"""

import pandas as pd
import string
import numpy as np
import nltk

from sklearn.naive_bayes import MultinomialNB
from sklearn import model_selection
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.model_selection import train_test_split
from sklearn.utils.multiclass import unique_labels
from sklearn.preprocessing import LabelBinarizer, OrdinalEncoder, OneHotEncoder

from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

bank = '/content/drive/MyDrive/bankfull01.csv'
text = pd.read_csv(bank, header=0, delimiter=';')
df = pd.DataFrame(text)
print(df)

#menentukan parameter input
#drop utk memotong kolom yg tdk diperlukan
xtarget = df.drop(['id','y'], axis=1)
print(xtarget)

#menentukan target
ytarget = df['y']
print(ytarget)

#merubah/encode nilai ytarget menjadi 2 kelas yaitu 1 atau 0
encoder = LabelBinarizer()
y = encoder.fit_transform(ytarget)
print(y)

#merubah/encode nilai atribut menjadi index nilai
tfidf_transformer = OneHotEncoder()
x = tfidf_transformer.fit_transform(xtarget)
print(x)
print(x.shape)

#membuat data training dan data testing dari dataset dengan dataset testing 30%
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=1)
print(x_train.shape)
print(y_train.shape)
print(x_test.shape)
print(y_test.shape)

#melakukan model training dengan naive bayes
#ravel utk merubah posisi matrix
nb = MultinomialNB().fit(x_train, np.ravel(y_train, order='C'))
print(nb)

#prediksi thdp model training yg tlh dibuat
prediction = nb.predict(x_test)
accuracy = accuracy_score(y_test, prediction)

print(prediction)
print(accuracy)

#confmat
print(confusion_matrix(y_test, prediction))

