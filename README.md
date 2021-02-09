# mypkg
ロボットシステム学課題1
---
## 概要
  - ランダムに2数を作成した。1つは1～10の整数、もう1つは0～1までの数字にした。
  加えて、その2数を掛けた値を表示させた。
---
## 環境
  - ubuntu 18.04
  - ROS Melodic
---
## 環境構築
  - パッケージのクローン(以下を実行してください)
  ```sh
  cd ~/catkin_ws/src  
  git clone https://github.com/RikuYokoo/draw_line_ros.git  
  cd ~/catkin_ws
  catkin_make
  ```
---
## 実行方法
  - 以下のコマンドを実行させます。
  `roslaunch mypkg mypkg.launch`
---
## ライセンス
  - [BSD 3-Clause "New" or "Revised" License](https://github.com/yuuhayato/mypkg/blob/main/LICENSE)
