#include <iostream>

int HexCharToValue(char ch) {
	if (ch >= '0' && ch <= '9')
		return  ch - '0';
	if (ch >= 'A' && ch <= 'F')
		return 10 + (ch - 'A');
	if (ch >= 'a' && ch <= 'f')
		return 10 + (ch - 'a');
	return -1;
}
int HexToDecimal(const char hex[]) {
	int result = 0;
	int i = 0;
	while (hex[i] != '\0') i++;
	int power = 1;
	for (int j = i - 1; j >= 0; j--) {
		int digit = HexCharToValue(hex[j]);
		if(digit == -1) {
			std::cout << "Wrong symbol in number: " << hex[j] << std::endl;
			return -1;
		}
		result += digit * power;
		power *= 16;
	}
	return result;
}
int main(){
	const char* HexNums[] = {"1FF", "94", "FF"};
	for(int i = 0; i < 3; i++) {
		std::cout << "Hex: " << HexNums[i] << " => Decimial: " << HexToDecimal(HexNums[i]) << std::endl;
	}
	return 0;
}
