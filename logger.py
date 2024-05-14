import inspect
from datetime import datetime
import os


class Logger:
    def __init__(self, log_file_name: str = ''):
        date = datetime.now().strftime('%d_%m_%Y')
        self.__log_file_name = f"log_{date}" if len(log_file_name) <= 0 else f"{log_file_name}_{date}"
        self.__message = '',
        self.__date_time = datetime.now()
        self.__file_name = inspect.stack()[1].filename

        self.__logger_enable: bool = False
        self.__info_enable: bool = False
        self.__debug_enable: bool = False
        self.__error_enable: bool = False
        self.__warning_enable: bool = False

        self.__config_file_read()

    @staticmethod
    def __create_directory_if_not_exists(dir_path: str):
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

    @staticmethod
    def __config_file_create():
        file = 'logger.conf'
        if not os.path.isfile(file):
            with open(file, 'a', encoding='utf-8') as conf:
                conf.write(f"#logger_enable=True \n")
                conf.write(f"#info_enable=True \n")
                conf.write(f"#debug_enable=True \n")
                conf.write(f"#error_enable=True \n")
                conf.write(f"#warning_enable=True \n")
                conf.close()

    def __config_file_read(self):
        self.__config_file_create()
        with open('logger.conf', 'r', encoding='utf-8') as conf:
            lines = conf.readlines()
            for line in lines:
                if line.startswith('#'):
                    rest_of_string = line[1:-1:]
                    key, value = rest_of_string.split('=')
                    match key:
                        case 'logger_enable':
                            self.__logger_enable = True if value.strip() == 'True' else False
                        case 'info_enable':
                            self.__info_enable = True if value.strip() == 'True' else False
                        case 'debug_enable':
                            self.__debug_enable = True if value.strip() == 'True' else False
                        case 'error_enable':
                            self.__error_enable = True if value.strip() == 'True' else False
                        case 'warning_enable':
                            self.__warning_enable = True if value.strip() == 'True' else False

    def __write(self, log_type: str):
        if self.__logger_enable:
            self.__create_directory_if_not_exists(f'log')

            with open(f'log\\{self.__log_file_name}.log', 'a', encoding='utf-8') as file:
                file.writelines(f"[{log_type}] [{self.__file_name}] [{self.__date_time}] - {self.__message} \n")
                file.close()

    def debug(self, message: str):
        if self.__debug_enable:
            self.__message = message
            self.__write(f'DEBUG')

    def info(self, message: str):
        if self.__info_enable:
            self.__message = message
            self.__write(f'INFO ')

    def error(self, message: str):
        if self.__error_enable:
            self.__message = message
            self.__write(f'ERROR')

    def warning(self, message: str):
        if self.__warning_enable:
            self.__message = message
            self.__write(f'WARNING')
