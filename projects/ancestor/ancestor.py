
def earliest_ancestor(ancestors, starting_node):
    # build an ajacency list from ancestors, keys are children, values are parents
    # create blank list
    ancestor_list = {}
    # for loop over ancestors
    for node in ancestors:
        print(node)
        # if child key exists
        if node[1] in ancestor_list.keys():
            # add parent to existing set
            ancestor_list[node[1]].add(node[0])
        # else, create key with parent in value set
        else:
            ancestor_list[node[1]] = {node[0]}

    # traverse child to parents until None
