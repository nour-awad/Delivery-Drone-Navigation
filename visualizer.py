from shutil import get_terminal_size
from problem import *
import matplotlib.pyplot as plt
import numpy as np

terminal_width, _ = get_terminal_size()

_visualizers = {}

def _default_visualizer(_, state):
    print(state)

# Visualizer
class Visualizer:

    def __init__(self, problem):
        self.problem = problem
        self.counter = 0

    def visualize(self, frontier):

        self.counter += 1
        print(f'Frontier at step {self.counter}')
        for node in frontier:
            print()
            _visualizers.get(type(self.problem), _default_visualizer)(self.problem, node)
        print('-' * terminal_width)

    
    def visualize_state(self, state):
        """Visualizes the state."""
        print(state)  # Or any other suitable visualization logic for the state

def node_visualizer(_, node):
    print(f'Position: {node.position}, Path Cost: {node.path_cost}, Heuristic: {node.heuristic}, Goal: {node.goal}, Start: {node.start}, Go: {node.go}')

_visualizers[Node] = node_visualizer

def visualize_maze(tree, row, col, solution=None, title="Maze"):
    fig, ax = plt.subplots(figsize=(col, row))

    for i in range(row):
        for j in range(col):
            node = tree[(i, j)]
            if not node.go:
                ax.add_patch(plt.Rectangle((j, row - i - 1), 1, 1, color='black'))
                #draw obsticles
            elif node.start:
                ax.add_patch(plt.Rectangle((j, row - i - 1), 1, 1, color='green'))
                ax.text(j + 0.5, row - i - 0.5, "S", ha='center', va='center', color='white', fontsize=12)
                #draw start state
            elif node.goal:
                ax.add_patch(plt.Rectangle((j, row - i - 1), 1, 1, color='red'))
                ax.text(j + 0.5, row - i - 0.5, "Goal", ha='center', va='center', color='white', fontsize=12)
                #draw goal state

            elif solution and node.is_part_of_solution(solution):
                ax.add_patch(plt.Rectangle((j, row - i - 1), 1, 1, color='blue'))
                #draw the path taken

    ax.set_xticks(np.arange(0, col, 1))
    ax.set_yticks(np.arange(0, row, 1))

    ax.set_xticklabels([])
    ax.set_yticklabels([])

    ax.grid(True)
    ax.set_title(title)
    plt.show()
