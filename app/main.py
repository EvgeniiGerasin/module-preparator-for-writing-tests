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


def check_exists(path_to: str, PATHS: tuple) -> str:
    """Проверяет наличие директорий и файлов в них

    Args:
    - path_to: путь до директории, в кторой нужно проверить
    существование директорий
    - PATH: пути, которые проверяются

    Returns:
    - not_exists_paths: отформатированная строка для вывода
    путей, которые не существуют
    """
    not_exists_paths = ''
    for path in PATHS:
        if not os.path.exists(path_to + path):
            not_exists_paths += "Not exists --> {} \n".format(path)
    return not_exists_paths


def main():
    path: str = "/home/evgenii/Work/edu-eschool/"
    check = check_exists(path, PATHS)
    print(check)


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
