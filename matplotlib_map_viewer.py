import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import sys

def load_map(file_path):
    try:
        with open(file_path, 'r') as f:
            return np.array([list(line.strip()) for line in f])
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        sys.exit(1)

def main():
    if len(sys.argv) != 2:
        print("Usage: python matplotlib_map_viewer.py <path_to_map_file>")
        sys.exit(1)

    map_file_path = sys.argv[1]
    game_map = load_map(map_file_path)

    # Create a colormap for the different tile types
    cmap = mcolors.ListedColormap(['white', 'black', 'blue'])
    bounds = [0, 1, 2, 3]
    norm = mcolors.BoundaryNorm(bounds, cmap.N)

    # Convert the character map to a numerical map
    numerical_map = np.zeros(game_map.shape)
    numerical_map[game_map == '#'] = 1
    numerical_map[game_map == '@'] = 2

    # Create the plot
    fig, ax = plt.subplots()
    ax.imshow(numerical_map, cmap=cmap, norm=norm)

    # Draw gridlines
    ax.grid(which='major', axis='both', linestyle='-', color='k', linewidth=2)
    ax.set_xticks(np.arange(-.5, game_map.shape[1], 1))
    ax.set_yticks(np.arange(-.5, game_map.shape[0], 1))

    # Hide the tick labels
    ax.set_xticklabels([])
    ax.set_yticklabels([])


    plt.show()


if __name__ == "__main__":
    main()
