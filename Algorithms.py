
from Setting import *
from helper import Manhattan, Euclidean, Path
from pygame import Vector2 as vec
from collections import deque as queue

class PriorityQueue:
    def __init__ (self, dummy):
        self.container = []
        self.container.append(dummy)

    def Swap(self, a, b):
        ob = self.container[a]
        self.container[a] = self.container[b]
        self.container[b] = ob

    def Heapify(self, i):
        left = 1 << i
        right = 1 << i + 1
        largest = i
        if( left < len(self.container) and
            self.container[left] < self.container[largest]
        ):
            largest = left
        
        if(right < len(self.container) and
            self.container[right] < self.container[largest]    
        ):
            largest = right
        
        if(largest != i):
            self.Swap(i, largest)
            self.Heapify(largest)
            
    
    def isEmpty(self):
        return len(self.container) == 1
    
    def push(self, el):
        self.container.append(el)
        self.Swap(1, len(self.container) - 1)
        self.Heapify(1)
    
    def pop(self):
        Max = self.container[1]
        self.Swap(1, len(self.container) - 1)
        self.container.pop()
        self.Heapify(1)
        return Max
    
    def front(self):
        return self.container[0]

    def __str__ (self):
        return ' '.join(self.container)


class Pair:
    def __init__(self, f, s):
        self.f = f
        self.s = s
        self.x = f
        self.y = s

    def update(self):
        self.x = self.f
        self.y = self.s

    def __add__(self, other):
        return Pair(self.f  + other.f, self.s + other.s)
    
    def __sub__ (self, other):
        return Pair(self.f - other.f, self.s - other.s)
    def __mul__ (self, x):
        return Pair(self.f * x, self.s * x)
    
    def __truediv__ (self, x):
        return Pair(self.f / x, self.s / x)

    def __isadd__(self,other):
        self.f += other.f
        self.s += other.s
        self.update()
        return self

    def __issub__(self, other):
        self.f -= other.f
        self.s -= other.s
        self.update()
        return self

    def swap(self):
        temp = self.f
        self.f = self.s
        self.s = temp
        self.update()

    def __eq__ (self, other):

        return (
            self.f == other.x and 
            self.s == other.y
        )
    
    def __lt__ (self, other):
        if(self.s == other.s):
            return self.s < other.s
        return self.s < other.s
    
    def __ge__ (self, other):
        if(self.f == other.f):
            return self.s >= other.s
        return self.f >= other.f
         

    def __str__ (self):
        return "(" + str(self.f) + "," + str(self.s) + ")"

class Astar:
    def __init__(self, grid, start, target):
        self.grid = grid
        self.start = self.xySwap(start)
        self.target = self.xySwap(target)

    def xySwap(self, p):
        return Pair(p.y, p.x)

    def Valid(self, x, y):
        if(x < 0 or y < 0):
            return False
        if(x >= len(self.grid) or y >= len(self.grid[0])):
            return False
        if(self.grid[x][y] == '1' or self.grid[x][y] == '2'):
            return True
        return False
    
    def Heuristic(self, x, y):
         return Euclidean(x, y, self.target.x, self.target.y)
        #return Manhattan(x, y, self.target.x, self.target.y)

    def optimalPath(self):
        pq = PriorityQueue(Pair(Pair(0, 0), 0))

        currentBest = [ [OO for _ in range(len(self.grid[i]))] for i in range(len(self.grid)) ]
        parent = [ [Pair(-1, -1) for _ in range(len(self.grid[i]))] for i in range(len(self.grid))]

        pq.push(Pair(self.start, 0))
        currentBest[self.start.x][self.start.y] = 0

        answer = -1
        while(pq.isEmpty() == False):
            node = pq.pop()
            print(node)
            if(node.f == self.target):
                answer = node.s
                break
            
            for i in range(4):
                RR = node.f.x + dx[i]
                CC = node.f.y + dy[i]
         
                if(self.Valid(RR, CC)):
                    cost = node.s + 1
                    if(currentBest[RR][CC] > cost + self.Heuristic(RR, CC)):
                        currentBest[RR][CC] = cost + self.Heuristic(RR, CC)
                        parent[RR][CC] = node.f
                        pq.push(Pair(Pair(RR, CC), cost))
           

        assert(answer != -1) # I mean answer should exist else we are screwed 
        print(
            "START: ", self.start,
            "TARGET: ", self.target,
            "DISTANCE: ", answer
        )
        path = Path([], currentBest)
        curr = self.target
        while (curr != Pair(-1, -1)):
            path.append(curr)
            curr = parent[curr.x][curr.y]

        path.pop()
        path.xySwap()
       # print(path)
        return path 
        
class BFS:
    def __init__(self, grid, start, target):
        self.grid = grid
        self.start = self.xySwap(start)
        self.target = self.xySwap(target)

    def xySwap(self, p):
        return Pair(p.y, p.x)

    def Valid(self, x, y):
        if(x < 0 or y < 0):
            return False
        if(x >= len(self.grid) or y >= len(self.grid[0])):
            return False
        if(self.grid[x][y] == '1' or self.grid[x][y] == '2'):
            return True
        return False
    

    def optimalPath(self):

        parent = [ [Pair(-1, -1) for _ in range(len(self.grid[i]))] for i in range(len(self.grid))]
        used = [[False for _ in range(len(self.grid[i]))] for i in range(len(self.grid))]

        Q = queue()
        Q.append(Pair(self.start, 0))
        answer = -1

        while (len(Q) != 0):
            node = Q.popleft()
            used[node.f.x][node.f.y] = True
            if(node.f == self.target):
                answer = node.s
                break
            
            for i in range(4):
                RR = node.f.x + dx[i]
                CC = node.f.y + dy[i]
                if(self.Valid(RR, CC) and used[RR][CC] == False):
                    Q.append(Pair(Pair(RR, CC), node.s + 1))
                    parent[RR][CC] = node.f

        assert(answer != -1) # I mean answer should exist else we are screwed 
        print(
            "START: ", self.start,
            "TARGET: ", self.target,
            "DISTANCE: ", answer
        )

        path = Path([], answer)
        curr = self.target
        while (curr != Pair(-1, -1)):
            path.append(curr)
            curr = parent[curr.x][curr.y]

        path.pop()
        path.xySwap()
       # print(path)
        return path 
        

    
class UCS:
    def __init__(self, grid, start, target):
        self.grid = grid
        self.start = start
        self.target = target

class greedyBFS:
    def __init__(self, grid, start, target):
        self.grid = grid
        self.start = start
        self.target = target

class MiniMax:
    def __init__(self, grid, start, target):
        self.grid = grid
        self.start = start
        self.target = target
    


""" 
    Test class to test the algorithm locally before
    deploying it on the game grid
    You can easily visualize the result and compare the result
    from each algorithm
"""

class Test:
    def __init__(self):
        pass

    def test(self):
        grid = [    [ 1, 0, 1, 1, 1, 1, 0, 1, 1, 1 ],
                    [ 1, 1, 1, 0, 1, 1, 1, 0, 1, 1 ],
                    [ 1, 1, 1, 0, 1, 1, 0, 1, 0, 1 ],
                    [ 0, 0, 1, 0, 1, 0, 0, 0, 0, 1 ],
                    [ 1, 1, 1, 0, 1, 1, 1, 0, 1, 0 ],
                    [ 1, 0, 1, 1, 1, 1, 0, 1, 0, 0 ],
                    [ 1, 0, 0, 0, 0, 1, 0, 0, 0, 1 ],
                    [ 1, 0, 1, 1, 1, 1, 0, 1, 1, 1 ],
                    [ 1, 1, 1, 0, 0, 0, 1, 0, 0, 1 ] ]


        src = Pair(0, 8)
        dest = Pair(0, 0)

        astar = BFS(grid, src, dest)
        path = astar.optimalPath()
        print(path)
       

