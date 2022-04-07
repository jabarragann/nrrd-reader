#include <fstream>
#include <iostream>
#include "zstr.hpp"

using namespace std;

int main()
{
    // Open file in read mode
    string filename = "Segmentation_LT_144.seg.nrrd";
    ifstream file;
    file.open("./../../sample_volumes/" + filename);

    if (!file || !file.good())
    {
        std::cerr << "NRRD::parseHeader<T>(...): File access error.\n";
        return 0;
    }

    printf("Printing header .... \n");
    int line_num = -1;
    int header_offset;
    while (!file.eof() && file.good())
    {
        line_num++;
        string line, key, value;
        getline(file, line);
        printf("%s\n", line.c_str());

        header_offset = (int)file.tellg();
        if (line.empty()) // beginning of data chunk
            break;
        if (line[0] == '#') // comment
            continue;
    }
    printf("header offset: %d\n", header_offset);
    printf("line offset: %d\n", line_num);

    // Get gzip magic number
    // Check https://github.com/mateidavid/zstr
    unsigned char magic_number[2];
    file.read((char *)&magic_number, sizeof(char) * 2);
    printf("gzip magic numbers: %02x%02x\n", magic_number[0] & 0xff, magic_number[1] & 0xff);
    file.seekg(-2, ios::cur);

    zstr::istream raw_file(file);

    unsigned char pixels[10];
    file.read((char *)&pixels, sizeof(char) * 10);
    for (unsigned char n : pixels)
        std::cout << n << ' ' << endl;
}