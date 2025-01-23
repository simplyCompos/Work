#include <iostream>
using namespace std;

int main(){
	int a = 0, b = 12, c = 3;

	bool result = (b = a + c) && (c = b * 2) || (a = b - c);

	cout << "Result: " << result << endl;
	cout << "a: " << a << ", b: " << b << ", c: " << c << endl;

	return 0;
}
