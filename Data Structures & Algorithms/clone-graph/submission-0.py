"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        #create a hashmap that will map the nodes in the old graph to the cloned ones in the new graph
        if node is None:
            return None
        
        oldToNew = {}

        #define a depth first search algorith that will run recursively, cloning and connecting the different nodes
        def dfs(node): #takes the node as a argument/parameter
            if node in oldToNew: #if the node is already cloned
                return oldToNew[node] #just return the node (im guessing this connects the nodes aswell? creating a edge)

            copy = Node(node.val) #create the copy
            oldToNew[node] = copy #map the old node to the copy

            for neighbor in node.neighbors: #iterates through all the neighbors of the current original node
                copy.neighbors.append(dfs(neighbor)) #dfs(neighbor) recursively clones the neighbor node #copy.neighbors creates the edges/connections in the cloned graph
            return copy #return the fully cloned node with all its neighbors properly connected
        
        if dfs(node):
            return dfs(node)
        else: 
            return None