#include <iostream>

bool isTwins(int num) {
	if (num < 2) return false;
	for (int i = 2; i * i <= num; ++i) {
		if (num % i == 0) {
			return false;
		}
	}
	return true;
}
void findTwins(int n) {
	for (int i = n; i <= 2 * n - 2; ++i) {
		if (isTwins(i) && isTwins(i + 2)) {
			std::cout << "(" << i << ", " << i + 2 << ")" << std::endl;
		}
	}
}
int main() { 
	int n;
	std::cout << "Enter number n: ";
		std::cin >> n;
	if (n > 0) {
		std::cout << "Twins of simple numbers whis difference of 2 between" << n << " and " << 2 * n << ":" << std::endl;
		findTwins(n);
	} else {
		std::cout << "n must be more that 0!" << std::endl;
	}
	return 0;
}
