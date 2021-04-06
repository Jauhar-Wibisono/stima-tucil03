cd ../src
python3 -m venv venv
. venv/bin/activate
pip install flask
export FLASK_APP=interactiveMap.py
flask run
