from setup import app, server
from controllers.general_controller import general_blueprint

app.register_blueprint(general_blueprint)

if __name__ == '__main__':
    server.run_server()
