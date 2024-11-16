# Create a maze
row, col = 40, 40
tree = tree_creation(row, col)
tree = building(tree, row, col)
assign_cost(tree, row, col)
