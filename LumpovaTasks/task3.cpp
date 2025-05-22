#include <iostream>
#include <iomanip>

int global = 25;
double sqrtApprox(double num) {
	double x = num;
	double prev = 0;
	double eps = 0.00001;
	if(num < 0) return -1;
	while((x - prev > eps) || (prev - x >eps)) {
		prev = x;
		x = (x + num / x) / 2;
	}
	return x;
}
int main() {
	int x;
	double y = 10.0;
	std::cout << "Enter x: ";
	std::cin >> x;
	std::cout << "to calculation: x=" << x << ", y=" << y << std::endl;
	double z1 = x + y;
	double z2 = x * y;
	double z3 = (x != 0) ? y / x : 0;
	std::cout << "\nResults\n";
	std::cout << " 1     2      3\n";
	std::cout << fixed << setprecision(2);
	std::cout << setw(7) << z1 << setw(7) << z2 << setw(7) << z3 << std::endl;
	return 0;
}
