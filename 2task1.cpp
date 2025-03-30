#include <iostream>

int main() {
	int n;
        std::cout << "Enter number n: " << std::endl;
        std::cin >> n;
	if (n < 0) {
		std::cout << "Enter number n: " << std::endl;
		std::cin >> n;
	}
        int d;
	std::cout << "Enter deleted number d: " << std::endl;
	std::cin >> d;
        int result = 0, j = 1;
        while (n > 0) {
        int f = n % 10;
        if (f != d){
                result = result + f * j;
                j *= 10;
                }
        n /= 10;
        }
        std::cout << result;
}
