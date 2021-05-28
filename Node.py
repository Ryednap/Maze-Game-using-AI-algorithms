class Node:
    
    def __init__(self, From, To, cost):
        self.From = From
        self.To = To
        self.cost = cost # Get Heuristic cost
        
    
    def __str__(self):
        return "from " + str(self.From) + " " + "to" + str(self.To) +\
            "Heuristic Value of the Node :" + str(self.cost)
    
    def __eq__(self, other):
        return (
            self.cost == other.cost
        )
    
    def __lt__ (self, other):
        return (
            self.cost < other.cost
        )








         

    