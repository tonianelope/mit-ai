# Fall 2012 6.034 Lab 2: Search
#
# Your answers for the true and false questions will be in the following form.  
# Your answers will look like one of the two below:
#ANSWER1 = True
#ANSWER1 = False

# 1: True or false - Hill Climbing search is guaranteed to find a solution
#    if there is a solution
ANSWER1 = False

# 2: True or false - Best-first search will give an optimal search result
#    (shortest path length).
#    (If you don't know what we mean by best-first search, refer to
#     http://courses.csail.mit.edu/6.034f/ai3/ch4.pdf (page 13 of the pdf).)
ANSWER2 = False

# 3: True or false - Best-first search and hill climbing make use of
#    heuristic values of nodes.
ANSWER3 = True

# 4: True or false - A* uses an extended-nodes set.
ANSWER4 = True

# 5: True or false - Breadth first search is guaranteed to return a path
#    with the shortest number of nodes.
ANSWER5 = True

# 6: True or false - The regular branch and bound uses heuristic values
#    to speed up the search for an optimal path.
ANSWER6 = False

# Import the Graph data structure from 'search.py'
# Refer to search.py for documentation
from search import Graph

## Optional Warm-up: BFS and DFS
# If you implement these, the offline tester will test them.
# If you don't, it won't.
# The online tester will not test them.

def dfs(graph, start, goal):
    path = [start]
    #extend
    stack = []
    stack.append(path)
    atGoal = False
    while not atGoal:
        path = stack.pop()
        if goal in path:
            atGoal = True
        else:
            next_nodes = [e for e in graph.get_connected_nodes(path[-1])]
            next_nodes = list(filter(lambda x: x not in path, next_nodes))
            for node in next_nodes:
                stack.append(path+[node])
    return path


## Once you have completed the breadth-first search,
## this part should be very simple to complete.
def bfs(graph, start, goal):
    path = [start]
    ext_list = set([])
    q = [path]
    atGoal = False
    while not atGoal:
        path = q.pop(0)
        if goal in path:
            atGoal = True
        else:
            next_nodes = [e for e in graph.get_connected_nodes(path[-1])]
            next_nodes = list(filter(lambda x: x not in path, next_nodes))
            for node in next_nodes:
                if node not in ext_list:
                    q.append(path+[node])
            ext_list.add(path[-1])
    return path


## Now we're going to add some heuristics into the search.
## Remember that hill-climbing is a modified version of depth-first search.
## Search direction should be towards lower heuristic values to the goal.
def hill_climbing(graph, start, goal):
    path = [start]
    agenda = [path]
    current_agenda = agenda
    atGoal = False
    prev_path = []
    while not atGoal:
        #print(agenda,path, graph.get_heuristic(path[-1], goal))
        if goal in path:
            atGoal = True
        else:
            next_nodes = [e for e in graph.get_connected_nodes(path[-1])]
         #   print(next_nodes)
            next_nodes = list(filter(lambda x: x not in path, next_nodes))
            nodes = []
            for node in next_nodes:
                nodes.append(path+[node])
            #agenda = min(agenda, key=lambda path: graph.get_heuristic(path[-1], goal))
            if(len(nodes) == 0):
                path = agenda[-1].pop()
            elif(len(nodes)==1):
                path = nodes.pop()
            else:
                nodes.sort(reverse=True, key=lambda path: graph.get_heuristic(path[-1], goal))
                path = nodes.pop()
                agenda.append(nodes)
    return path



## Now we're going to implement beam search, a variation on BFS
## that caps the amount of memory used to store paths.  Remember,
## we maintain only k candidate paths of length n in our agenda at any time.
## The k top candidates are to be determined using the
## graph get_heuristic function, with lower values being better values.

def all_same_length(listt):
    if len(listt)<1:
        return True
    length = len(listt[0])
    return all(map(lambda x: len(x) == length, listt))


def beam_search(graph, start, goal, beam_width):
    path = [start]
    ext_list = set([])
    agenda = [path]
    #node_q = []
    atGoal = False
    level = 1
    while not atGoal:
        path = agenda.pop(0)
        #print(path)
        level = len(path)+1
        if goal in path:
            atGoal = True
        else:
            next_nodes = [e for e in graph.get_connected_nodes(path[-1])]
            next_nodes = list(filter(lambda x: x not in path, next_nodes))
            for node in next_nodes:
                #if node not in ext_list:
                agenda.append(path+[node])
            #at end of level ... if all paths on agenda same length
            #if all_same_length(agenda):
            if(len(agenda)==0):
                return []
            else:
                level_paths = list(filter(lambda x: len(x) == level, agenda))
                agenda = list(filter(lambda x: x not in level_paths, agenda))
                while(len(level_paths) > beam_width):
                    level_paths.remove(max(level_paths, key=lambda path: graph.get_heuristic(path[-1], goal)))
                agenda += level_paths
    return path

## Now we're going to try optimal search.  The previous searches haven't
## used edge distances in the calculation.

## This function takes in a graph and a list of node names, and returns
## the sum of edge lengths along the path -- the total distance in the path.
def path_length(graph, node_names):
    p_len = 0
    if(len(node_names)>1):
        for node1, node2 in zip(node_names, node_names[1:]):
            #print(node1, node2)
            p_len += graph.get_edge(node1, node2).length
   # print(p_len)
    return p_len

def branch_and_bound(graph, start, goal):
    path = [start]
    agenda = [path]
    atGoal = False

    while not atGoal:
        #path_lens = [path_length(graph, path) for path in agenda]
        agenda = sorted(agenda, key=lambda x: path_length(graph, x))
        path = agenda.pop(0)
        if goal in path:
            atGoal = True
        else:
            next_nodes = [e for e in graph.get_connected_nodes(path[-1]) if e not in path]
            #next_nodes = list(filter(lambda x: x not in path, next_nodes))
            for node in next_nodes:
                #if node not in ext_list:
                agenda.append(path+[node])

    return path


def a_star(graph, start, goal):
    #if not consistent don't use extended set

    path = [start]
    agenda = [path]
    extended = set()
    atGoal = False
    consitent = True #is_consistent(graph, goal)
    while not atGoal:
        agenda = sorted(agenda, key=lambda x: path_length(graph, x)+graph.get_heuristic(x[-1], goal))
        if(len(agenda)==0):
            return []
        path = agenda.pop(0)
        #print(agenda, path)
        if goal in path:
            atGoal = True
        else:
            next_nodes = [e for e in graph.get_connected_nodes(path[-1])]
            next_nodes = list(filter(lambda x: x not in path, next_nodes))
            for node in next_nodes:
                if node not in extended:
                    agenda.append(path+[node])
            if consitent:
                extended.add(path[-1])

    return path


## It's useful to determine if a graph has a consistent and admissible
## heuristic.  You've seen graphs with heuristics that are
## admissible, but not consistent.  Have you seen any graphs that are
## consistent, but not admissible?

# never overestimates cost
def is_admissible(graph, goal):
    all_admis = True
    for node in graph.nodes:
        admis = (graph.get_heuristic(node, goal) <= path_length(graph, branch_and_bound(graph, node, goal)))
        all_admis = admis and all_admis
    return all_admis

# h(N) <= c(N,P) + h(P) and h(G) = 0
def is_consistent(graph, goal):
    all_cons = True
    for node in graph.nodes:
        if(node == goal):
            all_cons = all_cons and graph.get_heuristic(node, goal) == 0
        else:
            adjecent = graph.get_connected_nodes(node)
            for adj_node in adjecent:
                h_node = graph.get_heuristic(node, goal)
                h_adj = graph.get_heuristic(adj_node, goal)
                edge_len = graph.get_edge(node, adj_node).length
                all_cons = all_cons and (h_node <= (edge_len + h_adj))
    return all_cons

HOW_MANY_HOURS_THIS_PSET_TOOK = 'some??? 2-3'
WHAT_I_FOUND_INTERESTING = 'everythoing'
WHAT_I_FOUND_BORING = 'nothing'
