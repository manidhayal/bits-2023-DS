INPUT_FILE = "inputPS10.txt"
OUTPUT_FILE = "outputPS10.txt"

class TreeNode:
    """A tree node class for a binary tree"""
    def __init__(self, value):
        self.value = value
        self.left_node = None
        self.right_node = None

    def is_leaf(self):
        """ This method checks if the given TreeNode is leaf node or not.
            A TreeNode whose left child is None and right child is also None."""
        return not self.left_node and not self.right_node

def create_node(value):
    """ This builder method will create Node.
    params
        : value -> int
    return
        : TreeNode -> TreeNode Object
    """
    return TreeNode(value) if value is not None else None

def construct_tree_list(input_tree_array):
    """ This Method will build Tree out of the list of numbers provided
    params
        : input_tree_array -> list
    Return
        : root_node -> Tree Object
    """
    size_of_input_array = len(input_tree_array)

    if size_of_input_array == 0 or input_tree_array[0] is None:
        return None  # Empty or invalid input

    # This will hold the root element at each iteration so that left and right child can inserted which will be of constant time.
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
    """ Print the paths on the Tree for Left and Right Childs.
    params
        : root_node -> Tree object.
    """
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
    """ This method traverse all the paths from root to leaf nodes of the forest object and does sum
        of the numbers that it come across and returns if the sum matches with luck_number.

    params
        : node -> Tree Object.
        : sum -> int
        : lucky_num -> int
        : path -> string 
            This is current path of the forest which sum may or may not be luck_number.
        : paths -> list
            This list hold all the path whose sum is equals to lucky_number.
    """
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

# Driver code
if __name__ == "__main__":
    with open(INPUT_FILE, "r") as file:
        content = file.read().splitlines()

    output_data = []
    for line in content:
        input_tree_array, lucky_num = parse_input_line(line)
        if input_tree_array is not None and lucky_num is not None:
            root_node = construct_tree_list(input_tree_array)
            paths = []
            find_my_paths(root_node, "", 0, lucky_num, paths)
            output_data.append(";".join(paths))

    write_to_file(OUTPUT_FILE, output_data)
