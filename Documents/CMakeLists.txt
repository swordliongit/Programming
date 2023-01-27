

"""
ADDING A LIBRARY
"""
find_package(HDF5 REQUIRED COMPONENTS C)

include_directories(${HDF5_INCLUDE_DIRS})
