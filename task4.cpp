#include <iostream>

void divisionintodivisors(int n){
	std::cout << n << " = ";
	while (n % 2 == 0) {
		std::cout << 2 << " ";
		n /= 2;
	}
	for (int i = 3; i * i <= n; i += 2) {
		while(n % i == 0) {
			std::cout << i << " ";
			n /= i;
		}
	}
	if(n > 1) {
		std::cout << n;
	}
	std::cout << "/n";
}
int main(){
	int n;
	std::cout << "enter number";
	std::cin >> n;
	divisionintodivisors(n);
	return 0;
}
