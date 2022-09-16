from datetime import timedelta
import os

class Config:
    # use SQLite
    # SQLALCHEMY_DATABASE_URI = "sqlite:///demo.db"

    # use MySQL
    # 要預先在MySQL建立DB
    # mysql+pymysql://root(帳號):Dreamer_0506(pwd)@localhost(位址):3306(port num)/demo(dbName)
    # SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:Dreamer_0506@localhost:3306/demo"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # SECRET_KEY = "demo123"                        # create / decode token
    JWT_EXPIRATION_DELTA = timedelta(seconds=300)   # timeout 預設 300s
    JWT_AUTH_URL_RULE = "/auth/login"               # URL 預設 /auth
    # JWT_AUTH_HEADER_PREFIX = "FLASK"                # token value 前綴 預設 JWT (flask-jwt)
    JWT_AUTH_HEADER_PREFIX = os.environ.get("JWT_AUTH_HEADER_PREFIX", "FLASK")      # (os環境變量, 預設)
    SECRET_KEY = os.environ.get("SECRET_KEY", "flask123")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    # (command 設定環境變量) set DATABASE_URL=mysql+pymysql://root:Dreamer_0506@localhost:3306/demo

class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"      # 內存DB, 無具體文件

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    pass

app_config = {
    "testing": TestingConfig,
    "development": DevelopmentConfig,
    "production": ProductionConfig
}