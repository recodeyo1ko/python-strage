## HOW TO USE

```
# 仮想環境の作成
# python3 -m venv 任意の仮想環境名
python3 -m venv env
# 仮想環境の有効化
#Windows
env\scripts\activate.bat
#Mac
source env/bin/activate
# ライブラリのインストール
pip3 install -r requirements.txt
# 物体検出実行
python3 detect.py
# 仮想環境の無効化
deactivate
```

## memo

```
ライブラリの出力・保存
pip3 list
pip3  freeze > requirements.txt
```

```
ライブラリのインストール
pip3 install opencv-python
pip3 install ultralytics
```
