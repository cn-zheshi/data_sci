import config
from app import create_app

if __name__ == "__main__":
    app = create_app(config.DevelopmentConfig)
    app.run(host='127.0.0.1', port=8000)
