#include <iostream>

void PascalTriangle(int n)
{
	for(int i = 0; i < n; ++i)
	{
		int value = 1;
	       for (int	j = 0; j <= i; ++j){
		 std::cout << value << " ";
		 value = value * (i - j) / (j + 1);
	       }
	      std::cout << "\n";
	 }
}

int main() {
	int n = 25;
	PascalTriangle(n);
	return 0;
}
