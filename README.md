# Robot Neuro-Symbolic AI System

This public repository contains all the documentation of the **'Twist and Snap: A Neuro-symbolic System for  
Affordance Learning of Opening Jars and Bottles'** research project.

The repository is divided into 4 main directories:

 - **Appendices**: Knowledge base representation, message formatting between services, and robot system evaluation captions.
 - **ROS**: Source code of the Robot Operating System used for the project.
 - **Scripts**: [Inference-System](https://github.com/Joagai23/robot-neuro-symbolic-system/tree/main/Scripts/Inference-System "Inference-System") (service used alongside ROS to run the simulation), [Jar-Knowledge-Base](https://github.com/Joagai23/robot-neuro-symbolic-system/tree/main/Scripts/Jar-Knowledge-Base "Jar-Knowledge-Base") (scripts used to gather and process data), and [blip-image-captioning-large](https://github.com/Joagai23/robot-neuro-symbolic-system/tree/main/Scripts/blip-image-captioning-large "blip-image-captioning-large") (scripts for the fine-tunning and testing of the image-captioning model)
 - **Unity/PickAndPlaceProject**: Virtual Unity project containing the Niryo Robot Arm and the Jar-Bottle models used for the simulation. The Unity Project must be run alongside the Inference System and the ROS container to successfully execute the project pipeline.
