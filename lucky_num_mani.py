class TreeNode:
    def __init__(self, value):
        self.value = value
        self.leftNode = None
        self.rightNode = None

def createNode(value):
    return TreeNode(value) if value is not None else None

def constructTreeList(inputTreeArray):
    sizeOfInputArray = len(inputTreeArray)
    
    if sizeOfInputArray == 0 or inputTreeArray[0] is None:
        return None  # Empty or invalid input
    
    rootNode = createNode(inputTreeArray[0])
    leafQueue = [rootNode]

    j = 1
    while j < sizeOfInputArray:
        leaf = leafQueue.pop(0)
        
        leftValue = inputTreeArray[j] if j < sizeOfInputArray else None
        j += 1

        if leftValue is not None:
            leaf.leftNode = createNode(leftValue)
            leafQueue.append(leaf.leftNode)

        rightValue = inputTreeArray[j] if j < sizeOfInputArray else None
        j += 1
        if rightValue is not None:
            leaf.rightNode = createNode(rightValue)
            leafQueue.append(leaf.rightNode)

    return rootNode

def printTree(rootNode):
    if not rootNode:
        return

    queue = [rootNode]

    while queue:
        currentLevel = len(queue)
        for i in range(currentLevel):
            node = queue.pop(0)
            if node:
                print(node.value, end=' ')
                queue.append(node.leftNode)
                queue.append(node.rightNode)
            else:
                print('null', end=' ')
        
        print()  # Move to the next level

def find_luck_number_path(node, path, sum, lucky_num):
    if not node:
        return

    value_of_node = node.value

    path += str(value_of_node) + ','
    sum += value_of_node

    if sum == lucky_num:
        # Print lucky_num path
        print(path[:-1])  # Remove the trailing comma

    # Traverse left sub tree
    find_luck_number_path(node.leftNode, path, sum, lucky_num)
    # Traverse right sub tree
    find_luck_number_path(node.rightNode, path, sum, lucky_num)

    return

def find_luck_number_path_by_stack(node, stack, sum, lucky_num):
    if not node:
        return

    value_of_node = node.value
    stack.append(value_of_node)
    sum += value_of_node

    if sum == lucky_num:
        # Print the specific path that equals the lucky_num
        print(stack)

    # Traverse left sub tree
    find_luck_number_path_by_stack(node.leftNode, stack, sum, lucky_num)
    # Traverse right sub tree
    find_luck_number_path_by_stack(node.rightNode, stack, sum, lucky_num)

    stack.pop()

    return

# Example usage:
inputTreeArray = [5, 4, 8, 11, None, 9, 4, -7, 2, None, None, 5, 1]
rootNode = constructTreeList(inputTreeArray)
print("Input:")
print(inputTreeArray)
print("Tree constructed")
printTree(rootNode)
print("Luck Paths")
find_luck_number_path_by_stack(rootNode, [], 0, 22)
print("")

inputTreeArray = [1,4,3,None,None,-10,None,11,2]
rootNode = constructTreeList(inputTreeArray)
print("Input:")
print(inputTreeArray)
print("Tree constructed")
printTree(rootNode)
print("Luck Paths")
find_luck_number_path(rootNode, "", 0, 5)
print("")

inputTreeArray = [1,2,3,4,5,None,-4,1]
rootNode = constructTreeList(inputTreeArray)
print("Input:")
print(inputTreeArray)
print("Tree constructed")
printTree(rootNode)
print("Luck Paths")
find_luck_number_path(rootNode, "", 0, 8)

