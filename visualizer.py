# Get the terminal width
terminal_width, _ = get_terminal_size()

# Dictionary to store visualizer functions for different problem types
_visualizers = {}

# Default visualizer function
def _default_visualizer(_, state):
    '''Generic visualizer for unknown problems.'''
    print(state)

# Visualizer class
class Visualizer:
    '''Visualization and printing functionality encapsulation.'''

    def __init__(self, problem):
        '''Constructor with the problem to visualize.'''
        self.problem = problem
        self.counter = 0

    def visualize(self, frontier):
        '''Visualizes the frontier at every step.'''
        self.counter += 1
        print(f'Frontier at step {self.counter}')
        for node in frontier:
            print()
            _visualizers.get(type(self.problem), _default_visualizer)(self.problem, node)
        print('-' * terminal_width)

# Custom visualizer for the Node class
def node_visualizer(_, node):
    '''Visualizer for Node objects.'''
    print(f'Position: {node.position}, Path Cost: {node.path_cost}, Heuristic: {node.heuristic}, Goal: {node.goal}, Start: {node.start}, Go: {node.go}')

# Register the custom visualizer for the Node class
_visualizers[Node] = node_visualizer
