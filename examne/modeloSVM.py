import sys
import os
import time
from sklearn.metrics import confusion_matrix
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm
from sklearn.metrics import classification_report

# Read the data
test_data = ['a el le dijeron ineficaz malo y corrupto', 
	'el es eficaz y colaborador pero a veces es mentiroso']
test_labels = ['bueno', 'malo']

# test_data = ['el es eficaz y colaborador pero a veces es mentiroso']
# test_labels = ['bueno']

train_data = ['es un amigo bueno y colaborador', 
	'es un amigo malo mentiroso y corrupto', 
	'el es  colaborador con todos']
train_labels = ['bueno', 
	'malo', 
	'bueno']


train_vectors = []
test_vectors = []


# Create feature vectors
vectorizer = TfidfVectorizer(
	min_df=1, 
	max_df = 0.6, 
	sublinear_tf=True, 
	use_idf=True, 
	decode_error='ignore', 
	lowercase=True,
	smooth_idf=True)


train_vectors = vectorizer.fit_transform(train_data)
test_vectors = vectorizer.transform(test_data)

# print('MAtriz de confusión')
# print(train_vectors)
# print()
# print(test_vectors)


# Perform classification with SVM, kernel=rbf


# Perform classification with SVM, kernel=linear
classifier_liblinear = svm.LinearSVC()
t0 = time.time()
classifier_liblinear.fit(train_vectors, train_labels)
t1 = time.time()
prediction_liblinear = classifier_liblinear.predict(test_vectors)
t2 = time.time()
time_liblinear_train = t1-t0
time_liblinear_predict = t2-t1



print("Results for LinearSVC()")
print("Training time: %fs; Prediction time: %fs" % (time_liblinear_train, time_liblinear_predict))
print(classification_report(test_labels, prediction_liblinear))
print('Matriz de confusión:')
print(confusion_matrix(test_data, prediction_liblinear))