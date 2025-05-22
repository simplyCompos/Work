#include <iostream>

void toBinary(int num) {
	int binary[32];
	int i = 0;

	while (num > 0) {
		binary[i] = num % 2;
		num = num / 2;
		i++;
	}
	std::cout << "Binary: ";
	for(int j = i - 1; j >= 0; j--) {
		std::cout << binary[j];
	}
	std::cout << std::endl;
}

void toHex(int num) {
	char HexDigits[] = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'};
	char hex[32];
	int i = 0;
	while (num > 0) {
		hex[i] = HexDigits[num % 16];
		num = num / 16;
		i++;
	}
	std::cout << "Hex: ";
	for(int j = i - 1; j >= 0; j--) {
		std::cout << hex[j];
	}
	std::cout << std::endl;
}

int main() {
	int nums[] = {255, 1024, 364};
	for(int i = 0; i < 3; i++) {
		std::cout << "Decimal: " << nums[i] << std::endl;
		toBinary(nums[i]);
		toHex(nums[i]);
		std::cout << "---------" << std::endl;
	}
	return 0;
}
