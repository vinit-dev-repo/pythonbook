class Node:
    def __init__(self, name):
        self.name = name
        self.other = None

node_a = Node("A")
node_b = Node("B")
node_a.other = node_b
node_b.other = node_a            # a circle: A points to B, B points to A

del node_a
del node_b                       # both names are gone, but the two objects still point at each other
