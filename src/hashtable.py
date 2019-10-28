# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * self.capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        slot = self._hash_mod(key)
        data = self.storage[slot]

        if data is None:
            self.storage[slot] = LinkedPair(key, value)
        else:
            while data and data.key != key:
                previous, data = data, data.next
            if data:
                data.value = value
            else:
                previous.next = LinkedPair(key, value)



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        slot = self._hash_mod(key)
        data = self.storage[slot]
        if not self.storage[slot]:
            raise KeyError
        else:
            if data.key == key:
                self.storage[slot] = None
            else:
                while data and data.key != key:
                    previous, data = data, data.next
                if data.value:
                    previous.next = data.next



    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        slot = self._hash_mod(key)
        data = self.storage[slot]
        if not self.storage[slot]:
            return None
        else:
            while data and data.key != key:
                previous, data = data, data.next
            if data:
                return data.value
            else:
                return None

    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        new_storage = [None] * (self.capacity * 2)
        
        for i in range(self.capacity):
            old_data = self.storage[i]
            if old_data != None:
                while old_data.next != None:
                    slot = self._hash(old_data.key) % (self.capacity * 2)
                    data = new_storage[slot]

                    if data is None:
                        new_storage[slot] = LinkedPair(old_data.key, old_data.value)
                    else:
                        while data and data.key != old_data.key:
                            previous, data = data, data.next
                        if data:
                            data.value = old_data.value
                        else:
                            previous.next = LinkedPair(old_data.key, old_data.value)
                        print(new_storage)
        self.storage = new_storage
        self.capacity = self.capacity *2





if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")
    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
