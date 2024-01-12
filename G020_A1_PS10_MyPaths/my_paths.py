class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left_node = None
        self.right_node = None

    def is_leaf(self):
        return not self.left_node and not self.right_node

def create_node(value):
    return TreeNode(value) if value is not None else None

def construct_tree_list(input_tree_array):
    size_of_input_array = len(input_tree_array)
    
    if size_of_input_array == 0 or input_tree_array[0] is None:
        return None  # Empty or invalid input
    
    root_node = create_node(input_tree_array[0])
    leaf_queue = [root_node]

    j = 1
    while j < size_of_input_array:
        leaf = leaf_queue.pop(0)
        
        left_value = input_tree_array[j] if j < size_of_input_array else None
        j += 1

        if left_value is not None:
            leaf.left_node = create_node(left_value)
            leaf_queue.append(leaf.left_node)

        right_value = input_tree_array[j] if j < size_of_input_array else None
        j += 1
        if right_value is not None:
            leaf.right_node = create_node(right_value)
            leaf_queue.append(leaf.right_node)

    return root_node

def print_tree(root_node):
    if not root_node:
        return

    queue = [root_node]

    while queue:
        current_level = len(queue)
        for i in range(current_level):
            node = queue.pop(0)
            if node:
                print(node.value, end=' ')
                queue.append(node.left_node)
                queue.append(node.right_node)
            else:
                print('null', end=' ')
        
        print()  # Move to the next level

def find_my_paths(node, path, sum, lucky_num, paths):
    if not node:
        return

    value_of_node = node.value

    path += str(value_of_node) + ','
    sum += value_of_node

    if sum == lucky_num and node.is_leaf():
        paths.append(path[:-1]) # Remove the trailing comma
        # print(path[:-1])  

    # Traverse left sub tree
    find_my_paths(node.left_node, path, sum, lucky_num, paths)
    # Traverse right sub tree
    find_my_paths(node.right_node, path, sum, lucky_num, paths)

    return

def convert_value(value):
    try:
        return int(value) if value != "null" else None
    except ValueError:
        return None

def parse_input_line(line):
    if not line:
        return None, None

    try:
        tree_values, target_sum = line.split("::")
        values = tree_values.split(",")
    except ValueError:
        return None, None
    

    converted_values = [convert_value(val) for val in values]
    target_sum = convert_value(target_sum)

    return converted_values, target_sum

def write_to_file(file_path, data):
    with open(file_path, 'w') as file:
        for line in data:
            file.write(line + '\n')

def main():
    with open("inputPS10.txt", "r") as file:
        content = file.read().splitlines()

    output_data = []
    for line in content:
        input_tree_array, lucky_num = parse_input_line(line)
        if input_tree_array is not None and lucky_num is not None:
            root_node = construct_tree_list(input_tree_array)
            # print("Input:")
            # print(input_tree_array)
            # print("Tree constructed")
            # print_tree(root_node)
            # print("Lucky Paths")
            paths = []
            find_my_paths(root_node, "", 0, lucky_num, paths)
            # print("")
            output_data.append(";".join(paths))

    write_to_file("outputPS10.txt", output_data)

if __name__ == "__main__":
    main()


# def find_my_paths_iterative(node, lucky_num):
#     if not node:
#         return

#     to_visit_nodes = [node]
    
#     sum = 0
#     path = []
#     while to_visit_nodes:
#         n = to_visit_nodes.pop()
#         path.append(n)
#         sum += n.value

#         if sum == lucky_num and n.is_leaf():
#             # Print lucky_num path
#             values_as_strings = [str(node.value) for node in path]
#             print(",".join(values_as_strings))
#             sum -= n.value
#             path.pop()

#         if n.is_leaf() and to_visit_nodes:
#             next_n = to_visit_nodes[-1]
#             while path:
#                 p = path[-1]
#                 if p.right_node == next_n or p.left_node == next_n:
#                     break
#                 sum -= p.value
#                 path.pop()
#         else:
#             if n.right_node:
#                 to_visit_nodes.append(n.right_node)
#             if n.left_node:
#                 to_visit_nodes.append(n.left_node)

#     return
