#include <iostream>

void extract_message(const char* text) {
	int state = 0;
	int bit_index = 7;
	char current_char = 0;
	char extracted_message[100];
	int j = 0;
	int space_count = 0;
	for (int i = 0; text[i] != '\0'; i++) {
		if (text[i] == ' ') {
			space_count++;
		} else {
			if (space_count > 0) {
				int bit = ( space_count == 2) ? 1 : 0;
				current_char |= (bit << bit_index);
				if (bit_index == 0) {
					extracted_message[j++] = current_char;
					current_char = 0;
					bit_index = 7;
				} else {
					bit_index--;
				}
				space_count = 0;
			}
		}
	}
	extracted_message[j] = '\0';
	std::cout << "Extracted message: " << extracted_message << std::endl;
}
int main() {
	char text[500];
	std::cout << "Enter text: ";
	std::cin.getline(text, 500);
		extract_message(text);
		return 0;
}
