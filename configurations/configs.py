import os
import yaml

ENV_KEY = "ENV"
PORT_KEY = "PORT"
DEFAULT_ENV = "dev"
DEFAULT_PORT = "8080"

DB_URL_PREFIX = 'db_url_prefix'
DB_USER_KEY = "db_user"
DB_PASSWORD_KEY = "db_password"
DB_HOST_KEY = "db_host"
DB_PORT_KEY = "db_port"
DB_NAME_KEY = "db_name"


class Config:

    def __init__(self):
        self.data = Config.load()

    @staticmethod
    def load():
        data = dict()
        data[ENV_KEY] = os.getenv(ENV_KEY) if os.getenv(ENV_KEY) else DEFAULT_ENV
        data[PORT_KEY] = os.getenv(PORT_KEY) if os.getenv(PORT_KEY) else DEFAULT_PORT
        config_file_name = f"configurations/{data[ENV_KEY]}.yaml"

        try:
            with open(config_file_name) as f:
                data = yaml.safe_load(f)
        except:
            print(f"Config File {config_file_name} not found.")

        for key, _ in data.items():
            env_value = os.getenv(key.upper())
            if env_value:
                data[key] = env_value

        return data

    def get_database_url(self):
        url_prefix = self.data[DB_URL_PREFIX]
        user = self.data[DB_USER_KEY]
        password = self.data[DB_PASSWORD_KEY]
        host = self.data[DB_HOST_KEY]
        port = self.data[DB_PORT_KEY]
        db_name = self.data[DB_NAME_KEY]

        return f'{url_prefix}://{user}:{password}@{host}:{port}/{db_name}'

    def get_port(self):
        return self.data[PORT_KEY]


configs = Config()
