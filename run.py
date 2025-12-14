import search
import time

problem = search.GPSProblem('O', 'E', 
                            search.romania)

node_bfs, visited_bfs, generated_bfs, cost_bfs = search.breadth_first_graph_search(problem)
print("BFS generated:", generated_bfs)
print("BFS visited:", visited_bfs)
print("BFS cost:", cost_bfs)
print("BFS path:", node_bfs.path())

print("==============================")

node_dfs, visited_dfs, generated_dfs, cost_dfs = search.depth_first_graph_search(problem)
print("DFS generated:", generated_dfs)
print("DFS visited:", visited_dfs)
print("DFS cost:", cost_dfs)
print("DFS path:", node_dfs.path())

print("===============================")

# Branch and Bound sin subestimación
node_bb, visited_bb, generated_bb, cost_bb = search.branch_and_bound_Without(problem)
print("Branch and Bound without subestimation generated:", generated_bb)
print("Branch and Bound without subestimation visited:", visited_bb)
print("Branch and Bound without subestimation cost:", cost_bb)
print("Branch and Bound without subestimation path:", node_bb.path())

print("==============================")

# Branch and Bound con subestimación
node_bbw, visited_bbw, generated_bbw, cost_bbw = search.branch_and_bound_With(problem)
print("Branch and Bound with subestimation generated:", generated_bbw)
print("Branch and Bound with subestimation visited:", visited_bbw)
print("Branch and Bound with subestimation cost:", cost_bbw)
print("Branch and Bound with subestimation path:", node_bbw.path())
