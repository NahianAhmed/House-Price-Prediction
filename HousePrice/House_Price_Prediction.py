
from matplotlib import pyplot
import csv
from sklearn import linear_model
reg=linear_model.LinearRegression()
house_size=[]
Price_sft=[]

print(" Enter Your House Information : what is the size of your house ? ")
X=float(input())

print("How Many Bed Room Do you has ?")
N=int(input())

if N is 3:
    with open("house_02.csv") as csvfile:
        read=csv.DictReader(csvfile)
        for row in read:
           house_size.append([float(row['3_Room'])])
           Price_sft.append(float(row['Tsft(3)']))
    reg.fit(house_size,Price_sft)
    m=reg.coef_[0]
    b=reg.intercept_

    print("slope=",m, "intercept=",b)

    ans=reg.predict(X)
    print(ans)
    print("Predicted Price : " +str(ans*X))

    pyplot.plot(house_size,Price_sft,'ro')
    pyplot.plot(X,ans,'bs')
    pyplot.title("house sell")
    pyplot.xlabel("X axis")
    pyplot.ylabel("Y axis")
    pyplot.show()

if N is 2:
    with open("house_02.csv") as csvfile:
        read=csv.DictReader(csvfile)
        for row in read:
           house_size.append([float(row['2_Room'])])
           Price_sft.append(float(row['Tsft(2)']))
    reg.fit(house_size,Price_sft)
    m=reg.coef_[0]
    b=reg.intercept_

    print("slope=",m, "intercept=",b)

    ans=reg.predict(X)
    print(ans)
    print("Predicted Price : " +str(ans*X))

    pyplot.plot(house_size,Price_sft,'ro')
    pyplot.plot(X,ans,'bs')
    pyplot.title("house sell")
    pyplot.xlabel("X axis")
    pyplot.ylabel("Y axis")
    pyplot.show()

if N is 4:
    with open("house_02.csv") as csvfile:
        read=csv.DictReader(csvfile)
        for row in read:
           house_size.append([float(row['4_Room'])])
           Price_sft.append(float(row['Tsft(4)']))
    reg.fit(house_size,Price_sft)
    m=reg.coef_[0]
    b=reg.intercept_

    print("slope=",m, "intercept=",b)

    ans=reg.predict(X)
    print(ans)
    print("Predicted Price : " +str(ans*X))

    pyplot.plot(house_size,Price_sft,'ro')
    pyplot.plot(X,ans,'bs')
    pyplot.title("Data of house sell")
    pyplot.xlabel("X axis")
    pyplot.ylabel("Y axis")
    pyplot.show()

else:
    print("Please Enter No. of room 2 to 4. Thank You! ")
