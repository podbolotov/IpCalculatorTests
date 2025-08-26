import os
from os import environ
from lib.tools.app_path import get_apk_file_path


class Variables:
    """
    Данный класс представляет собой централизованное хранилище ссылок на переменные окружения,
    а также на их значения по умолчанию, если они не были определены в оболочке.
    """
    APPIUM_SERVER = environ.get("APPIUM_SERVER") or 'http://localhost:4723'
    ''' Сервер с запущенным Appium '''

    DEVICE_NAME = environ.get("DEVICE_NAME") or 'Android 11'
    ''' Целевое устройство для исполнения тестов '''

    APP_PATH = environ.get("APP_PATH") or get_apk_file_path()
    ''' Путь к установочному файлу приложения '''
