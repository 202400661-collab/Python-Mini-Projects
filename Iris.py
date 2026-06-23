flower=input("Enter flower name:")
petal_length=float(input("Enter petal length(cm):"))
petal_width=float(input("Enter petal width(cm):"))
sepal_length=float(input("Enter sepal length(cm):"))
sepal_width=float(input("Enter sepal width(cm):"))
if petal_width<2.5:
    iris_type="Iris Setesa"
elif petal_length<5.0 and petal_width<1.8:
    iris_type="Iris Versicolor"
else:
    iris_type="Iris virginica"
print("\n----Iris Flower classification:")
print("Flower Name:",flower)
print("Petal Length:",petal_length,"cm")
print("Petal width:",petal_width,"cm")
print("Sepal Length:",sepal_length,"cm")
print("Sepal Width:",sepal_width,"cm")
print("Predicted Type:",iris_type)
