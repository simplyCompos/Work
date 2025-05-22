#include <iostream>

double sqrtApprox(double num) {
	double x = num;
	double prev = 0;
	double eps = 0.00001;
	if(num < 0) return -1;
	while((x - prev > eps) || (prev - x > eps)) { 
		prev = x;
		x = (x + num / x) / 2;
	}
	return x;
}
int main() {
	double a, b, c;
	char repeat;
	do {
		std::cout << " Enter coefficients a, b, c: ";
		std::cin >> a >> b >> c;
		double D = b * b - 4 * a * c;
		std::cout << "Discriminant D = " << D << std::endl;
		if (D > 0) {
			double sqrtD = sqrtApprox(D);
			double x1 = (-b + sqrtD) / (2 * a);
			double x2 = (-b - sqrtD) / (2 * a);
			std::cout << "Two roots: x1 = " << x1 << ", x2 = " << x2 << std::endl;
		} else if (D == 0) {
			double x = -b / (2 * a);
			std::cout << "One root: x = " << x << std::endl;
		} else {
			std::cout << "There are no solutions(roots not valid)." << std::endl;
		}
		std::cout << "\nRepeat (y/n)? ";
		std::cin >> repeat;
	} while (repeat == 'y' || repeat == 'Y');
	return 0;
}
