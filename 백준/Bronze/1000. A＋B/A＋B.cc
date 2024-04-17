#include <iostream>
#include <string>

int main() {
    std::string input;
    std::getline(std::cin, input);
    size_t space_pos = input.find(' ');
    int a = std::stoi(input.substr(0, space_pos));
    int b = std::stoi(input.substr(space_pos + 1));
    std::cout << a + b << std::endl;
    return 0;
}