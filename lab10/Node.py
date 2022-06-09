from lab10 import Film


class Node:
    def __init__(self, film: Film):
        self.right = None
        self.left = None
        self.film = film
