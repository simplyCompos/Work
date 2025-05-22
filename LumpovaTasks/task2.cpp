#include <iostream>

const int MaxSubjects = 3;
struct Student {
	int code;
	char surname[20];
	char name[20];
	int grades[MaxSubjects];
};
struct Teacher {
	int code;
	char surname[20];
        char name[20];
        int subjects[MaxSubjects];
};
int main() {
	Student s1;
	Teacher t1;
	std::cout << "Enter student code: ";
	std::cin >> s1.code;
	std::cout << "Student surname: ";
	std::cin >> s1.surname;
	std::cout << "Student name: ";
	std::cin >> s1.name;
	for(int i = 0; i < MaxSubjects; i++) {
		std::cout << "Grade from subject " << i + 1 << ": ";
		std::cin >> s1.grades[i];
	}
	std::cout << "\nInformation about student:\n";
	std::cout << "Code: " << s1.code << ", Surname: " << s1.surname << "Name: " << s1.name << std::endl;
	std::cout << "Grades: ";
	for(int i = 0; i < MaxSubjects; i++) {
		std::cout << s1.grades[i] << " ";
	}
	std::cout << std::endl;
	std::cout << "\nEnter teacher code: ";
	std::cin >> t1.code;
	std::cout << "Teacher surname: ";
	std::cin >> t1.surname;
	std::cout << "Teacher name: ";
	std::cin >> t1.name;
	for(int i = 0; i < MaxSubjects; i++) {
	std::cout << "Subject code: " << i + 1 << ": ";
	std::cin >>t1.subjects[i];
	}
	std::cout << "\nInformation about teacher:\n";
	std::cout << "Code " << t1.code << ", surname: " << t1.surname << ", name: " << t1.name << std::endl;
	std::cout << "Subjects codes: ";
	for(int i = 0; i < MaxSubjects; i++) {
		std::cout << t1.subjects[i] << " ";
	}
	std::cout << std::endl;
	return 0;
}
