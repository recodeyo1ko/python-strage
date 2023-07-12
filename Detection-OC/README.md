# HOW TO USE

## Python 環境構築

仮想環境の構築

```bash
python3 -m venv env
```

仮想環境の有効化

```bash
#Windowsの場合
env\scripts\activate.bat
#Macの場合
source env/bin/activate
```

ライブラリのインストール

```bash
pip3 install -r requirements.txt
```

物体検出実行

```bash
python3 detect.py
```

仮想環境の無効化

```bash
deactivate
```


## memo

```bash
ライブラリの出力
pip3 list
ライブラリの保存
pip3  freeze > requirements.txt
```
