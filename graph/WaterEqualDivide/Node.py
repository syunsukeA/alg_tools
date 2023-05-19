import copy

class Node():
    def __init__(self, capacity, state, parent, cost, n_divide):
        self.capacity = capacity
        self.state = state
        self.parent = parent
        self.cost = cost
        self.n_divide = n_divide
        self.goal_amount = sum(state)//n_divide
    
    def get_neighbors(self):
        neighbor_node_list = []
        for i in range(len(self.state)):
            if self.state[i] == 0: # is empty
                continue
            for j in range(len(self.state)):
                if i == j: # same cup
                    continue
                next_state = copy.deepcopy(self.state)
                if self.state[i]+self.state[j]<=self.capacity[j]: # poru all amount of water to cup_j
                    # if next_state[j] == 0: # waste operation(XX04X -> XX40X)
                    #     continue
                    next_state[j] += next_state[i]
                    next_state[i] = 0
                else:
                    next_state[i] -= self.capacity[j]-next_state[j]
                    next_state[j] = self.capacity[j]
                # add a one of the next node to the list.    
                neighbor_node_list.append(Node(self.capacity, next_state, self, self.cost, self.n_divide)) # ToDo: How to send Instance itself.
                    
        return neighbor_node_list
    
    # get state as tuple
    def get_state(self):
        return tuple(self.state)
    
    def is_goal(self):
        cnt = 0
        for i in range(len(self.state)):
            if self.state[i] == self.goal_amount:
                cnt += 1
            elif self.state[i] != 0:
                return False
            
        if cnt == self.n_divide:
            return True 
        else:
            return False