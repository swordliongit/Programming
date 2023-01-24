# tasks.py
import invoke

invoke.run(
    "g++ -O3 -Wall -Werror -shared -std=c++11 -fPIC "
    "`python3 -m pybind11 --includes` "
    "-I /usr/include/python3.7 -I .  "
    "{0} "
    "-o {1}`python3.7-config --extension-suffix` "
    "-L. -lcppmult -Wl,-rpath,.".format("pybind11_wrapper", "cpp")
)