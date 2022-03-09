#DSA2 Project
#graphFile.py
#David Brown (001313638)
#Total runtime complexity is worst case O(n^2)

from hashTable import PackageHashTable
#from main import hash_table
from value import Value
from datetime import datetime, timedelta


class Graph:
    def __init__(self):
        print("made it")

#Takes in the hash table, a matrix with my distances, a dictionary full of keys by address, and the truck with packages.
#Scalability/Adaptability of this algorithm would allow this algorithm to work regardless of how many addresses, trucks,
# or packages you sent to it.  However, the more locations that require visiting, the less accurate an optimal route
# will be as the Nearest Neighbor only visits the next closest location vs. creating an optimal ENTIRE path.
#While the time complexity will remain the same, if there was stricter constraints on the total mileage of the trucks, then
# this algorithm would lose efficiency.
    def deliverPackage(self, deliveryTime, hashTable=[], edgeMatrix=[], edgeDictionary={}, truck=[]):
        self.hashTable = hashTable
        self.truck = truck
        self.edgeMatrix = edgeMatrix
        self.edgeDictionary = edgeDictionary
        self.deliveryTime = deliveryTime


        start = '4001 South 700 East'
        minDistance = 20.0
        mileCounter = 0.0
        rowList = list(edgeDictionary.keys())
        row = 0
        visitedLoc = []
        prevMinDist = 0.0
        currLocation = rowList[0]

#The algorithm uses the addresses of the packages in the truck and finds the minimum distance from the current location.
#Once it reaches the destination it removes the package from the truck, updates the milecounter, updates the delivery
#status of that package, and moves to the next location until the truck is empty. Has a runtime of O(n^2)
        while len(truck) != 0:
            for package in truck:
                i = rowList.index(currLocation)
                j = rowList.index(hashTable.search(package).address)

                if (float(edgeMatrix[i][j]) < minDistance and float(edgeMatrix[i][j]) != 0.0):
                    minDistance = float(edgeMatrix[i][j])
                    nxtLocation = rowList[j]


            currLocation = nxtLocation

            for package in truck:

                if currLocation == hashTable.search(package).address:

                    timeToDeliver = minDistance/.3
                    hashTable.search(package).dStatus = "Delivered "
                    hashTable.search(package).dTime = deliveryTime
                    truck.remove(package)

            deliveryTime += timedelta(minutes=timeToDeliver)


            mileCounter += minDistance
            minDistance = 20.0



        return print("Packages delivered in ", mileCounter, " miles")





































