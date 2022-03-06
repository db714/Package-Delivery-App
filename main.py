#DSA2 Project
#main.py
#David Brown (001313638)
from graphFile import Graph
from hashTable import PackageHashTable
import csv
from value import Value
from datetime import datetime, timedelta
#from graph import Vertex


deliveryTime = timedelta(hours=0, minutes=0)


hash_table = PackageHashTable(40)


#Read the package csv file and put items in hashmap
with open("package_file.csv") as pf:
    csv_reader = csv.reader(pf, delimiter=',')
    next(csv_reader, None)
    next(csv_reader, None)
    next(csv_reader, None)
    next(csv_reader, None)
    next(csv_reader, None)
    next(csv_reader, None)
    next(csv_reader, None)
    next(csv_reader, None)

    #value = []
    i = 1

    for row in csv_reader:
        #print(','.join(row))
        pID = int(row[0])
        address = row[1]
        city = row[2]
        state = row[3]
        zip = row[4]
        deadline = row[5]
        weight = row[6]
        note = row[7]
        departTime = None
        dStatus = "At the Hub"
        dTime = None


        value = Value(pID, address, city, state, zip, deadline, weight, note, departTime, dStatus, dTime)

        hash_table.insert(i, value)
        i +=1


print(type(departTime))
print(type(dTime))






N = 27
M = 27
#Matrix for edge distances
edgeMatrix = []


#Dictionary for edge distances and location
edgeDictionary = {}


#Read the distance csv file and store values in a matrix
with open("distance_file.csv") as df:

    csv_reader = csv.reader(df, delimiter=',')



    next(csv_reader, None)
    next(csv_reader, None)
    next(csv_reader, None)
    next(csv_reader, None)
    next(csv_reader, None)
    #next(csv_reader, None)
    #next(csv_reader, None)
    #next(csv_reader, None)

    i = 0
    j = 3
    for row in csv_reader:
        edgeMatrix.append(row[2:29])
        text = row[1]
        text = text[1:-8]
        edgeDictionary[text] = edgeMatrix[i]
        i +=1
        j +=1













#Creating/Loading each truck
#Truck 1 is early morning
Truck1 = [15, 14, 19, 16, 37, 13, 20, 1, 29, 30, 31, 34, 5, 40, 2, 4]
for i in Truck1:
    hash_table.search(i).departTime = timedelta(hours=8)

#Truck 2 is arrival after 9
Truck2 = [36, 38, 18, 3, 6, 28, 32, 7, 8, 10, 11, 12, 17, 25, 21, 22]
for i in Truck2:
    hash_table.search(i).departTime = timedelta(hours=9, minutes=5)

#Truck 3 is wrong address and left overs
Truck3 = [9, 35, 23, 24, 26, 33, 27, 39]
for i in Truck3:
    hash_table.search(i).departTime = timedelta(hours=10, minutes=20)





g = Graph()








# main - START
if __name__ == '__main__':
    print("C950 Package Delivery Application")

    #loops until user decides to exit
    isExit = True
    while (isExit):
        print("\nOptions:")
        print("1: Get Package Data")
        print("2: Deliver Truck 1")
        print("3: Deliver Truck 2")
        print("4: Deliver Truck 3")
        print("5: Delivery Status by Time")
        print("6: Exit Program")
        option = input("Choose an option (1,2,3,4,5 or 6): ")
        if option == "1":
            for i in range(1, 41):
                print(hash_table.search(i))
        elif option == "2":
            for i in Truck1:
                hash_table.search(i).dStatus = "En Route"
            deliveryTime = timedelta(hours=8, minutes=0)
            g.deliverPackage(deliveryTime, hash_table, edgeMatrix, edgeDictionary, Truck1)
        elif option == "3":
            for i in Truck2:
                hash_table.search(i).dStatus = "En Route"
            deliveryTime = timedelta(hours=9, minutes=5)
            g.deliverPackage(deliveryTime, hash_table, edgeMatrix, edgeDictionary, Truck2)
        elif option == "4":
            for i in Truck3:
                hash_table.search(i).dStatus = "En Route"
            deliveryTime = timedelta(hours=10, minutes=20)
            g.deliverPackage(deliveryTime, hash_table, edgeMatrix, edgeDictionary, Truck3)
        elif option == "5":
            time = input("Please input a time(X:XX): ")

            timeList = time.split(':')
            tH = int(timeList[0])
            tM = int(timeList[1])
            print(timeList)
            print(tH)
            print(tM)
            for i in range(1, 41):
                if hash_table.search(i).departTime < timedelta(hours=tH, minutes=tM) < hash_table.search(i).dTime:
                    hash_table.search(i).dStatus = "En Route"
                if timedelta(hours=tH, minutes=tM) < hash_table.search(i).departTime:
                    hash_table.search(i).dStatus = "At the Hub"
                print(hash_table.search(i))

        elif option == "6":
            isExit = False
            print("Goodbye")
        else:
            print("Wrong option, please try again!")











