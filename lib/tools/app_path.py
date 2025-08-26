import glob, os


def get_apk_file_path():
    os.chdir("./")
    files_list = glob.glob("*.apk")
    if len(files_list) > 1:
        raise EnvironmentError("В директории проекта ожидается только один файл с расширением .apk!")
    else:
        real_path = os.path.realpath(files_list[0])
        return real_path
