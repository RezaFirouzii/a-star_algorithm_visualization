import pygame
from color import Color
from node import Node


# represent the graph/grid object
class Grid:
    def __init__(self, rows, cols, cell_size):
        self.grid = []
        self.rows = rows
        self.cols = cols
        self.width = self.rows * cell_size
        self.height = self.cols * cell_size
        self.cell_size = cell_size

    def create(self):
        for i in range(self.rows):
            self.grid.append([])
            for j in range(self.cols):
                node = Node(i, j, self.cell_size)
                self.grid[i].append(node)

    def draw_borders(self, surface):
        for i in range(self.rows):
            pygame.draw.line(surface, Color.GREY, (0, i * self.cell_size), (self.width, i * self.cell_size))
            for j in range(self.cols):
                pygame.draw.line(surface, Color.GREY, (j * self.cell_size, 0), (j * self.cell_size, self.height))

    def draw(self, surface):
        surface.fill(Color.WHITE)
        for row in self.grid:
            for node in row:
                node.draw(surface)

        self.draw_borders(surface)
        pygame.display.update()

    # helper method: returns the clicked cell
    def get_mouse_pos(self, pos):
        x, y = pos
        row = x // self.cell_size
        col = y // self.cell_size
        return self.grid[row][col]
