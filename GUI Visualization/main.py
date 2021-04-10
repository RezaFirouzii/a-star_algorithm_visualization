import os
from grid import *
from a_star import *

# GUI Constants
TITLE = "A* Algorithm Visualization"
WINDOWS_LOCATION = '350,50'
SIZE = 50
WIDTH = 800
HEIGHT = 800
CELL_SIZE = 10
FPS = 10


# starting game loop
def launch_game(surface):
    grid = Grid(SIZE, SIZE, CELL_SIZE)
    grid.create()

    beginning = None
    destination = None

    algo_kickoff = False
    over = False
    while not over:

        grid.draw(surface)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                over = True

            if algo_kickoff:
                continue

            if pygame.mouse.get_pressed(3)[0]:   # left click
                pos = pygame.mouse.get_pos()
                node = grid.get_mouse_pos(pos)
                if not beginning:
                    node.set_beginning()
                    beginning = node
                elif not destination and node != beginning:
                    node.set_destination()
                    destination = node
                elif node != beginning and node != destination:
                    node.set_wall()

            elif pygame.mouse.get_pressed(3)[2]:   # right click
                pos = pygame.mouse.get_pos()
                node = grid.get_mouse_pos(pos)
                node.set_free()

                if node == beginning:
                    beginning = None
                if node == destination:
                    destination = None

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and not algo_kickoff:
                    algo_kickoff = True
                    a_star(screen, grid, beginning, destination)


if __name__ == '__main__':
    # setting Pygame window position
    os.environ['SDL_VIDEO_WINDOW_POS'] = WINDOWS_LOCATION

    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(TITLE)

    CELL_SIZE = HEIGHT // SIZE
    launch_game(screen)
    pygame.quit()
