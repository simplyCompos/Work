#include <iostream>

using namespace std;

int main() {
	int a = 3, b = 8, c = 0;

	bool result = (a < b & 8 + c < 1 ) || (b > a || -c > -1);

	cout << "Result: " << result << endl;
	cout << "c: " << c << endl;

	return 0;
}
