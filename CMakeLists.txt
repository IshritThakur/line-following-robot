cmake_minimum_required(VERSION 3.5)
project(line_follower)

# Find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)

# Install setup.py as an executable
install(PROGRAMS
  setup.py
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
