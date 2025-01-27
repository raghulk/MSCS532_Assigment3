class HashTableChaining:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash_function(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])

    def search(self, key):
        index = self._hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None

    def delete(self, key):
        index = self._hash_function(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                return True
        return False

    def display(self):
        for i, chain in enumerate(self.table):
            print(f"Bucket {i}: {chain}")

# Test cases
if __name__ == "__main__":
    ht = HashTableChaining(5)
    ht.insert("apple", 10)
    ht.insert("banana", 20)
    ht.insert("grape", 30)
    ht.display()
    print("Search 'apple':", ht.search("apple"))
    print("Search 'cherry':", ht.search("cherry"))
    ht.delete("banana")
    ht.display()
