from api.auth_api import AuthAPI
from api.group_api import GroupAPI
from api.account_api import AccountAPI
from api.audit_api import AuditAPI
from api.config_repo_api import ConfigRepoAPI
from api.machine_api import MachineAPI
from api.res_pool_api import ResPoolAPI
from api.safe_group_api import SafeGroupAPI
from api.service_api import ServiceAPI
from api.task_api import TaskAPI
from api.overview_api import OverviewAPI
from core.settings import settings
from core.server import Server

Server.app.register_blueprint(AuthAPI.bp_auth_api)
Server.app.register_blueprint(GroupAPI.bp_group_api)
Server.app.register_blueprint(AccountAPI.bp_account_api)
Server.app.register_blueprint(AuditAPI.bp_audit_api)
Server.app.register_blueprint(ConfigRepoAPI.bp_config_repo_api)
Server.app.register_blueprint(MachineAPI.bp_machine_api)
Server.app.register_blueprint(ResPoolAPI.bp_res_pool_api)
Server.app.register_blueprint(SafeGroupAPI.bp_safe_group_api)
Server.app.register_blueprint(ServiceAPI.bp_service_api)
Server.app.register_blueprint(TaskAPI.bp_task_api)
Server.app.register_blueprint(OverviewAPI.bp_over_view_api)

app = Server.app

if __name__ == '__main__':
    print(settings["listen"]["port"])
    # app.run(host=settings["listen"]["bind"], port=1234, debug=True)
    # app.run(host='0.0.0.0', port=8088)
