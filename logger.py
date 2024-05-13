import inspect
from datetime import datetime
import os


class Logger:

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, log_file_name: str = ''):
        date = datetime.now().strftime('%d_%m_%Y')
        self.__log_file_name = f"log_{date}" if len(log_file_name) <= 0 else f"{log_file_name}_{date}"
        self.__message = '',
        self.__date_time = datetime.now()
        self.__file_name = inspect.stack()[1].filename

    @staticmethod
    def __create_directory_if_not_exists(dir_path: str):
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

    def __write(self, log_type: str):
        self.__create_directory_if_not_exists(f'log')

        with open(f'log\\{self.__log_file_name}.log', 'a', encoding='utf-8') as file:
            file.writelines(f"[{log_type}] [{self.__file_name}] [{self.__date_time}] - {self.__message} \n")
            file.close()

    def debug(self, message: str):
        self.__message = message
        self.__write(f'DEBUG')

    def info(self, message: str):
        self.__message = message
        self.__write(f'INFO')

    def error(self, message: str):
        self.__message = message
        self.__write(f'ERROR')

