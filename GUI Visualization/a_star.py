
# this is the main algorithm implementation

import math
import pygame
from queue import PriorityQueue


# create_path: creates the path from all saved previous nodes
def create_path(surface, grid, previous_nodes, current):
    path = []
    while current in previous_nodes:
        current = previous_nodes[current]
        path.append(current)

    path.pop(-1)
    path.reverse()
    for node in path:
        node.set_path()
        grid.draw(surface)


# the main heuristic
def manhattan_heuristic(node1, node2):
    return abs(node1.row - node2.row) + abs(node1.col - node2.col)


def a_star(surface, grid, start, end):

    count = 0
    visiting_set = set()
    visiting_q = PriorityQueue()

    visiting_set.add(start)
    visiting_q.put((0, count, start))

    g_table = {node: math.inf for row in grid.grid for node in row}
    g_table[start] = 0

    f_table = {node: math.inf for row in grid.grid for node in row}
    f_table[start] = g_table[start] + manhattan_heuristic(start, end)

    previous_nodes = {}

    while not visiting_q.empty():

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = visiting_q.get()[2]
        visiting_set.remove(current)

        if current == end:
            end.set_destination()
            create_path(surface, grid, previous_nodes, end)
            return True

        last = None
        if current != start:
            last = previous_nodes[current]

        for neighbor in current.get_neighbors(grid.grid, last):
            g = g_table[current] + 1

            if g < g_table[neighbor]:
                g_table[neighbor] = g
                f_table[neighbor] = g + manhattan_heuristic(neighbor, end)
                previous_nodes[neighbor] = current
                if neighbor not in visiting_set:
                    count += 1
                    visiting_set.add(neighbor)
                    visiting_q.put((f_table[neighbor], count, neighbor))
                    neighbor.visit()

        grid.draw(surface)

        if current != start:
            current.set_checked()

    return False
