#include <iostream>
#include <cstdlib>
#include <vector>

int main() {
std::vector<char> rec;
rec.push_back(3);
rec.push_back(7);

unsigned long long int elf0 = 0;
unsigned long long int elf1 = 1;
unsigned long long int tic = 0;

unsigned long long int size = 0;
while(true) {
    char v = rec[elf0] + rec[elf1];
    if(v >= 10)
        rec.push_back(v/10);
    rec.push_back(v % 10);

    size = rec.size();
    elf0 = (elf0 + rec[elf0] + 1) % size;
    elf1 = (elf1 + rec[elf1] + 1) % size;
    if(rec[size-1] == 1 && rec[size-2] == 4 && rec[size-3] == 6 && rec[size-4] == 0 && rec[size-5] == 7 && rec[size-6] == 1) {
        std::cout << rec.size()-6 << std::endl;
        break;
    }
    tic++;
    if(tic == 0)
        std::cout << "DEAD" << std::endl;
}
}
