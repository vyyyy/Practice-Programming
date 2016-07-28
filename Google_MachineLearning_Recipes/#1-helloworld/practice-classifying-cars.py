from sklearn import tree

#feature 1: horsepower and feature 2: no. of seats (2 seats:0 or more than 2 seats: 1)
features = [[300,2],[450,2],[200,8],[150,9]]
#sports-car: 0 or minivan: 1
labels = [0,0,1,1]

#classifier
clf = tree.DecisionTreeClassifier()
#trained classifier
clf = clf.fit(features,labels)

#provide a new set of features (horsepower and no. of seats) to classify a new car
feature1 = 400
feature2 = 2

#use trained classifier to predict
#0 if it's a sportscar
#1 if it's a minivan
print(clf.predict([[feature1,feature2]]))

#expected output: [0]

