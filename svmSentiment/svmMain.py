import sys
import os
import time
from sklearn.metrics import confusion_matrix
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import svm
from sklearn.metrics import classification_report

# Read the data
test_data = ['mi banco es pesimo', 'hermoso esta por venir me gusta', 'no me gusta el por venir']
test_labels = ['negativo', 'positivo', 'negativo']

train_data = ['En Ecuador es hermoso', 'No me gusta la delicuencia', 'Lo mejor esta por venir']
train_labels = ['positivo', 'negativo', 'positivo']


train_vectors = []
test_vectors = []


# Create feature vectors
vectorizer = TfidfVectorizer(
	min_df=1, 
	max_df = 0.8, 
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


# # Perform classification with SVM, kernel=rbf
# classifier_rbf = svm.SVC(
# 	C = 1.0, 
# 	kernel = 'rbf', 
# 	degree = 3, 
# 	gamma='auto', 
# 	coef0 = 0.0, 
# 	shrinking = True, 
# 	probability = False,
# 	tol = 0.001, 
# 	cache_size = 200, 
# 	class_weight = None, 
# 	verbose = False, 
# 	max_iter = -1, 
# 	random_state = None
# 	)
# t0 = time.time()
# classifier_rbf.fit(train_vectors, train_labels)
# t1 = time.time()
# prediction_rbf = classifier_rbf.predict(test_vectors)
# t2 = time.time()
# time_rbf_train = t1-t0
# time_rbf_predict = t2-t1


# Perform classification with SVM, kernel=linear
# classifier_linear = svm.SVC(kernel='linear', gamma='auto', C = 1.0)
# t0 = time.time()
# classifier_linear.fit(train_vectors, train_labels)
# t1 = time.time()
# prediction_linear = classifier_linear.predict(test_vectors)
# t2 = time.time()
# time_linear_train = t1-t0
# time_linear_predict = t2-t1

# Perform classification with SVM, kernel=linear
classifier_liblinear = svm.LinearSVC()
t0 = time.time()
classifier_liblinear.fit(train_vectors, train_labels)
t1 = time.time()
prediction_liblinear = classifier_liblinear.predict(test_vectors)
t2 = time.time()
time_liblinear_train = t1-t0
time_liblinear_predict = t2-t1


print()
# Print results in a nice table
# print("Results for SVC(kernel=rbf)")
# print("Training time: %fs; Prediction time: %fs" % (time_rbf_train, time_rbf_predict))
# print(classification_report(test_labels, prediction_rbf))
# print("Results for SVC(kernel=linear)")
# print("Training time: %fs; Prediction time: %fs" % (time_linear_train, time_linear_predict))
# print(classification_report(test_labels, prediction_linear))
print("Results for LinearSVC()")
print("Training time: %fs; Prediction time: %fs" % (time_liblinear_train, time_liblinear_predict))
print(classification_report(test_labels, prediction_liblinear))
print('Matriz de confusión:')
print(confusion_matrix(test_data, prediction_liblinear))