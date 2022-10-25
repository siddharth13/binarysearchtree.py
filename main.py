class TreeNode:
    def __init__(self, data):
        self._data = data
        self._left = None
        self._right = None

    # setter for data of the TreeNode
    def set_data(self, data):
        self._data = data

    # getter for data of the TreeNode
    def get_data(self):
        return self._data

    def set_left_node(self, left_node=None):
        self._left = left_node

    def get_left_node(self):
        return self._left

    def set_right_node(self, right_node=None):
        self._right = right_node

    def get_right_node(self):
        return self._right


class BinarySearchTree:
    def __init__(self, limit):
        self._root = None
        self._sizeLimit = limit
        self._currentSize = 0

    def insert(self, data):
        current_root=self.get_root()
        if current_root is None:
            self.set_root(data)
        else:
            while current_root is not None:
                if current_root.get_left_tree_node() is None and current_root.getRightTreeNode() is None:
                    if data >= current_root.get_data():
                        current_root.set_right_node(TreeNode(data))
                    else:
                        current_root.set_left_node(TreeNode(data))
                    break
                elif current_root.getLeftTreeNode() is None:
                    if data >= current_root.getData():
                        current_root = current_root.getRightNode()
                    else:
                        pass

    def get_size_of_tree(self):
        return self._currentSize

    def get_root(self):
        return self._root

    def set_root(self,value):
        self._root=TreeNode(value)

    def is_empty(self):
        return True if self.get_root() is None else False

    def is_full(self):
        return True if self.getSizeOfTree() == self._sizelimit
