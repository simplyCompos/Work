#include <iostream>

void printNumbersinwords(int n) {
	const char* ones[] = {"", "one", "two", "three", "four", "five","six", "seven", "eight", "nine"};
	const char* tens[] = {"", "ten", "twenty", "thirdty", "fourty", "fifty", "sixty", "seventy", "eighty", "ninety"};
	const char* teens[] = {"ten", "eleven", "tvelv", "therteen", "fourteen", "fiveteen", "sixteen", "seventeen", "eighteen", "nineteen"};
	const char* hundreds[] = {"", "one hundred", "two hundreds", "three hundreds", "four hundreds", "five hundreds", "six hundreds", "seven hundreds", "eight hundreds", "nine hundreds"};
	int h = n / 100;
	int t = (n / 10) % 10;
	int o = n % 10;
	if (h > 0) {
		std::cout << hundreds[h] << " ";
	}
	if (t == 1) {
		std::cout << teens[t] << " ";
	} else {
	if (t > 1) {
		std::cout << tens[t] << " ";
	}
	if (o > 1) {
		std::cout << ones[o];
	}	
	}
	std::cout << std::endl;
}

int main() {
	int n;
	std::cout << "Enter number (not more that 1000): ";
	std::cin >> n;

	if(n < 1 || n > 1000) {
		std::cout << "Number must be higer that 1 and or equal 1000!" << std::endl;
	}
	else if (n == 1000) {
		std::cout << "thousan" << std::endl;
	}
	else {printNumbersinwords(n);
	}
	return 0;
}

