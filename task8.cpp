#include <iostream>

void Textformat(const char* text, int n) {
	int lineLenght = 0;
	for (int i = 0; text[i] != '\0'; ++i) {
		char c = text[i];
		if (c == '\n') {
			std::cout << '\n' << '\n';
			lineLenght = 0;
			continue;
		}
		std::cout << c;
		lineLenght++;
		if (lineLenght == n) {
			std::cout << '\n';
			lineLenght = 0;
		}
	}
	std::cout << '\n';
	lineLenght = 0;
}
int main() {
	const int MAX_TEXT_SIZE = 10000;
	char text[MAX_TEXT_SIZE];
	int n;
	std::cout << "Enter line widht (n > 50): ";
	std::cin >> n;
	std::cin.ignore();
	if (n <= 50) {
		std::cout << "Line widht must be more that 50!" << std::endl;
		return 1;
	}
	std::cout << "Enter text (end input CTRL+D or Enter after empty line):" << std::endl;
	std::cin.getline(text, MAX_TEXT_SIZE, '\0');
	std::cout << "\nFormatted text:\n";
	Textformat(text, n);
	return 0;
}
