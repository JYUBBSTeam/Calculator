# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.14

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /home/h/JetBrains/clion-2019.1.2/bin/cmake/linux/bin/cmake

# The command to remove a file.
RM = /home/h/JetBrains/clion-2019.1.2/bin/cmake/linux/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/h/Project/Calculator/ComputingLibrary/test/testCACLFloat

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/h/Project/Calculator/ComputingLibrary/test/testCACLFloat/cmake-build-debug

# Include any dependencies generated for this target.
include CMakeFiles/testCACLFloat.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/testCACLFloat.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/testCACLFloat.dir/flags.make

CMakeFiles/testCACLFloat.dir/test.cpp.o: CMakeFiles/testCACLFloat.dir/flags.make
CMakeFiles/testCACLFloat.dir/test.cpp.o: ../test.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/h/Project/Calculator/ComputingLibrary/test/testCACLFloat/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/testCACLFloat.dir/test.cpp.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/testCACLFloat.dir/test.cpp.o -c /home/h/Project/Calculator/ComputingLibrary/test/testCACLFloat/test.cpp

CMakeFiles/testCACLFloat.dir/test.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/testCACLFloat.dir/test.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/h/Project/Calculator/ComputingLibrary/test/testCACLFloat/test.cpp > CMakeFiles/testCACLFloat.dir/test.cpp.i

CMakeFiles/testCACLFloat.dir/test.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/testCACLFloat.dir/test.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/h/Project/Calculator/ComputingLibrary/test/testCACLFloat/test.cpp -o CMakeFiles/testCACLFloat.dir/test.cpp.s

CMakeFiles/testCACLFloat.dir/home/h/Project/Calculator/ComputingLibrary/CACLFloat/IO.cpp.o: CMakeFiles/testCACLFloat.dir/flags.make
CMakeFiles/testCACLFloat.dir/home/h/Project/Calculator/ComputingLibrary/CACLFloat/IO.cpp.o: /home/h/Project/Calculator/ComputingLibrary/CACLFloat/IO.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/h/Project/Calculator/ComputingLibrary/test/testCACLFloat/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building CXX object CMakeFiles/testCACLFloat.dir/home/h/Project/Calculator/ComputingLibrary/CACLFloat/IO.cpp.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/testCACLFloat.dir/home/h/Project/Calculator/ComputingLibrary/CACLFloat/IO.cpp.o -c /home/h/Project/Calculator/ComputingLibrary/CACLFloat/IO.cpp

CMakeFiles/testCACLFloat.dir/home/h/Project/Calculator/ComputingLibrary/CACLFloat/IO.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/testCACLFloat.dir/home/h/Project/Calculator/ComputingLibrary/CACLFloat/IO.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /home/h/Project/Calculator/ComputingLibrary/CACLFloat/IO.cpp > CMakeFiles/testCACLFloat.dir/home/h/Project/Calculator/ComputingLibrary/CACLFloat/IO.cpp.i

CMakeFiles/testCACLFloat.dir/home/h/Project/Calculator/ComputingLibrary/CACLFloat/IO.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/testCACLFloat.dir/home/h/Project/Calculator/ComputingLibrary/CACLFloat/IO.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /home/h/Project/Calculator/ComputingLibrary/CACLFloat/IO.cpp -o CMakeFiles/testCACLFloat.dir/home/h/Project/Calculator/ComputingLibrary/CACLFloat/IO.cpp.s

# Object files for target testCACLFloat
testCACLFloat_OBJECTS = \
"CMakeFiles/testCACLFloat.dir/test.cpp.o" \
"CMakeFiles/testCACLFloat.dir/home/h/Project/Calculator/ComputingLibrary/CACLFloat/IO.cpp.o"

# External object files for target testCACLFloat
testCACLFloat_EXTERNAL_OBJECTS =

testCACLFloat: CMakeFiles/testCACLFloat.dir/test.cpp.o
testCACLFloat: CMakeFiles/testCACLFloat.dir/home/h/Project/Calculator/ComputingLibrary/CACLFloat/IO.cpp.o
testCACLFloat: CMakeFiles/testCACLFloat.dir/build.make
testCACLFloat: CMakeFiles/testCACLFloat.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/h/Project/Calculator/ComputingLibrary/test/testCACLFloat/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Linking CXX executable testCACLFloat"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/testCACLFloat.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/testCACLFloat.dir/build: testCACLFloat

.PHONY : CMakeFiles/testCACLFloat.dir/build

CMakeFiles/testCACLFloat.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/testCACLFloat.dir/cmake_clean.cmake
.PHONY : CMakeFiles/testCACLFloat.dir/clean

CMakeFiles/testCACLFloat.dir/depend:
	cd /home/h/Project/Calculator/ComputingLibrary/test/testCACLFloat/cmake-build-debug && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/h/Project/Calculator/ComputingLibrary/test/testCACLFloat /home/h/Project/Calculator/ComputingLibrary/test/testCACLFloat /home/h/Project/Calculator/ComputingLibrary/test/testCACLFloat/cmake-build-debug /home/h/Project/Calculator/ComputingLibrary/test/testCACLFloat/cmake-build-debug /home/h/Project/Calculator/ComputingLibrary/test/testCACLFloat/cmake-build-debug/CMakeFiles/testCACLFloat.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/testCACLFloat.dir/depend

