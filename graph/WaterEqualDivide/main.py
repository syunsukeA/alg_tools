from Solver import Solver
from Searcher import BFS
import sys

if __name__ == '__main__':
    args = sys.argv
    # Part of input
    if len(args) > 1: # get data from file
        with open(f"input/{args[1]}", "r") as f:
            N = int(f.readline())
            C = list(map(int, f.readline().split()))
            W = list(map(int, f.readline().split()))  
            D = int(f.readline())
        
    else: # ged data from stdIO
        print(f'Input number of cups.')
        N = int(input())
        print(f'Input capacity of each cups.')
        C = list(map(int, input().split()))
        print(f'Input amount of water of each cups.')
        W = list(map(int, input().split()))  
        print(f'Input equal devide number.')
        D = int(input())
        
    # Illegal input judge
    if (D > N) or (sum(W)%D != 0) or not(len(C)==N and len(W)==N):
        print('Illegal input!')
        exit()
    
    solver = Solver(N, C, W, D)
    
    # select Searcher.
    searcher = BFS()
    
    solver.solve(searcher)