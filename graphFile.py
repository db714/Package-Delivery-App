from hashTable import PackageHashTable
#from main import hash_table


# class Vertex:
#     def __init__(self, address):
#         self.address = address
#
#     def __str__(self):
#         return "%s" % self.address




class Graph:
    def __init__(self):
        print("made it")
    # def addVertex(self, new_vertex):
#     self.adjacencyList[new_vertex] =[]
# def addWeight(self, vertex1, vertex2, weight):
#     self.weightList[(vertex1, vertex2)] = weight
#     return

    def deliverPackage(self, hashTable=[], edgeMatrix=[], edgeDictionary={}, truck=[]):
        self.hashTable = hashTable
        self.truck = truck
        self.edgeMatrix = edgeMatrix
        self.edgeDictionary = edgeDictionary

        start = '4001 South 700 East'
        minDistance = 20.0
        mileCounter = 0
        rowList = list(edgeDictionary.keys())



        while len(truck) != 0:
            #shows all the edges for that key
            valueList = edgeDictionary.get(start)
            #converts all the edges to a float value
            valueList = list(map(float, valueList))
            #traverses through the edges
            
            for i in valueList:
                #if a new mindistance is found and its not 0 it sets new mindistance
                if i < minDistance and i != 0.0:
                 minDistance = i



            #traverses through each value in the truck list
            for i in truck:
                #if key(package id) address matches the start address then it removes the index
                if hashTable.search(i).address == start:
                    truck.remove(i)

                    print("removed package", i)

                    #break

            #print("truck for loop ended")

            #rowlist is list of all the keys
            #The new start is created with i #####keysList[value list index where minDistance value is at]

            start = rowList[valueList.index(minDistance)]

            minDistance = 20.0


        return print("function ended")








