# Author: Jun Kim
# Description: In this program we will implement a HashMap class


# Import pre-written DynamicArray and LinkedList classes
from a5_include import *


def hash_function_1(key: str) -> int:
    """
    Sample Hash function #1 to be used with HashMap implementation
    """
    hash = 0
    for letter in key:
        hash += ord(letter)
    return hash


def hash_function_2(key: str) -> int:
    """
    Sample Hash function #2 to be used with HashMap implementation
    """
    hash, index = 0, 0
    index = 0
    for letter in key:
        hash += (index + 1) * ord(letter)
        index += 1
    return hash


class HashMap:
    def __init__(self, capacity: int, function) -> None:
        """
        Init new HashMap based on DA with SLL for collision resolution
        """
        self.buckets = DynamicArray()
        for _ in range(capacity):
            self.buckets.append(LinkedList())
        self.capacity = capacity
        self.hash_function = function
        self.size = 0

    def __str__(self) -> str:
        """
        Return content of hash map t in human-readable form
        """
        out = ''
        for i in range(self.buckets.length()):
            list = self.buckets.get_at_index(i)
            out += str(i) + ': ' + str(list) + '\n'
        return out

    def clear(self) -> None:
        """
        clears the content of the hash map
        """

                                                                                            # sets each index of hashmap to have an empty linked list value and size of 0
        for index in range(0, self.capacity):                                               # capacity is set during initialization
            self.buckets.set_at_index(index, (LinkedList()))
            self.size = 0



    def get(self, key: str) -> object:
        """
        returns the value associated with the given key
        """

        if self.contains_key(key) == False:                                                 # if the hashmap doesn't have the key, then return None                           
            return None

        else:
            hash = self.hash_function(key)
            size = self.capacity
            index = hash % size                                                             # the hash function can vary

            return self.buckets.get_at_index(index).contains(key).value

        return None

    def put(self, key: str, value: object) -> None:
        """
        updates the key / value pair in the hash map
        """

        hash = self.hash_function(key)
        size = self.capacity

        index = hash % size

        linked = self.buckets.get_at_index(index)

        if linked.contains(key) != None: #if they share the same key, replace value
            linked.remove(key)
            linked.insert(key, value)

        else:
            linked.insert(key, value)
            self.size += 1

    def is_empty_linked(self, linked):

        if linked.length() > 0:
            return False

        return True

    def remove(self, key: str) -> None:
        """
        removes the given key and its associated value from the hash map
        """

        hash = self.hash_function(key)
        size = self.capacity

        index = hash % size

        linked = self.buckets.get_at_index(index)

        if linked.length() == 0:
            return None

        if linked.contains(key) != None:
            linked.remove(key)
            self.size -= 1

        return None

    def contains_key(self, key: str) -> bool:
        """
        returns True if the given key is in the hash map, otherwise it returns False
        """
        hash = self.hash_function(key)
        size = self.capacity
        index = hash % size

        pointer = self.buckets.get_at_index(index)

        if pointer.contains(key):
            return True
        return False


    def empty_buckets(self) -> int:
        """
        returns a number of empty buckets in the hash table.
        """

        empty = 0
        size = self.capacity

        for index in range(0, size):
            if self.buckets.get_at_index(index).length() == 0:
                empty = empty + 1

        return empty


    def table_load(self) -> float:
        """
        returns the current hash table load factor.
        """

        load = self.size/self.capacity

        return load


    def resize_table(self, new_capacity: int) -> None:
        """
        changes the capacity of the internal hash table
        """

        if new_capacity < 1:
            return

        newtable = DynamicArray()
        OneLink = LinkedList() #put all the key/value pair into one linked list

        # create a new empty dynamic array
        for x in range(new_capacity):
            newtable.append(LinkedList())

        # get all the linked list in dynamic array, and get their nodes.
        for x in range(0, self.capacity):
            linked = self.buckets.get_at_index(x)
            if linked.length() == 0:
                continue
            else:
                for node in linked:
                    OneLink.insert(node.key, node.value)

        self.clear()
        self.capacity = new_capacity
        self.buckets = newtable

        for i in (OneLink):
            self.put(i.key, i.value)


    def get_keys(self) -> DynamicArray:
        """
        returns a DynamicArray that contains all keys stored in your hash map
        """

        keys = DynamicArray()

        for i in range(self.capacity):
            for node in self.buckets.get_at_index(i):
                keys.append(node.key)

        return keys


# BASIC TESTING
if __name__ == "__main__":

    print("\nPDF - empty_buckets example 1")
    print("-----------------------------")
    m = HashMap(100, hash_function_1)
    print(m.empty_buckets(), m.size, m.capacity)
    m.put('key1', 10)
    print(m.empty_buckets(), m.size, m.capacity)
    m.put('key2', 20)
    print(m.empty_buckets(), m.size, m.capacity)
    m.put('key1', 30)
    print(m.empty_buckets(), m.size, m.capacity)
    m.put('key4', 40)
    print(m.empty_buckets(), m.size, m.capacity)


    print("\nPDF - empty_buckets example 2")
    print("-----------------------------")
    m = HashMap(50, hash_function_1)
    for i in range(150):
        m.put('key' + str(i), i * 100)
        if i % 30 == 0:
            print(m.empty_buckets(), m.size, m.capacity)


    print("\nPDF - table_load example 1")
    print("--------------------------")
    m = HashMap(100, hash_function_1)
    print(m.table_load())
    m.put('key1', 10)
    print(m.table_load())
    m.put('key2', 20)
    print(m.table_load())
    m.put('key1', 30)
    print(m.table_load())


    print("\nPDF - table_load example 2")
    print("--------------------------")
    m = HashMap(50, hash_function_1)
    for i in range(50):
        m.put('key' + str(i), i * 100)
        if i % 10 == 0:
            print(m.table_load(), m.size, m.capacity)

    print("\nPDF - clear example 1")
    print("---------------------")
    m = HashMap(100, hash_function_1)
    print(m.size, m.capacity)
    m.put('key1', 10)
    m.put('key2', 20)
    m.put('key1', 30)
    print(m.size, m.capacity)
    m.clear()
    print(m.size, m.capacity)


    print("\nPDF - clear example 2")
    print("---------------------")
    m = HashMap(50, hash_function_1)
    print(m.size, m.capacity)
    m.put('key1', 10)
    print(m.size, m.capacity)
    m.put('key2', 20)
    print(m.size, m.capacity)
    m.resize_table(100)
    print(m.size, m.capacity)
    m.clear()
    print(m.size, m.capacity)


    print("\nPDF - put example 1")
    print("-------------------")
    m = HashMap(50, hash_function_1)
    for i in range(150):
        m.put('str' + str(i), i * 100)
        if i % 25 == 24:
            print(m.empty_buckets(), m.table_load(), m.size, m.capacity)


    print("\nPDF - put example 2")
    print("-------------------")
    m = HashMap(40, hash_function_2)
    for i in range(50):
        m.put('str' + str(i // 3), i * 100)
        if i % 10 == 9:
            print(m.empty_buckets(), m.table_load(), m.size, m.capacity)


    print("\nPDF - contains_key example 1")
    print("----------------------------")
    m = HashMap(10, hash_function_1)
    print(m.contains_key('key1'))
    m.put('key1', 10)
    m.put('key2', 20)
    m.put('key3', 30)
    print(m.contains_key('key1'))
    print(m.contains_key('key4'))
    print(m.contains_key('key2'))
    print(m.contains_key('key3'))
    m.remove('key3')
    print(m.contains_key('key3'))


    print("\nPDF - contains_key example 2")
    print("----------------------------")
    m = HashMap(75, hash_function_2)
    keys = [i for i in range(1, 1000, 20)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.size, m.capacity)
    result = True
    for key in keys:
        # all inserted keys must be present
        result &= m.contains_key(str(key))
        # NOT inserted keys must be absent
        result &= not m.contains_key(str(key + 1))
    print(result)


    print("\nPDF - get example 1")
    print("-------------------")
    m = HashMap(30, hash_function_1)
    print(m.get('key'))
    m.put('key1', 10)
    print(m.get('key1'))


    print("\nPDF - get example 2")
    print("-------------------")
    m = HashMap(150, hash_function_2)
    for i in range(200, 300, 7):
        m.put(str(i), i * 10)
    print(m.size, m.capacity)
    for i in range(200, 300, 21):
        print(i, m.get(str(i)), m.get(str(i)) == i * 10)
        print(i + 1, m.get(str(i + 1)), m.get(str(i + 1)) == (i + 1) * 10)


    print("\nPDF - remove example 1")
    print("----------------------")
    m = HashMap(50, hash_function_1)
    print(m.get('key1'))
    m.put('key1', 10)
    print(m.get('key1'))
    m.remove('key1')
    print(m.get('key1'))
    m.remove('key4')


    print("\nPDF - resize example 1")
    print("----------------------")
    m = HashMap(20, hash_function_1)
    m.put('key1', 10)
    print(m.size, m.capacity, m.get('key1'), m.contains_key('key1'))
    m.resize_table(30)
    print(m.size, m.capacity, m.get('key1'), m.contains_key('key1'))


    print("\nPDF - resize example 2")
    print("----------------------")
    m = HashMap(75, hash_function_2)
    keys = [i for i in range(1, 1000, 13)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.size, m.capacity)

    for capacity in range(111, 1000, 117):
        m.resize_table(capacity)

        m.put('some key', 'some value')
        result = m.contains_key('some key')
        m.remove('some key')

        for key in keys:
            result &= m.contains_key(str(key))
            result &= not m.contains_key(str(key + 1))
        print(capacity, result, m.size, m.capacity, round(m.table_load(), 2))


    print("\nPDF - get_keys example 1")
    print("------------------------")
    m = HashMap(10, hash_function_2)
    for i in range(100, 200, 10):
        m.put(str(i), str(i * 10))
    print(m.get_keys())

    m.resize_table(1)
    print(m.get_keys())

    m.put('200', '2000')
    m.remove('100')
    m.resize_table(2)
    print(m.get_keys())
