from Node import Node

class Solver():
    def __init__(self, N, C, W, D):
        self.N = N
        self.C = C
        self.D = D
        self.start_node = Node(capacity=C, state=W, parent=None, cost=0, n_divide=D)
    
    def solve(self, searcher):
        goal_node = searcher.search(self.start_node)
        if goal_node:
            path = []
            while goal_node:
                path.append(goal_node.state)
                goal_node = goal_node.parent
            print("----------------------------------------------")
            print(f"Best solution need {len(path)-1} times operation.")
            print("----------------------------------------------")
            print("")
            for i in range(1, len(path)+1):
                print(f"{i-1}th: {path[-i]}")
        else:
            print('Solution is not exist.')
            