#import dataset
from sklearn import datasets
iris = datasets.load_iris()

#features
X = iris.data
#labels
y = iris.target

#separate dataset into training set and testing set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.5)


#classifiers - decision tree and KNearestNeighbor

#decision tree classifier
from sklearn import tree
my_classifier_1 = tree.DecisionTreeClassifier()

#train decision tree classifier
my_classifier_1.fit(X_train, y_train)

#test the classifier using testing data to classify new data
predictions_1 = my_classifier_1.predict(X_test)
#output should be either 0, 1, 2 (depending on flower)
print(predictions_1)

#calculate the accuracy of the classifier by comparing the predicted labels with the actual labels
from sklearn.metrics import accuracy_score
#running the script three times consecutively produced accuracy of 93%, 96% and 97%
#due to randomness in shuffling the data points (not increased accuracy from repeat testing)
print('accuracy of decision tree classifier: ', accuracy_score(y_test,predictions_1))


#KNearestNeighbor
from sklearn.neighbors import KNeighborsClassifier
my_classifier_2 = KNeighborsClassifier()
#train KNearestNeighbor classifier
my_classifier_2.fit(X_train, y_train)
#test the classifier with testing data
predictions_2 = my_classifier_2.predict(X_test)
#output should be either 0, 1, 2 (depending on flower)
print(predictions_2)
#calculate the accuracy of the classifier by comparing the predicted labels with the actual labels
from sklearn.metrics import accuracy_score
#calculate accuracy
print('accuracy of KNearestNeighbor classifier: ', accuracy_score(y_test,predictions_2))
