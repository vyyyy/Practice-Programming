#code a KNearestNeighbor classifier from scratch

#re-use code from the basic pipeline
#instead of importing a classifier from a lib, write one from scratch

#import random
from scipy.spatial import distance

#euc method calculates the distance between a single test datapoint and a training datapoint
def euc(a,b):
    return distance.euclidean(a,b)
    

#create a class for the classifier
class ScrappyKNN():

    #the fit method is used to train the classifier
    def fit(self, X_train, y_train):
        #provide the training data X_train containing features
        self.X_train = X_train
        #provide the training data y_train containing the labels
        self.y_train = y_train

    #the predict method is used to test the classifier
    def predict(self, X_test):
        predictions_2 = []
        for row in X_test:
            #label = random.choice(self.y_train)
            label = self.closest(row)
            predictions_2.append(label)
        return predictions_2

    #loop over the training data and keep track of the closest datapoint ("the k nearest neighor")
    def closest(self, row):
        #the distane between the test datapoint and the training datapoint
        #the best distance is the closest distance between test point and training point
        best_dist = euc(row, self.X_train[0])
        best_index = 0
        for i in range(1, len(self.X_train)):
            dist = euc(row, self.X_train[i])
            if dist < best_dist:
                best_dist = dist
                best_index = i
        return self.y_train[best_index]

#dataset
from sklearn import datasets
iris = datasets.load_iris()

#features
X = iris.data
#labels
y = iris.target

#separate dataset into training data and testing data
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.5)

#KNearestNeighbor - custom classifier coded from scratch
my_classifier_2 = ScrappyKNN()

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

