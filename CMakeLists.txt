cmake_minimum_required(VERSION 3.5)
project(line_follower)

# Find dependencies
find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)
find_package(rclpy REQUIRED)

# Install the python package.
ament_python_install_package(${PROJECT_NAME})

# Optionally install the resource directory if needed.
install(
  DIRECTORY resource/
  DESTINATION share/${PROJECT_NAME}
)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
