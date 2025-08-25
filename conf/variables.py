import os
from os import environ


class Variables:
    """
    Данный класс представляет собой централизованное хранилище ссылок на переменные окружения,
    а также на их значения по умолчанию, если они не были определены в оболочке.
    """
    APPIUM_SERVER = environ.get("APPIUM_SERVER") or 'http://localhost:4723'
    ''' Сервер с запущенным Appium '''

    DEVICE_NAME = environ.get("DEVICE_NAME") or 'Android 11'
    ''' Целевое устройство для исполнения тестов '''

    APP_PATH = environ.get("APP_PATH") or os.path.realpath("./app-debug.apk")
    ''' Путь к установочному файлу приложения '''

    ORIENTATION = environ.get("ORIENTATION") or 'PORTRAIT'
    ''' Путь к установочному файлу приложения '''