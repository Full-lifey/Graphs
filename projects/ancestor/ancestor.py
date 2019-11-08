from util import Stack, Queue  # These may come in handy


def earliest_ancestor(ancestors, starting_node):
    # build an ajacency list from ancestors, keys are children, values are parents
    # create blank list
    ancestor_list = {}
    # for loop over ancestors
    for node in ancestors:
        # if child key exists
        if node[1] in ancestor_list.keys():
            # add parent to existing set
            ancestor_list[node[1]].add(node[0])
        # else, create key with parent in value set
        else:
            ancestor_list[node[1]] = {node[0]}

    # use dft child to parents until key not in ancestor_list

    # Create empty stack and push a path to starting_node
    oldest_ancestors = []
    s = Stack()
    s.push([starting_node])

    # while stack is not empty
    while s.size() > 0:
        # pop the path
        path = s.pop()
        # if last vertex has a parent
        if path[-1] in ancestor_list:
            # add a path to parent to back of stack
            for parent in ancestor_list[path[-1]]:
                # copy the path
                new_path = path.copy()
                # append the parent
                new_path.append(parent)
                # add to stack
                s.push(new_path)
        # else, append path to oldest_ancestors
        else:
            oldest_ancestors.append(path)

    if len(oldest_ancestors[0]) == 1:
        return -1
    # save answer path
    answer_path = oldest_ancestors[0]
    # loop over oldest_ancestors
    for i in range(1, len(oldest_ancestors)):
        # if arrays are same size
        if len(oldest_ancestors[i]) == len(answer_path):
            # if oldest_ancestors[i] tail node is smaller than answer_path tail node
            if oldest_ancestors[i][-1] < answer_path[-1]:
                # replace answer_path
                answer_path = oldest_ancestors[i]
        # elif new array is larger
        elif len(oldest_ancestors[i]) > len(answer_path):
            # replace answer_path
            answer_path = oldest_ancestors[i]

    return answer_path[-1]
