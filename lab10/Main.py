from lab10.BinaryTree import BinaryTree
from lab10.Film import Film
from lab10.Node import Node

if __name__ == '__main__':
    film_1 = Film('dddd', 2004, 156, 'genre1', 'studio1')
    film_2 = Film('aaaa', 2012, 189, 'genre1', 'studio3')
    film_3 = Film('cccc', 2001, 145, 'genre3', 'studio2')
    film_4 = Film('bbbb', 2000, 111, 'genre4', 'studio4')
    film_5 = Film('eeee', 2020, 123, 'genre5', 'studio5')
    tree = BinaryTree()
    node = Node(film_1)
    tree.add_node_by_name(node, film_1)
    tree.add_node_by_name(node, film_2)
    tree.add_node_by_name(node, film_3)
    tree.add_node_by_name(node, film_4)
    tree.add_node_by_name(node, film_5)
    tree.traversal(node)
    print('======================')
    print('After deleting an element:')
    node = tree.delete_node(node, 'studio4')
    tree.traversal(node)
    print('======================')
    print('All films of genre1:')
    tree.print_films_of_one_genre(node, 'genre1')
    print('======================')
    tree.delete_tree(node)
    print('A tree was deleted')


