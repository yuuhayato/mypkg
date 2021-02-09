# mypkg
ロボットシステム学課題1
---
## 概要
  - ランダムに2数を作成した。1つ目は[random1.py](https://github.com/yuuhayato/mypkg/blob/main/scripts/random1.py)は1～10の整数、もう1つの[random2.py](https://github.com/yuuhayato/mypkg/blob/main/scripts/random2.py)は0～1までの数字にした。
  加えて、その2数を掛けた値を表示させる[kadai2.py](https://github.com/yuuhayato/mypkg/blob/main/scripts/kadai2.py)を作成した。
---
## 環境
  - ubuntu 18.04
  - ROS Melodic
---
## 環境構築
  - パッケージのクローン(以下を実行してください)
  ```sh
  cd ~/catkin_ws/src  
  git clone https://github.com/yuuhayato/mypkg.git  
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
