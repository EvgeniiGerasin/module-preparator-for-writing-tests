import argparse
from pathlib import Path
import os


PATHS = (
    '/config/config_test.py',
    '/config/requirements.txt',
    '/links/links.py',
    '/source/desktop/task.py',
    '/source/desktop/locator.py',
    '/source/authorization/task.py',
    '/source/authorization/locator.py',
    '/tests',
    '/utility/action.py',
    '/utility/asserts.py',
    '/utility/browser.py',
    '/utility/exceptions.py',
    '/utility/helper.py',
    '/utility/wait.py',
    '/conftest.py',
    '/pytest.ini',
)


def check_exists(path_to: str, PATHS: tuple) -> list:
    """Проверяет наличие директорий и файлов в них

    Args:
    - path_to: путь до директории, в кторой нужно проверить
    существование директорий
    - PATH: пути, которые проверяются

    Returns:
    - [exists_flag (bool), not_exists_paths(str)]: если пути существуют
    то exists_flag = True, not_exists_paths отформатированная
    строка для вывода путей, которые не существуют
    """
    not_exists_paths = ''
    exists_flag = True
    for path in PATHS:
        if not os.path.exists(path_to + path):
            exists_flag = False
            not_exists_paths += "not exists --> {} \n".format(path)
    return [exists_flag, not_exists_paths]


def create_objects(
    path_to: str,
    name_modul: str,
    data_file: bool = True,
    test_file: bool = False
) -> str:
    """Функция для создания указанных объектов в проекте

    Args:
    - path_to: путь до директории, в кторой нужно проверить
    существование директорий и создать объекты
    - name_modul: имя модуля для создания
    - data_file (optional): создать data.py. Defaults to True.
    - test_file (optional): создать test_name_modul.py. 
    Defaults to False.

    Returns:
    """
    PATH_TO_SOURSE = path_to + '/source/'
    PATH_TO_TEST = path_to + '/tests/'
    if check_exists(PATH_TO_SOURSE, (name_modul,))[0]:
        print("already exists ->", name_modul)
    else:
        Path(PATH_TO_SOURSE + name_modul).mkdir(
            parents=True,
            exist_ok=False
        )
        Path(PATH_TO_SOURSE + name_modul + '/task.py').touch(
            exist_ok=False
        )
        Path(PATH_TO_SOURSE + name_modul + '/locator.py').touch(
            exist_ok=False
        )
        if data_file:
            Path(PATH_TO_SOURSE + name_modul + '/data.py').touch(
                exist_ok=False
            )


def main():
    path: str = "/home/evgenii/Work/edu-eschool/"
    # check = check_exists(path, PATHS)
    # print(check)
    create_objects(
        '/home/evgenii/python-code/other/module-preparator-for-writing-tests',
        'class_journal',
        True,
    )


if __name__ == "__main__":
    main()


# DIRS_AND_OWN_FILES = {
#     # 'config': ['config_test.py', 'requirements.txt'],
#     # 'links': ['links.py'],
#     # 'sourse':
#     #     {
#     #         'desktop':
#     #             [
#     #                 'task.py', 'locator.py',
#     #             ],
#     #         'authorization':
#     #             [
#     #                 'task.py', 'locator.py',
#     #             ],
#     #     }
#     # ''
# }
