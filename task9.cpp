#include <iostream>

void hide_message(char* text, const char* message);
void extract_message(const char* text);
int main() {
	char text[500] = "This message used to hide information.";
	char message[50] = "No";
	std::cout << "Original text:\n" << text << std::endl;

	hide_message(text, message);
	extract_message(text);

	return 0;
}
void hide_message(char* text, const char* message) {
	int i = 0, j = 0, bit_index = 7;
	char modified_text[1000];
	int mod_index = 0;

	while (text[i] != '\0' ) {
		modified_text[mod_index++] = text[i];

		if (text[i] == ' ' && message[j] != '\0' ) {
			int bit = (message[j] >> bit_index) & 1;
			if (bit == 1) {
				modified_text[mod_index++] = ' ';
			}
			if (bit_index == 0) {
				bit_index = 7;
				j++;
			} else {
				bit_index--;
			}
		}
		i++;
	}
	modified_text[mod_index] = '\0';
	std::cout << "Text after hiding:\n" << modified_text << std::endl;
}
void extract_message(const char* text) {
	int i = 0, bit_index = 7, j = 0;
	char extracted_message[100];
	char current_char = 0;
	int space_count = 0;
	bool space_found = false;

	while (text[i] != '\0') {
		if (text[i] == ' ') {
			if (!space_found) {
				space_count = 1;
				space_found = true;
			} else {
				space_count++;
			}
		} else {
			if (space_found) {
				int bit = (space_count == 2) ? 1 : 0;
				current_char |= (bit << bit_index);

				if (bit_index == 0) {
					extracted_message[j++] = current_char;
					current_char = 0;
					bit_index = 7;
				} else {
					bit_index--;
				}
				space_found = false;
			}
		}
		i++;
	}
	extracted_message[j] = '\0';
	std::cout << "Extracted message: " << extracted_message << std::endl;
}
