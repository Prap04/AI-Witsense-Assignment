
# UGV based Robotics Solution 
This repository contains the solution for an autonomous Unmanned Ground Vehicle (UGV) that integrates sensor data, object detection, and navigation in a simulated environment using ROS 2 and Gazebo. The solution demonstrates how to work with ROS 2 nodes, sensors, and simulation tools for autonomous robot control.

Installation:

1. Ubuntu 22.04 on your Virtual Machine or WSL
   
https://automaticaddison.com/how-to-install-ubuntu-22-04-virtual-machine-on-a-windows-pc/

3. ROS 2 Humble on Ubuntu 22.04
https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debs.html

4. Publisher node code and Subsrciber node code is provided in the main branch this is how it would look on the temrinal.
It Generates random floating-point numbers in the range [0, 1] and publishes the values to the topic sensor_x_readings whereas the Subscriber subscribes to the sensor_x_readings topic.

## Screenshots


Terminal Output Example
Publisher Node:

![publish ](https://github.com/user-attachments/assets/9cb448c5-b420-4f3f-8b59-8274f308e898)


Subsrciber Node:

![subscribe ](https://github.com/user-attachments/assets/8f13d96f-226d-4272-b9c2-0de5c891834f)


Data Publishing on same topic:

![topic](https://github.com/user-attachments/assets/e9b6912c-f688-4656-a9cc-cc1cb9bf0cce)



TurtleBot3 Simulation Guide:
https://emanual.robotis.com/docs/en/platform/turtlebot3/simulation/

Turtle Bot3 Slam Guide:
https://emanual.robotis.com/docs/en/platform/turtlebot3/slam/#run-slam-node



