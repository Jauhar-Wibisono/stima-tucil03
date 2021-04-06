cd ../src
py -3 -m venv venv
CALL venv\Scripts\activate
pip install Flask
set FLASK_APP=interactiveMap.py
python -m flask run