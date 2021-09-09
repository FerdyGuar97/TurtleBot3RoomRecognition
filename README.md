# TurtleBot Navigation and Detection

### Authors: Group 14

| Name | Student ID |
|--------------|--------|
|Vincenzo di Somma | 0622701283|
|Salvatore Gravina | 0622701063|
|Ferdinando Guarino | 0622701321|

# Task

Navigate into different rooms, look around and report the list of objects of each visited room
The objects are:
* Cat
* Sofa
* Potted plant
* Clock
* Sports ball

Rooms to be visited are given in the /poses topic published by the *poses_publisher_node*.
Use the rostopic command and the ros documentation to understand the type and the structure of the topics.

The included *myproject.launch* launches the framework, including 
* the gazebo simulator, loading the appropriate world
* the map publisher (complete with reference frames)
* the pose publisher (that publisher the list of locations to be visited in the world)
* a rviz file with some topics preloaded

## Setup

Extract the gazebo_data archive in the home directory

```
mv gazebo_data.tar.gz ~
cd
tar -zxf gazebo_data.tar.gz
```

# Running

### Requirements

build the workspace
~~~ sh
catkin build
~~~

## Execution

For a successful execution follows these steps:

1. launch the framework
~~~ sh
roslaunch cog2020proj myproject.launch world:=world1_objects
~~~

2. run the detector, wait for the "detector ready" feedback to launch the number 6
~~~ sh
rosrun detector detector_node
~~~

3. run the image publisher
~~~ sh
rosrun detector imagepublisher_node
~~~

4. run the image visualization node for debugging
~~~ sh
rosrun detector visualization_node
~~~

5. run the counter node
~~~ sh
rosrun cog2020proj counter_node
~~~

6. run the poses manager node
~~~ sh
rosrun cog2020proj poses_manager_node 
~~~

In order to re-execute the demostration you just need to run the poses_manager_node again.
