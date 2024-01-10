class Forest:
    # A tree node class for a binary tree
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def insert(self, node):
        pass

def check_leaf_node(forest):
    """ This method checks if the given forest is leaf node or not.
        A forest whose left child is None and right child is also None.
    params
        : forest -> Tree Object.
    return
        : True -> bool,  if forest is leaf node.
        : False -> bool, If forest is not leaf Node.
    """
    if forest.left is None and forest.right is None:
        return True
    return False


def find_possible_paths( forest, current_sum, lucky_number, current_path, all_paths):
    """ This method traverse all the paths from root to leaf nodes of the forest object and does sum
        of the numbers that it come across and returns if the sum matches with luck_number.

    params
        : forest -> Tree Object.
        : current_sum -> int
        : lucky_number -> int
        : current_path -> list 
            This is current path of the forest which sum may or may not be luck_number.
        : all_paths -> list
            This list hold all the path whose sum is equals to lucky_number.
    """
    pass # yet to decide the implementation.

def find_lucky_number_paths(forest, lucky_number):
    """ This method will return all paths that matches the lucky number.
    params
        : forest -> Tree Object
        : lucky_number -> int
    return
        : all_paths -> list
    raises
        : ex -> Exception 
    """
    all_paths = []  # This will hold all the paths that sum up to the lucky number
    try:
        find_possible_paths(forest, 0, lucky_number, [], all_paths)
    except Exception as ex:
        raise ex
    return all_paths

# Helper function to build the tree from the list input
def build_tree(nodes_list):
    """ This Method will build Tree out of the list of numbers provided.
    params
        : nodes_list -> list
    Return
        : forest -> Tree Object
    """
    if not nodes_list:
        return None
    forest = Forest(nodes_list[0]) # root of the Tree.
    # This will hold the root element at each iteration so that left and right child can inserted which will be of constant time.
    queue = [forest] 
    i = 1
    # Iteratively build the tree using a queue
    while queue and i < len(nodes_list):
        current = queue.pop(0)
        if nodes_list[i] is not None:
            current.left = Forest(nodes_list[i])
            queue.append(current.left)
        i += 1
        if i < len(nodes_list) and nodes_list[i] is not None:
            current.right = Forest(nodes_list[i])
            queue.append(current.right)
        i += 1
    return forest


if __name__ == '__main__':
    # TestCase #01
    nodes_list = [5, 4, 8, 11, None, 9, 4, None, None, 7, 2, None, None, None, 5, 1]
    lucky_number = 22
    forest = build_tree(nodes_list)

    # Find paths that sum up to the lucky number
    paths = find_lucky_number_paths(forest, lucky_number)

    print("\n\n\n#######################################")
    print("All Paths whose sum matches Lucky Number:- {0}".format(paths))

