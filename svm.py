import sklearn
from sklearn import svm
from sklearn import metrics
#https://stackoverflow.com/questions/13942744/prepare-data-for-text-classification-using-scikit-learn-svm
#https://www.quantstart.com/articles/Supervised-Learning-for-Document-Classification-with-Scikit-Learn
modelo = svm.SVC(
	C = 1.0, 
	kernel = 'rbf', 
	degree = 3, 
	gamma='auto', 
	coef0 = 0.0, 
	shrinking = True, 
	probability = False,
	tol = 0.001, 
	cache_size = 200, 
	class_weight = None, 
	verbose = False, 
	max_iter = -1, 
	random_state = None
)

# X = [[0, 1], [2, 3]]
# y = [0, 2]
#base de datos
X = [[1,6], [7,15], [20.23, 25.25]]
#etiquetas
y = [0,1,7]

modelo.fit(X, y)

prediccion = modelo.predict([[-3.5 , 1.25]])

print(modelo.score(X, y))
print(prediccion)


