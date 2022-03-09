#DSA2 Project
#hashTable.py
#David Brown (001313638)
#from graphFile import Graph
class PackageHashTable:

#Constructor
#Initializing the size of the table
    def __init__(self, size):
        self.size = size
        self.table = []
        for i in range(size):
            self.table.append([])

#Inserting/updating entries into HashTable. Hashtable has a space complexity of O(n)
#As long as number of keys needed are known beforehand the scalabilty/adaptability of the hashtable can grow as much as
#needed.
    def insert(self, key, val):
        bucket = hash(key) % len(self.table)

        bucket_list = self.table[bucket]

        for kv in bucket_list:
            if kv[0] == key:
                kv[1] = val
                return True

        key_value = [key, val]
        bucket_list.append(key_value)
        return True

#Searching for entries in HashTable. Search function has time Big O time of O(1). Even as the table grows the efficiency
# of the runtime stays the same.
    def search(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for kv in bucket_list:
            if kv[0] == key:

                return kv[1]
            break

        else:
            return print("Package not found")