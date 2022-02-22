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


#create new vertex objects for each location
# vertex_a = Vertex("4001 South 700 East") #HUB
# vertex_b = Vertex("1060 Dalton Ave S")
# vertex_c = Vertex("1330 2100 S")
# vertex_d = Vertex("1488 4800 S")
# vertex_e = Vertex("177 W Price Ave")
# vertex_f = Vertex("195 W Oakland Ave")
# vertex_g = Vertex("2010 W 500 S")
# vertex_h = Vertex("2300 Parkway Blvd")
# vertex_i = Vertex("233 Canyon Rd")
# vertex_j = Vertex("2530 S 500 E")
# vertex_k = Vertex("2600 Taylorsville Blvd")
# vertex_l = Vertex("2835 Main St")
# vertex_m = Vertex("300 State St")
# vertex_n = Vertex("3060 Lester St")
# vertex_o = Vertex("3148 S 1100 W")
# vertex_p = Vertex("3365 S 900 W")
# vertex_q = Vertex("3575 W Valley Central Station bus Loop")
# vertex_r = Vertex("3595 Main St")
# vertex_s = Vertex("380 W 2880 S")
# vertex_t = Vertex("410 S State St")
# vertex_u = Vertex("4300 S 1300 E")
# vertex_v = Vertex("4580 S 2300 E")
# vertex_w = Vertex("5025 State St")
# vertex_x = Vertex("5100 South 2700 West")
# vertex_y = Vertex("5383 S 900 East #104")
# vertex_z = Vertex("600 E 900 South")
# vertex_zz = Vertex("6351 South 900 East")



#adding all vertex objects to graph
# g.addVertex(vertex_a)
# g.addVertex(vertex_b)
# g.addVertex(vertex_c)
# g.addVertex(vertex_d)
# g.addVertex(vertex_e)
# g.addVertex(vertex_f)
# g.addVertex(vertex_g)
# g.addVertex(vertex_h)
# g.addVertex(vertex_i)
# g.addVertex(vertex_j)
# g.addVertex(vertex_k)
# g.addVertex(vertex_l)
# g.addVertex(vertex_m)
# g.addVertex(vertex_n)
# g.addVertex(vertex_o)
# g.addVertex(vertex_p)
# g.addVertex(vertex_q)
# g.addVertex(vertex_r)
# g.addVertex(vertex_s)
# g.addVertex(vertex_t)
# g.addVertex(vertex_u)
# g.addVertex(vertex_v)
# g.addVertex(vertex_w)
# g.addVertex(vertex_x)
# g.addVertex(vertex_y)
# g.addVertex(vertex_z)
# g.addVertex(vertex_zz)


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
    next(csv_reader, None)
    next(csv_reader, None)
    next(csv_reader, None)

    i = 0
    j = 3
    for row in csv_reader:
        edgeMatrix.append(row[2:29])
        text = row[1]
        text = text[1:-8]
        edgeDictionary[text] = edgeMatrix[i]
        i +=1
        j +=1


# edgeDictionary['4001 South 700 East'] = edgeDictionary['']
# del edgeDictionary['']
#print(value)
#print(edgeDictionary)
#row x column
#print(edgeMatrix[3][1])
#valueList = edgeDictionary.get(' 1330 2100 S')
#print(valueList.index('7.1'))
#index where number is found will be the new row
#turn the keys into a list to line up the row and find the address(key)
#rowList = list(edgeDictionary.keys())
#print(rowList[1])


# for i, value in enumerate(edgeDictionary):
#         if edgeMatrix[i] == value:
#           print(i)

# print("try this")
# print(hash_table.search(16).address)
# print(hash_table.search(19).address)



#g.addWeight(vertex_b, vertex_a, float(7.2))


#Creating/Loading each truck
#Truck 1 is early morning
Truck1 = [15, 14, 19, 16, 13, 20, 1, 29, 30, 31, 34, 37, 40, 2, 4, 5]

#Truck 2 is arrival after 9
Truck2 = [36, 38, 18, 3, 6, 25, 28, 32, 7, 8, 10, 11, 12, 17, 21, 22]

#Truck 3 is wrong address and left overs
Truck3 = [9, 23, 24, 26, 27, 33, 35, 29]





# for i in range(1,41):
#     print(hash_table.search(i))
#
# print(vertex_a)
#
# print(g.adjacencyList)
# print(g.weightList)



# if 'vertex_a' in g.adjacencyList:
#     print('TRUE')
g = Graph()
g.deliverPackage(hash_table, edgeMatrix, edgeDictionary, Truck1)












#hash_table.insert(1, p1)

