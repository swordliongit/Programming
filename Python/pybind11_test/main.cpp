// pybind11_wrapper.cpp
#include <pybind11/pybind11.h>
// #include <C:/Users/SWORD/AppData/Local/Programs/Python/Python311/Lib/site-packages/pybind11/include/pybind11/pybind11.h>
// #include <cppmult.hpp>
#include "test.cpp"

namespace py = pybind11;

PYBIND11_MODULE(module_name, handle) {
    handle.doc() = "pybind11 example plugin"; // Optional module docstring
    handle.def("cpp_function", &cppmult);
}