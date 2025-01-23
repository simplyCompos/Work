#include <iostream>
using namespace std;

int main(){
	int x = 10, y = 6, z = 4;

	int result = x * y - y / z + x % z;

	cout << "Result: " << result << endl;

	return 0;
}
