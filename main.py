#DSA2 Project
from graphFile import Graph
from hashTable import PackageHashTable
import csv
from value import Value
#from graph import Vertex







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

        #value = [pID, address, city, state, zip, deadline, weight, note]
        value = Value(pID, address, city, state, zip, deadline, weight, note)

        hash_table.insert(i, value)
        i +=1









N = 27
M = 27
#Matrix for edge distances
edgeMatrix = []


#Dictionary for edge distances and location
edgeDictionary = {}



with open("distance_file.csv") as df:

    csv_reader = csv.reader(df, delimiter=',')


    ####if value is null or value == none then next again
    ####the alternative would be at the end of the for loop add another next since you know that its uniform
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

#Truck 2 is arrival after 9
Truck2 = [36, 38, 18, 3, 6, 28, 32, 7, 8, 10, 11, 12, 17, 25, 21, 22]

#Truck 3 is wrong address and left overs
Truck3 = [9, 35, 23, 24, 26, 33, 27, 29]








g = Graph()
#g.deliverPackage(hash_table, edgeMatrix, edgeDictionary, Truck1)
#g.deliverPackage(hash_table, edgeMatrix, edgeDictionary, Truck2)
#g.deliverPackage(hash_table, edgeMatrix, edgeDictionary, Truck3)
Truck4 = [6, 25, 17, 32, 28, 39, 33, 26, 23]
#g.deliverPackage(hash_table, edgeMatrix, edgeDictionary, Truck4)
Truck5 = [13, 14, 15, 19, 16, 20, 29, 30, 31, 34, 37, 40, 1, 12, 22, 24]
#g.deliverPackage(hash_table, edgeMatrix, edgeDictionary, Truck5)
Truck6 = [5, 3, 18, 36, 38, 8, 2, 4, 27, 10, 11, 9, 7, 21, 35]
#g.deliverPackage(hash_table, edgeMatrix, edgeDictionary, Truck6)
Truck7 = [23, 15, 10]
g.deliverPackage(hash_table, edgeMatrix, edgeDictionary, Truck7)















