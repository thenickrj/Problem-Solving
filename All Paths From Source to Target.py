'''
All Paths From Source to Target

Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, 
find all possible paths from node 0 to node n - 1, and return them in any order.

The graph is given as follows: graph[i] is a list of all nodes you can visit from node i 
(i.e., there is a directed edge from node i to node graph[i][j]).


Input: graph = [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]
Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
Example 2:


Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
Example 3:

Input: graph = [[1],[]]
Output: [[0,1]]
Example 4:

Input: graph = [[1,2,3],[2],[3],[]]
Output: [[0,1,2,3],[0,2,3],[0,3]]
Example 5:

Input: graph = [[1,3],[2],[3],[]]
Output: [[0,1,2,3],[0,3]]
 
'''
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def backtrack(graph,source,dest,temp_path,all_paths):
        # base case or when we reach leaf
            if(source==dest):
                # we append the current temp path
                # since the condition is met it is a valid path
                all_paths.append(temp_path[:])
                # temp_path is not used as it points to the  original object
                # which is [0]..its a python thing
                return
            for neighbour in graph[source]:
                temp_path.append(neighbour)
                backtrack(graph,neighbour,dest,temp_path,all_paths)
                # we backtrack if the path is not valid
                # we have to remove the nodes while backtracking
                temp_path.pop()
        all_paths = []
        temp_path = [0]
        backtrack(graph,0,len(graph)-1,temp_path,all_paths)
        return all_paths        
