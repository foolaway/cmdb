from flask import Flask
from api import auth_api
from api import account_api
from api import group_api

app = Flask(__name__)

app.register_blueprint(auth.bp_auth)
app.register_blueprint(group.bp_group)
app.register_blueprint(account.bp_account)

if __name__ == '__main__':
    app.run()
