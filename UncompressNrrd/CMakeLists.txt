cmake_minimum_required(VERSION 2.8)

PROJECT(UNCOMPRESS_NRRD)
add_subdirectory(zstr)
add_executable(UncompressData uncompress_data.cpp)
target_link_libraries(UncompressData PRIVATE zstr::zstr)