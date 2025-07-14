import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
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
        print("Usage: python seaborn_map_viewer.py <path_to_map_file>")
        sys.exit(1)

    map_file_path = sys.argv[1]
    game_map = load_map(map_file_path)

    # Convert the character map to a numerical map
    numerical_map = np.zeros(game_map.shape)
    numerical_map[game_map == '#'] = 1
    numerical_map[game_map == '@'] = 2

    # Create the heatmap with Seaborn
    ax = sns.heatmap(numerical_map, cmap="viridis", linewidths=.5, linecolor='black', cbar=False)

    # Set the aspect of the plot to be equal
    ax.set_aspect('equal')

    plt.show()


if __name__ == "__main__":
    main()
