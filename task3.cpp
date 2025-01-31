#include <iostream>

void resheto(int n){
	int resheto[1001] = {0};
	for (int i = 2; i * i <= n; ++i) {
		if (resheto[i] == 0) {
			for (int j = i * i; j <= n; j += i){
				resheto[j] = 1;
			}
		}
	}
	for (int i = 2; i <= n; ++i) {
		if (resheto[i] == 0) {
			std::cout << i << " ";
		}
	}
	std::cout << "\n";
 }

int main() {
	int n = 1000;
	resheto(n);
	return 0;
 }
