# Creating a Gazebo World with Random Objects and Mapping with TurtleBot3 in ROS2


## Prerequisites
- Install ROS2.
- Install TurtleBot3 packages.
- Install Gazebo simulation environment.


Follow the instrustions provided in this link to download Turtlebot3:

https://emanual.robotis.com/docs/en/platform/turtlebot3/simulation/#gazebo-simulation

Once you create the workspace and follow the PC setup instructions run the following commands to open the turtlebot3 robot in gazebo:

$export TURTLEBOT3_MODEL=burger

$roslaunch turtlebot3_gazebo turtlebot3_empty_world.launch

To list all environment variables just type $env
 
To search for a specific environment variable pipe the output to grep by $env|grep "TURTLE"

By running the following command u can make the turtlebot model into a model equipped with camera and simulation world:

$ export TURTLEBOT3_MODEL=waffle
$ roslaunch turtlebot3_gazebo turtlebot3_world.launch


