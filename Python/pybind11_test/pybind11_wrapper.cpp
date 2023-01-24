// pybind11_wrapper.cpp
#include <pybind11/pybind11.h>
// #include <C:/Users/SWORD/AppData/Local/Programs/Python/Python311/Lib/site-packages/pybind11/include/pybind11/pybind11.h>
#include "cppmult.cpp"

PYBIND11_MODULE(pybind11_example, m) {
    m.doc() = "pybind11 example plugin"; // Optional module docstring
    m.def("cpp_function", &cppmult, "A function that multiplies two numbers");
}