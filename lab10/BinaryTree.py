from lab10.Film import Film
from lab10.Node import Node


class BinaryTree:
    def __init__(self):
        self.root = None

    def add_node_by_name(self, current_node: Node, film: Film):
        if not self.root:
            self.root = Node(film)
        else:
            if film.name < current_node.film.name:
                if not current_node.left:
                    current_node.left = Node(film)
                else:
                    self.add_node_by_name(current_node.left, film)
            else:
                if not current_node.right:
                    current_node.right = Node(film)
                else:
                    self.add_node_by_name(current_node.right, film)

    def traversal(self, current_node: Node):
        if current_node:
            self.traversal(current_node.left)
            print(current_node.film)
            self.traversal(current_node.right)

    def delete_node(self, root: Node, key: str):
        if not root:
            return root
        root.left = self.delete_node(root.left, key)
        root.right = self.delete_node(root.right, key)
        if key == root.film.studio:
            if not root.left:
                temp = root.right
                root = None
                return temp
            elif not root.right:
                temp = root.left
                root = None
                return temp
            temp = self.min_value_node(root.right)
            root.film.name = temp.film.name
            root.right = self.delete_node(root.right, temp.film.studio)
        return root

    def min_value_node(self, node: Node):
        current = node
        while current.left:
            current = current.left
        return current

    def print_films_of_one_genre(self, current_node: Node, genre: str):
        if current_node:
            self.print_films_of_one_genre(current_node.left, genre)
            if current_node.film.genre == genre:
                print(current_node.film)
            self.print_films_of_one_genre(current_node.right, genre)

    def delete_tree(self, node: Node):
        if node:
            self.delete_tree(node.left)
            self.delete_tree(node.right)
            print(f'Deleted node: {node.film}')
            del node
