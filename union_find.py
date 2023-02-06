class UnionFind():
    def __init__(self, n):
        self.clustetr = n
        self.parent = [i for i in range(n+1)]
        self.rank = [1]*(n+1)
    
    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return True
        else:
            if self.rank[x] < self.rank[y]:
                self.parent[x] = y
                self.rank[y] += self.rank[x]
                self.rank[x] = 0
            else:
                self.parent[y] = x
                self.rank[x] += self.rank[y]
                self.rank[y] = 0
            return False
    
    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

if __name__ == '__main__':
    pass


if __name__ == '__main__':
    n = 8
    uf = UnionFind(n)
    
    uf.union(0, 1)
    uf.union(1, 3)
    uf.union(0, 4)
    uf.union(5, 6)
    uf.union(3, 7)

    print(uf.find(3))  # 0
    print(uf.clustetr)