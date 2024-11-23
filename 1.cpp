#include <iostream>

int main(){
	int number;
	number = 12;

	int & number_r = number;
	number_r = 15;
	std::cout << "number_r " << number_r << std::endl;
	std::cout << "number " << number << std::endl;
	std::cout << "&number: " << &number << std::endl;
	return 0;
}
