#include <iostream>

int BinaryToDecimial(long long binary) {
	int decimial = 0, base = 1, digit;
	while(binary > 0) {
		digit = binary % 10;
		decimial += digit * base;
		base *= 2;
		binary /= 10;
	}
	return decimial;
}
int main() {
	long long binaries[] = {11001, 11100111, 111000};
	for(int i = 0; i < 3; i++) {
		std::cout << "Binary: " << binaries[i] << " => Decimal: " << BinaryToDecimial(binaries[i]) << std::endl;
	}
	return 0;
}
