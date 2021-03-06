# mypkg
ロボットシステム学課題1
---
## 概要
  - このリポジトリは上田隆一先生の[第10回講義](https://github.com/ryuichiueda/robosys2020/blob/master/md/ros.md)で作成したコードを改変したものです。  
  - ランダムに2数を作成した。1つ目の[random1.py](https://github.com/yuuhayato/mypkg/blob/main/scripts/random1.py)は1～10の整数、もう1つの[random2.py](https://github.com/yuuhayato/mypkg/blob/main/scripts/random2.py)は0～1までの数字にした。
  加えて、その2数を掛けた値を表示させる[kadai2.py](https://github.com/yuuhayato/mypkg/blob/main/scripts/kadai2.py)を作成した。
---
## 環境
  - ubuntu 18.04
  - ROS Melodic
---
## 動画
  - [デモ動画](https://www.youtube.com/watch?v=DJKWpmAZ53I)です。
---
## 環境構築
  - ROSのインストール
      - [こちら](https://github.com/ryuichiueda/ros_setup_scripts_Ubuntu18.04_server)を使用させていただきました。
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
