#!/bin/bash

# ROS2 環境の設定
source /opt/ros/humble/setup.bash  # ROSバージョンに応じて変更してください
source ~/neuratruck_ws/install/setup.bash  # ワークスペースに応じて変更してください

# 初期座標
x=100
y=100

# 座標を(100,100)から(900,900)まで100ごとに増加させて送信
while [ $x -le 900 ]
do
  ros2 topic pub /odom nav_msgs/msg/Odometry "{
    header: {
      stamp: {
        sec: $(date +%s),
        nanosec: 0
      },
      frame_id: 'odom'
    },
    pose: {
      pose: {
        position: { x: $x, y: $y, z: 0.0 },
        orientation: { x: 0.0, y: 0.0, z: 0.0, w: 1.0 }
      }
    }
  }" -1

  # 100単位で増加
  x=$((x + 100))
  y=$((y + 100))

  # メッセージ送信間隔
  sleep 1  # 1秒ごとにメッセージを送信
done

