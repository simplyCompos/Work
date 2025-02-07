#include <iostream>

bool isPalindrom(int num) {
	int reserved = 0, original = num;
	while(num > 0) {
		int digit = num % 10;
		reserved = reserved * 10 + digit;
		num /= 10;
	}
	return original == reserved;
}

void findPalindroms() {
	for (int i = 1; i <= 100; ++i) {
		if (isPalindrom(i) && i > 9) {
			int square = i * i;
			if (isPalindrom(square)){
				std::cout << i << "^2 = " << square << std::endl;
			}
		}
	}
}
int main() {
	findPalindroms();
	return 0;
}
