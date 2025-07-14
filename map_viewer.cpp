#include <iostream>
#include <fstream>
#include <string>
#include <vector>

void load_and_display_map(const std::string& file_path) {
    std::ifstream map_file(file_path);
    if (!map_file.is_open()) {
        std::cerr << "Error: Could not open file " << file_path << std::endl;
        return;
    }

    std::string line;
    while (std::getline(map_file, line)) {
        std::cout << line << std::endl;
    }

    map_file.close();
}

int main(int argc, char* argv[]) {
    if (argc != 2) {
        std::cout << "Usage: ./map_viewer <path_to_map_file>" << std::endl;
        return 1;
    }

    load_and_display_map(argv[1]);

    return 0;
}
