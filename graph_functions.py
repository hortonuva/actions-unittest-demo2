__author__ = 'horton'

from operator import itemgetter
# from my_adts import Queue, Graph
from graph import Graph

def is_complete(gr):
    if not isinstance(gr, Graph):  # this test is not needed for HW3 in S14
        raise TypeError
    is_compl = True
    for n1 in gr:
        adj_list = gr.get_adjlist(n1)
        for n2 in gr:
            if n1 != n2 and n2 not in adj_list:
                return False
    return True

def is_complete2(gr):
    # this version assumes it's a valid graph, which is OK for HW3 in S14
    num_nodes = len(gr)
    for n in gr:
        if len(gr.get_adjlist(n)) != num_nodes-1:
            return False
    return True

def nodes_by_degree(gr):
    result = []
    for n in gr:
        result.append( (n, len(gr.get_adjlist(n))) )
    return sorted(result, key=itemgetter(1), reverse=True)


def main():
    gr1 = Graph(
            { 'a': ['b', 'c', 'd'], 'b': ['a', 'd'], 'c' : ['a'], 'd' : ['b', 'a'], 'e' : []}
    )
    print("gr1: ", gr1)
    print(is_complete2(gr1))
    print(nodes_by_degree(gr1))


if __name__ == '__main__':
    main()


