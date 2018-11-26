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

	groups = []
	print(groups)
	add_group([root], groups)
	print(groups[1])
	return node_dict

def add_group(level, groups):
    for node in level:
        if not node.is_leaf:
            children = node.children
            curr_group = [n.name for n in children]
            groups.append(curr_group)
            add_group(children, groups)

tree_dict = read_tree()