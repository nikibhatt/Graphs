

class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

def get_parents(node, ancestors):
    parents = []
    for x in ancestors:
        parent, child = x
        if child == node:
            parents.append(parent)

    return parents

def earliest_ancestor(ancestors, starting_node):
    ancestors = ancestors
    visited = set()
    s = Stack()
    s.push([starting_node])
    while s.size() > 0:
        path = s.pop()
        v = path[-1]
        if v not in visited:
            visited.add(v)
            parents = get_parents(v, ancestors)
            if v == starting_node and parents == []:
                return -1
            if parents == [] and s.size() == 0:
                return v
            for parent in parents:
                path_copy = list(path)
                path_copy.append(parent)
                s.push(path_copy)


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

print(earliest_ancestor(test_ancestors, 3))
