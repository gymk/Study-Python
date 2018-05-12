#include <iostream>
#include <fstream>
#include <stdlib.h>

using namespace std;

int main(int argc, char * argv[])
{
	int seed = atoi(argv[2]);
	int count = atoi(argv[3]);
	int v;
	ofstream out(argv[1]);

	cout << "Seed: " << seed << " count: " << count << " OutputFile: " << argv[1] << endl;

	srand(seed);

	for(int i = 0; i < count; i++)
	{
		v = rand();
		out << v << endl;
	}
}
