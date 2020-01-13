# SAUVC Simulator

## Installation

* Install ROS (desktop full)
* Install uuv simulator: https://uuvsimulator.github.io/installation/
* Create catkin workspace (skip if already created): http://wiki.ros.org/catkin/Tutorials/create_a_workspace
* Clone this project to your catkin workspace
```
cd ~/catkin_ws/src
git clone https://github.com/heyuhang0/sauvc_simulator.git
```

* Then build your workspace
```
cd ~/catkin_ws
catkin_make
```

* Install other dependencies
```
# install numpy for python3
# install pip3: sudo apt install python3-pip
pip3 install numpy
pip3 install rospkg
```

## Run

* Start environment (year argument to select year)
```
roslaunch sauvc_gazebo sauvc_gazebo.launch year:=2020
```

* Start a new terminal, then upload robot to gazebo
```
roslaunch bubbles_description upload_bubbles.launch
```

* To reset world, use: `rosservice call /gazebo/reset_world`

* To try basic joystick teleop (without PID): `roslaunch bubbles_adapter basic_teleop.launch`

## Ros topics

You may want to use following ros topics

* thruster_manager: geometry_msgs/Twist -> /bubbles/thruster_manager/input
* thrusters(index in range(0, 4)): uuv_gazebo_ros_plugins_msgs/FloatStamped -> /bubbles/thrusters/{index}/input
* IMU: /bubbles/imu -> sensor_msgs/Imu
* pressure sensor: /bubbles/pressure -> sensor_msgs/FluidPressure
* camera: /bubbles/bubbles/camera/camera_image -> sensor_msgs/Image
* bottom camera: /bubbles/bubbles/camera_bottom/camera_image -> sensor_msgs/Image

![Screenshot](https://user-images.githubusercontent.com/10456378/69312063-e2d58e80-0c68-11ea-8e10-3f172c2f5799.png)

