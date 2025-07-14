import numpy as np
from sklearn.cluster import KMeans
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
        print("Usage: python scikit_map_viewer.py <path_to_map_file>")
        sys.exit(1)

    map_file_path = sys.argv[1]
    game_map = load_map(map_file_path)

    print("Map:")
    for row in game_map:
        print("".join(row))

    # Example of using a scikit-learn function: KMeans clustering
    # We'll cluster the character codes.
    # First, we need to convert the character data to numerical data.
    # We'll use the ASCII values of the characters.
    numerical_map = np.array([[ord(char) for char in row] for row in game_map])
    # We need to reshape the data to be a 1D array of samples
    X = numerical_map.reshape(-1, 1)

    # We'll create 3 clusters: walls, open space, and the player
    kmeans = KMeans(n_clusters=3, random_state=0, n_init=10)
    kmeans.fit(X)

    print(f"\\nCluster centers found by KMeans: {kmeans.cluster_centers_.flatten()}")


if __name__ == "__main__":
    main()
