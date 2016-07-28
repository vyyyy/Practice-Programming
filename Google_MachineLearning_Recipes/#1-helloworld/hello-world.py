from sklearn import tree 

#features are the input to the classifier
#two features are included - weight (grams) and texture (smooth: 1 or bumpy: 0)
features = [[140,0],[130,0],[150,1],[170,1]]

#labels are the output to the classifier
#apple: 0 or orange: 1
labels = [0,0,1,1]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features,labels)

print(clf.predict([[160,0]]))
