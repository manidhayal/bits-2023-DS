class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left_node = None
        self.right_node = None

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

def find_lucky_number(node, path, sum, lucky_num):
    if not node:
        return

    value_of_node = node.value

    path += str(value_of_node) + ','
    sum += value_of_node

    if sum == lucky_num:
        # Print lucky_num path
        print(path[:-1])  # Remove the trailing comma

    # Traverse left sub tree
    find_lucky_number(node.left_node, path, sum, lucky_num)
    # Traverse right sub tree
    find_lucky_number(node.right_node, path, sum, lucky_num)

    return

# Example usage:
input_tree_array = [5, 4, 8, 11, None, 9, 4, -7, 2, None, None, 5, 1]
root_node = construct_tree_list(input_tree_array)
print("Input:")
print(input_tree_array)
print("Tree constructed")
print_tree(root_node)
print("Lucky Paths")
find_lucky_number(root_node, "", 0, 22)
print("")

input_tree_array = [1, 4, 3, None, None, -10, None, 11, 2]
root_node = construct_tree_list(input_tree_array)
print("Input:")
print(input_tree_array)
print("Tree constructed")
print_tree(root_node)
print("Lucky Paths")
find_lucky_number(root_node, "", 0, 5)
print("")

input_tree_array = [1, 2, 3, 4, 5, None, -4, 1]
root_node = construct_tree_list(input_tree_array)
print("Input:")
print(input_tree_array)
print("Tree constructed")
print_tree(root_node)
print("Lucky Paths")
find_lucky_number(root_node, "", 0, 0)
