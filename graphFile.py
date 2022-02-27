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

#takes in the hash table, a matrix with my distances, a dictionary full of keys by address, and the truck with packages
    def deliverPackage(self, hashTable=[], edgeMatrix=[], edgeDictionary={}, truck=[]):
        self.hashTable = hashTable
        self.truck = truck
        self.edgeMatrix = edgeMatrix
        self.edgeDictionary = edgeDictionary

        start = '4001 South 700 East'
        minDistance = 20.0
        mileCounter = 0.0
        rowList = list(edgeDictionary.keys())
        row = 0
        visitedLoc = []
        prevMinDist = 0.0


        while len(truck) != 0:
            for i in edgeMatrix[row]:

                if (float(i) == prevMinDist or edgeMatrix[row].index(i) in visitedLoc):
                    continue

                if (float(i) < minDistance and float(i) != 0.0):
                    minDistance = float(i)
                    j = edgeMatrix[row].index(i)
                    print(minDistance)



            #print("row after min loop", row)
            #print("mindistance", minDistance)


            for k in truck:

                print(minDistance)
                if hashTable.search(k).address == rowList[row]:

                    #print("made truck loop")
                    print("package ", k, " delivered!")


                    truck.remove(k)



            if len(truck) == 0:
                    break



            print(mileCounter)
            mileCounter += minDistance
            print(mileCounter)
            visitedLoc.append(row)
            row = j
            prevMinDist = minDistance
            minDistance = 20.0






        return print("Packages delivered in ", mileCounter, " miles")































