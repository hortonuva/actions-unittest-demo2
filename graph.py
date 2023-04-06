__author__ = 'horton'

from copy import deepcopy

class Graph:
    def __init__(self, dict={}):
        #self.adj_dict = dict # no, not this!!! need to make copy! many ways to do that
        self.adj_dict = deepcopy(dict)  # this is one way (of many) to do that

    def get_adjlist(self, vertex):
        return self.adj_dict.get(vertex, None)

    def is_adjacent(self, v1, v2):
        alist = self.adj_dict.get(v1, None)
        if alist == None:
            return False
        return v2 in alist

    def num_nodes(self):
        return len(self.adj_dict)

    def __str__(self):
        return str(self.adj_dict)

    def __iter__(self):
        return iter(self.adj_dict)

    def __contains__(self, value):
        return value in self.adj_dict

    def __len__(self):
        return len(self.adj_dict)

    def addNode(self, node):
        if node in self.adj_dict:
            return False
        self.adj_dict[node] = [ ]
        return True

    def link_nodes(self, node1, node2):
        if node1 not in self.adj_dict or node2 not in self.adj_dict:
            return False
        if node1 == node2 or self.is_adjacent(node1,node2):
            return False
        self.adj_dict[node1].append(node2)
        self.adj_dict[node2].append(node1)
        return True

    def unlink_nodes(self, node1, node2):
        if node1 not in self.adj_dict or node2 not in self.adj_dict:
            return False
        if node1 == node2 or not self.is_adjacent(node1,node2):
            return False
        self.adj_dict[node1].remove(node2)
        self.adj_dict[node2].remove(node1)
        return True

    def del_node(self, node):
        if node not in self.adj_dict:
            return False
        del(self.adj_dict[node])

        for n in self.adj_dict:
            if node in self.adj_dict[n]:
                self.adj_dict[n].remove(node)
        return True


def main():
    g = Graph( { 'A': ['B', 'D'], 'B': ['A', 'D', 'C'], 'C': ['B'], 'D': ['A', 'B'], 'E' : [] } )
    print(g)
    # for n in g:
    #     print n
    print('C' in g)
    print('X' in g)

    # g2 = Graph( str(g) )
    # print(g2.num_nodes())
    # for i in g2:
    #     print(i)

if __name__ == '__main__':
    main()


