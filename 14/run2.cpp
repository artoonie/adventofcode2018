#include <iostream>
#include <cstdlib>
#include <vector>

inline bool chk(const std::vector<char>& rec) {
    size_t size = rec.size();
    bool is = rec[size-1] == 1 && rec[size-2] == 4 && rec[size-3] == 6 && rec[size-4] == 0 && rec[size-5] == 7 && rec[size-6] == 1;
    if(is) std::cout << rec.size()-6 << std::endl;
    return is;
}

int main() {
std::vector<char> rec;
rec.push_back(3);
rec.push_back(7);

size_t elf0 = 0;
size_t elf1 = 1;
size_t tic = 0;

size_t size = 0;
while(true) {
    char v = rec[elf0] + rec[elf1];
    if(v >= 10) {
        rec.push_back(v/10);
        if(chk(rec)) break;
    }
    rec.push_back(v % 10);

    size = rec.size();
    elf0 = (elf0 + rec[elf0] + 1) % size;
    elf1 = (elf1 + rec[elf1] + 1) % size;
    if(chk(rec)) {
        break;
    }
    tic++;
    if(tic == 0)
        std::cout << "DEAD" << std::endl;
}
}
