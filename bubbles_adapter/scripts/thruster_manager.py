#!/usr/bin/env python3

import numpy as np
from typing import Sequence

import rospy
from geometry_msgs.msg import Twist
from uuv_gazebo_ros_plugins_msgs.msg import FloatStamped


class Thruster:
    def __init__(self, node_name: str):
        self.pub = rospy.Publisher(node_name + '/input', FloatStamped, queue_size=10)

    def publish(self, value: float):
        output = FloatStamped()
        output.header.stamp = rospy.Time.now()
        output.data = value
        self.pub.publish(output)


class ThrusterManagerNode:
    def __init__(self):
        self.node_name = 'thruster_manager'
        rospy.init_node(self.node_name)

        self.tranform_matrix = np.array([
            # x  y   z roll pitch yaw
            [0,  0,  1,  1, -1,  0],  # left front motor
            [0,  0,  1, -1, -1,  0],  # right front motor
            [1,  0,  0,  0,  0,  0],  # left rear motor
            [1,  0,  0,  0,  0,  1],  # right rear motor
            [0,  0,  1,  0,  1, -1]   # rear motor
        ])
        self.scale = 10
        self.num_thrusters = len(self.tranform_matrix)
        self.thrusters = [Thruster(f'thrusters/{i}') for i in range(self.num_thrusters)]

        rospy.Subscriber(self.node_name + '/input', Twist, self.input_callback)

        rospy.loginfo("ThrusterManagerNode started")

    def input_callback(self, msg: Twist):
        control_vector = np.array([
            [msg.linear.x], [msg.linear.y], [msg.linear.z],
            [msg.angular.x], [msg.angular.y], [msg.angular.z]
        ])
        output = self.scale * self.tranform_matrix @ control_vector
        self.update_thrusters(output)

    def update_thrusters(self, output: Sequence[float]):
        for i in range(self.num_thrusters):
            self.thrusters[i].publish(output[i])


if __name__ == '__main__':
    ThrusterManagerNode()
    rospy.spin()
