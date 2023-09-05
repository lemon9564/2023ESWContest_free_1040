# 2023ESWContest_free_1040
SLAM &amp; GPT &amp; AI-Based Quadruped Robot System for Silver Care

we have some errors so we upload files again at 2023.09.05


this robot based on ros

if you use server & ros , can operate this robot

++Operate code++

move robot

    roscore

    sudo python3 server/server.py

    sudo python3 Quadruped_robot_ws/src/turtlebot3/turtlebot3_bringup/src/KeyBoard.py

    sudo python3 Quadruped_robot_ws/src/turtlebot3/turtlebot3_bringup/src/run_robot.py
    
    
if you active robot, press a & d one by one and if you press m & s, robot will move leg

    f : go ahead
    b : go back
    r : turn right
    l : turn left
    
    
fall detection

    sudo python3 fall_detection/detect.py
    
    
chat system

    sudo python3 GPT_chat.py
