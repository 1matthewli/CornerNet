from anytree import Node, RenderTree

def read_tree():
	tree_file = '../../metadata/9k.tree'
	f = open(tree_file, 'r')

	node_indices = {}
	node_dict = {}

	root = Node("root")
	node_indices[-1] = root

	lines = f.readlines()
	for i in range(len(lines)):
		line = lines[i]
		tokens = line.split()

		new_node = Node(tokens[0], parent=node_indices[int(tokens[1])])
		node_indices[i] = new_node
		node_dict[tokens[0]] = new_node

	return node_dict

tree_dict = read_tree()
print(tree_dict['n00003553'].ancestors)