cmake_minimum_required(VERSION 2.8.3)
project(bubbles_description)

find_package(catkin REQUIRED)

catkin_package()

install(DIRECTORY mesh robots urdf launch
        DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
        PATTERN "*~" EXCLUDE)
