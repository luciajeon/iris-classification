# CS-UY 1114
# Final project

import math
import turtle

def create_table(file_name):
    # creates a table using a given file
    # sig: str -> tuple(list(float), list(float), list(str))
    f=open(file_name,"r")
    length=[]
    width=[]
    label=[]
    for line in f:
        line=line.strip()
        if line!="":
            lstofline=line.split(",")
            length.append(float(lstofline[0]))
            width.append(float(lstofline[1]))
            label.append(lstofline[2])
    f.close()
    return (length, width, label) # returns a tuple


def print_range_max_min(data):
    # sig: tuple(list(float), list(float)) -> NoneType
    def max(lst):
        maxval=0 # set the initial value as 0
        for item in lst:
            if item>maxval:
                maxval=item # stores maximum value
        return maxval
    def min(lst):
        minval=float("INF") # set the initial value as float("INF")
        for item in lst:
            if item<minval:
                minval=item # stores minimum value
        return minval
    print("Feature 1 - min: "+str(min(data[0]))+" max: "+str(max(data[0]))+" range: "+str(max(data[0])-min(data[0])))
    print("Feature 2 - min: "+str(min(data[1]))+" max: "+str(max(data[1]))+" range: "+str(max(data[1])-min(data[1])))   

def find_mean(feature):
    # sig: list(float) -> float
    sum=0
    for item in feature:
        sum+=item
    return sum/len(feature)
        

def find_std_dev(feature, mean):
    # sig: list(float), float -> float
    squaresum=0
    for item in feature:
        squaresum+=(item-mean)**2 # adds each square sum ((item-mean)**2) to fulfill the formula
    return math.sqrt(squaresum/len(feature)) # divides the squaresum with the number of items

def normalize_data(data):
    # prints the mean and standard deviation
    # sig: tuple(list(float), list(float), list(str)) -> NoneType

    # stores mean and standard deviation before normalization for both feature 1 and 2
    formermean_1=find_mean(data[0])
    formerstd_1=find_std_dev(data[0], formermean_1)
    formermean_2=find_mean(data[1])
    formerstd_2=find_std_dev(data[1], formermean_2)

    for i in range(0,len(data[0])):
        data[0][i]=(data[0][i]-formermean_1)/formerstd_1 # normalizes the item and mutates the parameter(list)
    for j in range(0,len(data[1])):
        data[1][j]=(data[1][j]-formermean_2)/formerstd_2

    # prints out
    print("Feature 1- mean: "+str(formermean_1)+" std dev: "+str(formerstd_1))
    print("Feature 1 after normalization - mean: "+str(find_mean(data[0]))+" std dev: "+str(find_std_dev(data[0], find_mean(data[0]))))                           
    print("Feature 2- mean: "+str(formermean_2)+" std dev: "+str(formerstd_2))
    print("Feature 2 after normalization - mean: "+str(find_mean(data[1]))+" std dev: "+str(find_std_dev(data[1], find_mean(data[1]))))

def make_predictions(train_set, test_set):
    # check the 'nearest neighbor' by calling the fuction find_dist
    # return a prediction list
    # tuple(list(float), list(float), list(str)), tuple(list(float), list(float), list(str)) -> list(str)
    predictedlst=[]
    for i in range (len(test_set[0])):
        min_distance=float("INF") # set the initial value as float("INF")
        for j in range(len(train_set[0])):
            newdistance=find_dist(test_set[0][i], test_set[1][i], train_set[0][j], train_set[1][j]) # function call to find_dist
            if newdistance<min_distance:
                min_distance=newdistance # stores the distance from nearest neighbor
                typename=train_set[2][j] # stores the name of the type everytime they find nearest neighbor
        predictedlst.append(typename) # accumulates
    return predictedlst

def find_dist(x1, y1, x2, y2):
    # sig: float, float, float, float -> float
    return math.sqrt((x1-x2)**2+(y1-y2)**2)
        
def find_error(test_data, pred_lst):
    # compare the types in test_data with pred_lst
    # return error percentage
    # sig: tuple(list(float), list(float), list(str)) -> float
    errornum=0
    for i in range(0,len(pred_lst)):
        if test_data[2][i]!=pred_lst[i]:
            errornum+=1
    return ((errornum/len(pred_lst))*100)

# drawing a square using turtle
def square(size, color):
    turtle.begin_fill()
    turtle.down()
    turtle.color(color)
    for i in range (0,4):
        turtle.forward(size)
        turtle.right(90)
    turtle.up()
    turtle.end_fill()

def plot_data(train_data, test_data, pred_lst):
    # sig: tuple(list(float), list(float), list(str)), tuple(list(float), list(float), list(str)), list(str) -> NoneType
    
    # x-axis
    turtle.up()
    turtle.goto(-250,0)
    turtle.down()
    turtle.goto(250,0)
    turtle.goto(200,0)
    turtle.write("petal length")
    # y-axis
    turtle.up()
    turtle.goto(0,-250)
    turtle.down()
    turtle.goto(0,250)
    turtle.up()
    turtle.goto(2,240)
    turtle.write("petal width")

    # plot train_data
    for i in range(0,len(train_data[0])):
        turtle.up()
        if train_data[2][i]=="Iris-versicolor":
            turtle.goto(train_data[0][i]*125, train_data[1][i]*125)
            turtle.color("purple")
            turtle.dot(10)
        if train_data[2][i]=="Iris-setosa":
            turtle.goto(train_data[0][i]*125, train_data[1][i]*125)
            turtle.color("green")
            turtle.dot(10)
        if train_data[2][i]=="Iris-virginica":
            turtle.goto(train_data[0][i]*125, train_data[1][i]*125)
            turtle.color("orange")
            turtle.dot(10)
    # plot test_data    
    for i in range(0, len(test_data[0])):
        if test_data[2][i]==pred_lst[i]:
            if test_data[2][i]=="Iris-versicolor":
                turtle.goto(test_data[0][i]*125-5, test_data[1][i]*125+5)
                # +-5 is needed so that the x, y value can be at the middle of the square, not upperleft corner of the square
                square(10, "purple")
            if test_data[2][i]=="Iris-setosa":
                turtle.goto(test_data[0][i]*125-5, test_data[1][i]*125+5)
                square(10, "green")
            if test_data[2][i]=="Iris-virginica":
                turtle.goto(test_data[0][i]*125-5, test_data[1][i]*125+5)
                square(10, "orange")
        else:
            turtle.goto(test_data[0][i]*125-5, test_data[1][i]*125+5)
            square(10, "red") # plots incorrect predictions in red
    draw_key()

def draw_key():
    # legend for the plot indicating which group is shown by each color/shape combination. 
    # sig: () -> NoneType 
    turtle.up()
    letterheight=240
    turtle.goto(-240,letterheight)
    colornames=[("Iris-versicolor","purple"),("Iris-setosa","green"),("Iris-verginica","orange"),("Incorrectly","red")]
    for index in colornames[:3]:
        turtle.color(index[1])
        turtle.dot(10)
        turtle.color("black")
        letterheight-=5
        turtle.goto(-230, letterheight)
        turtle.write(index[0])
        letterheight-=12
        turtle.goto(-240,letterheight)
    for index in colornames:
        turtle.goto(-245,letterheight+5)
        turtle.color(index[1])
        square(10, index[1])
        turtle.color("black")
        letterheight-=5
        turtle.goto(-230, letterheight)
        turtle.write("predicted "+index[0])
        letterheight-=12


def main():
    # process the training set, analyze the test set, and display its conclusions.
    # sig: () -> NoneType
    
    turtle.hideturtle()
    turtle.speed(10) # set the turtle speed to fastest
    turtle.setup(500,500) # turtle canvas

    train_data = create_table("iris_train.csv")
    # print(train_data) #
    # print(len(train_data[0])) #
    print_range_max_min(train_data[:2])
    print()
    normalize_data(train_data)
    # print(train_data) #
    test_data = create_table("iris_test.csv")
    # print(test_data) #
    # print(len(test_data[0])) #
    print()
    normalize_data(test_data)
    pred_lst = make_predictions(train_data, test_data)
    # print(pred_lst) #
    # print(len(pred_lst)) #
    error = find_error(test_data, pred_lst)
    print()
    print("The error percentage is: ", error)
    plot_data(train_data, test_data, pred_lst)

main()
