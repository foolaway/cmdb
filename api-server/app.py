from flask import Flask

from api.auth_api import AuthAPI
from api.group_api import GroupAPI
from api.account_api import AccountAPI

app = Flask(__name__)

app.register_blueprint(AuthAPI.bp_auth)
app.register_blueprint(GroupAPI.bp_group)
app.register_blueprint(AccountAPI.bp_account)

if __name__ == '__main__':
    app.run()
