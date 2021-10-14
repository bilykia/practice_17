class BinaryTree:

    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def post_order(self):
        if self.left_child is not None:  # если левый потомок существует
           self.left_child.post_order()  # рекурсивно вызываем функцию

        if self.right_child is not None:  # если правый потомок существует
           self.right_child.post_order()  # рекурсивно вызываем функцию

        print(self.value)  # процедура обработки

    node_root = BinaryTree(2).insert_left(7).insert_right(5)
    node_7 = node_root.left_child.insert_left(2).insert_right(6)
    node_6 = node_7.right_child.insert_left(5).insert_right(11)
    node_5 = node_root.right_child.insert_right(9)
    node_9 = node_5.right_child.insert_left(4)