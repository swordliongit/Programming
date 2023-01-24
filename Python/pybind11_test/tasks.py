# tasks.py
import invoke

invoke.run(
    "g++ -O3 -Wall -Werror -shared -std=c++11 -fPIC cppmult.cpp "
    "-o libcppmult.so "
)