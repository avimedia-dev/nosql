### create a config
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
### to save config
pip freeze > requirements.txt
### database
https://cloud.mongodb.com/ 
### create .env file with
.env
DBUSERNAME=...
DBPASSWORD=...