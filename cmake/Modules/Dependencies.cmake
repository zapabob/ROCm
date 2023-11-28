# MIT License
#
# Copyright (c) 2023 Advanced Micro Devices, Inc. All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# ###########################
# ROCm dependencies
# ###########################

include(FetchContent)

if(ROCM_BUILD_DOCS)
  find_package(ROCM 0.11.0 CONFIG QUIET PATHS "${ROCM_PATH}") # First version with Sphinx doc gen improvement
  if(NOT ROCM_FOUND)
    message(STATUS "ROCm CMake not found. Fetching...")
    set(rocm_cmake_tag
      "c044bb52ba85058d28afe2313be98d9fed02e293" # develop@2023.09.12. (move to 6.0 tag when released)
      CACHE STRING "rocm-cmake tag to download")
    FetchContent_Declare(
      rocm-cmake
      GIT_REPOSITORY https://github.com/RadeonOpenCompute/rocm-cmake.git
      GIT_TAG        ${rocm_cmake_tag}
      SOURCE_SUBDIR "DISABLE ADDING TO BUILD" # We don't really want to consume the build and test targets of ROCm CMake.
    )
    FetchContent_MakeAvailable(rocm-cmake)
    find_package(ROCM CONFIG REQUIRED NO_DEFAULT_PATH PATHS "${rocm-cmake_SOURCE_DIR}")
  else()
    find_package(ROCM 0.11.0 CONFIG REQUIRED PATHS "${ROCM_PATH}")
  endif()

  if(Python_FIND_VIRTUALENV STREQUAL "ONLY" AND NOT DEFINED ENV{VIRTUAL_ENV})
    if(NOT EXISTS "${CMAKE_CURRENT_BINARY_DIR}/.venv")
      message(STATUS "Python virtualenv use requested but not found. Fetching...")
      find_program(BOOTSTRAP_PYTHON_EXE python3 REQUIRED)
      execute_process(
        COMMAND "${BOOTSTRAP_PYTHON_EXE}" -m pip install --user virtualenv
        OUTPUT_QUIET
        COMMAND_ERROR_IS_FATAL ANY
      )
      execute_process(
        COMMAND "${BOOTSTRAP_PYTHON_EXE}" -m virtualenv "${CMAKE_CURRENT_BINARY_DIR}/.venv"
        OUTPUT_QUIET
        COMMAND_ERROR_IS_FATAL ANY
      )
    endif()
    set(ENV{VIRTUAL_ENV} "${CMAKE_CURRENT_BINARY_DIR}/.venv")
    
    if(WIN32)
      set(ENV{PATH} "${CMAKE_CURRENT_BINARY_DIR}/.venv/Scripts;$ENV{PATH}")
    else()
      set(ENV{PATH} "${CMAKE_CURRENT_BINARY_DIR}/.venv/bin:$ENV{PATH}")
    endif()
    
    find_package(Python REQUIRED)

    # TODO: shortcircuit if installed
    execute_process(
      COMMAND "${Python_EXECUTABLE}" -m pip install pip-tools
      OUTPUT_QUIET
      COMMAND_ERROR_IS_FATAL ANY
    )

    list(APPEND CMAKE_CONFIGURE_DEPENDS "${PROJECT_SOURCE_DIR}/docs/sphinx/requirements.in")
    file(MAKE_DIRECTORY "$ENV{VIRTUAL_ENV}/usr/share/${PROJECT_NAME}")
    if("${PROJECT_SOURCE_DIR}/docs/sphinx/requirements.in" IS_NEWER_THAN "$ENV{VIRTUAL_ENV}/usr/share/${PROJECT_NAME}/requirements.txt")
      execute_process(
        COMMAND "${Python_EXECUTABLE}" -m piptools compile
          "${PROJECT_SOURCE_DIR}/docs/sphinx/requirements.in"
          --output-file
          "$ENV{VIRTUAL_ENV}/usr/share/${PROJECT_NAME}/requirements.txt"
        OUTPUT_QUIET
        ERROR_QUIET
        COMMAND_ERROR_IS_FATAL ANY
      )
      execute_process(
        COMMAND "${Python_EXECUTABLE}" -m piptools sync
          "$ENV{VIRTUAL_ENV}/usr/share/${PROJECT_NAME}/requirements.txt"
        OUTPUT_QUIET
        ERROR_QUIET
        COMMAND_ERROR_IS_FATAL ANY
      )
    endif()
  endif()
endif()
