# C++ Map Viewer

This is a simple command-line application to view `.map` files, written in C++.

## Building the Application

To build the application, you will need to have `cmake` and `make` installed.

1. Create a build directory: `mkdir build`
2. Navigate to the build directory: `cd build`
3. Run cmake: `cmake ..`
4. Run make: `make`

## Usage

To use the map viewer, run the following command from the `build` directory:

```bash
./map_viewer <path_to_map_file>
```

Replace `<path_to_map_file>` with the actual path to your `.map` file. You will need to provide the path relative to the `build` directory.

### Example

```bash
./map_viewer ../test.map
```
