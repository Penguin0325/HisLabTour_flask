# HisLabTour_flask
# 仮想環境の作成
python3 -m venv venv

# 仮想環境を有効化 (Windowsの場合)
venv\Scripts\activate

# 仮想環境を有効化 (Mac/Linuxの場合)
source venv/bin/activate

# Flaskのインストール
pip install flask

# requirements.txtの作成
pip freeze > requirements.txt

# requirements.txtのインストール
pip install -r requirements.txt

