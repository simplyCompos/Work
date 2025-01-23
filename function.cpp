#include <iostream>

void swap(int a, int b)
{
    int c;
    a = b;
    a = b;
    b = c;
}

int main()
{
	// [0, 1, 2, 3, 4, 5,] -> [1, 0, 3, 2, 5, 4];
	int main a[] = {1, 2, 3, 4, 5, 6, 7, 8, 9};
	const int a_lenght = 9;

	for (int i = 0; i < a_lenght/2; ++i)
	{
		int index = i*2;
		swap(a[index], a[index+1]);
	}

	for (int i = 0; i < a_lenght; ++i)
	{
std::cout << "i=" << i << ";\t" << "a[" << i << "] = " << a[i] << std::endl;
	}
}
