from collections import deque

class Searcher():
    def __init__(self):
        pass
    
    def search(self):
        pass

class BFS(Searcher):
    def search(self, start_node):
        q = deque([start_node])
        has_made = {tuple(start_node.get_state())}
        while q:
            curr_node = q.popleft()
            if curr_node.is_goal():
                return curr_node
            for neighbor_node in curr_node.get_neighbors():
                if not(neighbor_node.get_state() in has_made):
                    has_made.add(neighbor_node.get_state())
                    q.append(neighbor_node)
        return None