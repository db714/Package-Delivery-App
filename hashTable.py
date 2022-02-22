#from graphFile import Graph
class PackageHashTable:

#Constructor
#Initializing the size of the table
    def __init__(self, size):
        self.size = size
        self.table = []
        for i in range(size):
            self.table.append([])

#Inserting/updating entries into HashTable
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

#Searching for entries in HashTable
    def search(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        for kv in bucket_list:
            if kv[0] == key:

                return kv[1]
            break

        else:
            return print("Package not found")