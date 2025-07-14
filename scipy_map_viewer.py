import numpy as np
from scipy.ndimage import label
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
        print("Usage: python scipy_map_viewer.py <path_to_map_file>")
        sys.exit(1)

    map_file_path = sys.argv[1]
    game_map = load_map(map_file_path)

    print("Map:")
    for row in game_map:
        print("".join(row))

    # Example of using a SciPy function: label connected components
    # We'll label the open spaces.
    open_space = game_map == ' '
    labeled_array, num_features = label(open_space)
    print(f"\\nNumber of distinct open areas: {num_features}")


if __name__ == "__main__":
    main()
