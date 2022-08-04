"""
hash table by list
crud
"""


class HashTable:
    def __init__(self, bucket_size=10) -> None:
        # create
        self.data = [[] for _ in range(bucket_size)]

    def _hash(self, k):
        return hash(k) % len(self.data)

    def add(self, k, v):
        # add
        # tc : O(1)
        if self._exist(k):
            return v  # already indexed
        hashed = self._hash(k)
        self.data[hashed].append((k, v))  # for simplicity

    def _exist(self, k):
        # check the unique key
        # tc O(1) in general
        hashed = self._hash(k)
        for indexed_k, indexed_v in self.data[hashed]:
            if indexed_k == k:
                return True
        return False

    def remove(self, k):
        # delete
        hashed = self._hash(k)
        for indexed_k, indexed_v in self.data[hashed]:
            if indexed_k == k:
                self.data[hashed].remove((indexed_k, indexed_v))
                return indexed_v
        else:
            return None

    def search(self, k):
        # read
        # O(1) in general
        # O(N) worst case
        hashed = self._hash(k)
        if len(self.data[hashed]) == 0:
            print(f"Not Found {k} in hashtable")
        else:
            for indexed_k, indexed_v in self.data[hashed]:
                if indexed_k == k:
                    return indexed_v


# create
h = HashTable()
# add
h.add("p", 1)
print(h.data)
# read
print(h.search("p"))
# delete
h.remove("p")
print(h.data)
