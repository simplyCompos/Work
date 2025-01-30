#include <iostream>

void findTriples(int n) {
	for (int a = 1; a <= n; ++a) {
		for (int b = a; b <= n; ++b) {
	int c2 = a * a + b * b;
	int c = 1;
	while (c * c < c2) {
		++c;
	}
	if (c * c == c2 && c <= n) {
	std::cout << "(" << a << ", " << b << ", " << c << ")\n" ;
	}
      }
    }
  }
 int main() {
	int n = 100;
	findTriples(n);
	return 0;
}
