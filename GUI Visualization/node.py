import pygame
from color import Color


# represents each node of the graph or grid
class Node:
    def __init__(self, row, col, cell_size):
        self.row = row
        self.col = col
        self.x = row * cell_size
        self.y = col * cell_size
        self.size = cell_size
        self.color = Color.WHITE
        self.neighbors = []

    def is_checked(self):
        return self.color == Color.RED

    def visiting(self):
        return self.color == Color.GREEN

    def is_wall(self):
        return self.color == Color.BLACK

    def is_destination(self):
        return self.color == Color.BLUE

    def set_free(self):
        self.color = Color.WHITE

    def set_checked(self):
        self.color = Color.RED

    def visit(self):
        self.color = Color.GREEN

    def set_wall(self):
        self.color = Color.BLACK

    def set_beginning(self):
        self.color = Color.PINK

    def set_destination(self):
        self.color = Color.BLUE

    def set_path(self):
        self.color = Color.YELLOW

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))

    def get_neighbors(self, grid, last):
        size = (len(grid), len(grid[0]))   # (width, height)
        sides = [(self.row + 1, self.col), (self.row - 1, self.col), (self.row, self.col + 1), (self.row, self.col - 1)]
        neighbors = []
        for i in range(len(sides)):
            if self.is_valid(grid, sides[i], last, size):
                x, y = sides[i]
                neighbors.append(grid[x][y])

        return neighbors

    @staticmethod
    def is_valid(grid, pos, last_node, size):
        x, y = pos
        return 0 <= x < size[0] and 0 <= y < size[1] and not grid[x][y].is_wall() and grid[x][y] != last_node
