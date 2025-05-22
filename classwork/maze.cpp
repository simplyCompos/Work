#include <iostream>
#include <vector>
using field = std::vector<std::vector<char> >;

std::ostream& operator<<(std::ostream& out, field& map);
std::istream& operator>>(std::istream& in, field& map);

int main()
{
	field map = {{'X', ' ', 'X'}, {' ', 'X', ' '}};
	std::cin >> map;
	std::cout << map << std::endl;
	return 0;
}

std::ostream& operator<<(std::ostream& out, field& map)
{
	for(auto i = map.begin(); i != map.end(); i++){
		for(auto j = i->begin(); j != i->end(); j++)
			out << *j;
		out << std::endl;
	}
	return out;
}

std::istream& operator>>(std::istream& in, field& map);
{
	char ch;
	while(in.get(ch))
	{

	}
	return in;
}
