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

## Run

* Start environment
```
roslaunch sauvc_gazebo sauvc_gazebo.launch
```

* Start a new terminal, then upload robot to gazebo
```
roslaunch bubbles_description upload_bubbles.launch
```

* To reset world, use: `rosservice call /gazebo/reset_world`

## Ros nodes

You may want to use following ros nodes

* thrusters(index in range(0, 4)): /bubbles/thrusters/{index}/input
* IMU: /bubbles/imu
* pressure sensor: /bubbles/pressure
* camera: /bubbles/bubbles/camera/camera_image

![Screenshot](https://user-images.githubusercontent.com/10456378/69312063-e2d58e80-0c68-11ea-8e10-3f172c2f5799.png)

