from data.contents import FileContent

import os
import sys
from pathlib import Path

_PATHS = (
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


def _handler_error(text_error: str, discription: str) -> str:
    """Обработкич ошибок

    Args:
        text_error (str): текст ошибки
        discription (str): описание ошибки из исключения

    Returns:
        str: полный текст ошибки
    """
    return f'\n wrong -> {text_error} :: {discription} \n'


def _not_exists_message(text: str):
    """Выводит сообщение об неинициализированных модулях
    в проекте и завершает работу

    Args:
        text (str): список модулей
    """
    print(
        '\nF*CK!!!!\n\n'
        + text
        + '\nTake it easy! Just add the specified modules\n'
    )
    sys.exit()


def _write_to_file(path_to_files: str, data_to_write: str):
    """Созадет и записывает контент в файлы

    Args:
        path_to_files (str): путь до файла
        data_to_write (str): контент для записи
    """
    try:
        with open(path_to_files, 'w') as f:
            f.write(data_to_write)
    except OSError:
        print(_handler_error('process write to file', path_to_files))
        sys.exit()


def _check_exists(path_to: str, PATHS: tuple) -> list:
    """Проверяет наличие директорий и файлов в них

    Args:
    - path_to: путь до директории, в кторой нужно проверить
    существование директорий
    - PATH: пути, которые проверяются

    Returns:
    - [exists_flag (bool), not_exists_paths(str)]: 
    если пути существуют то exists_flag = True, 
    not_exists_paths отформатированная
    строка для вывода путей, которые не существуют
    """
    not_exists_paths = ''
    exists_flag = True
    for path in PATHS:
        if not os.path.exists(path_to + path):
            exists_flag = False
            not_exists_paths += "not exists -> {} \n".format(path)
    return [exists_flag, not_exists_paths]


def _create_directory(path_to: str, name_directory: str):
    """Функция для создания указанной директории по указанному
    пути

    Args:
        path_to (str): путь до директории
        name_directory (str): название директории
    """
    try:
        Path(path_to + name_directory).mkdir(
            parents=True,
            exist_ok=False
        )
    except FileNotFoundError as e:
        print(_handler_error('process create directory', e.strerror))
    except OSError as e:
        print(_handler_error('process create directory', e.strerror))


def _handler_name_directory(name_directory: str) -> str:

    handlered_name_directory = name_directory
    if name_directory[0] == '/':
        handlered_name_directory = handlered_name_directory[1:]
    if name_directory[-1] == '/':
        handlered_name_directory = handlered_name_directory[
            :len(handlered_name_directory) - 1
        ]
    return handlered_name_directory.replace('/', '.')


def create_sourse_files(
    path_to: str,
    name_module: str,
    data_file: bool = True
):
    """Функция для создания файло и записи контента в них
    Есть проверка на наличие нужных модулей в проекте

    Args:
        path_to (str): путь до проекта
        name_module (str): название модуля для создания
        data_file (bool, optional): создавать или нет data.py. 
        Defaults to True.
    """
    # Проверяем созданы ли необходимые для работы модули.
    # Если нет - выводим список модулей, которые отсутсвуют
    # и завершаем работу
    exsists_list = _check_exists(path_to, PATHS=_PATHS)
    # flag_exsists = exsists_list[0]
    flag_exsists = True
    text_not_exists = exsists_list[1]

    if flag_exsists:
        # путь до директории source
        PATH_TO_SOURSE = path_to + '/automation/source/'
        # создаем путь до места куда должны положить файлы
        full_path_to_file = (PATH_TO_SOURSE + name_module).replace('//', '/')
        # проверяем существование директории, которую
        # необходимо создать.
        # Если она есть, выводим сообщение и завершаем
        # работу
        if _check_exists(PATH_TO_SOURSE, (name_module,))[0]:
            print(
                "\nalready exists -> {}\n"
                .format(full_path_to_file)
            )
            sys.exit()
        # создание указаной директории в проекте
        _create_directory(PATH_TO_SOURSE, name_module)
        # создаем пустые файлы в созданной директории
        if data_file:
            # data.py
            _write_to_file(
                full_path_to_file + '/data.py',
                FileContent.DATA_CODE_FILE
            )
            # task.py
            # заменяем / на . для правильной вставки импорта
            # модуля
            _write_to_file(
                full_path_to_file + '/task.py',
                FileContent.TASK_CODE_FILE_WITH_DATA
                .format(name_module=_handler_name_directory(name_module))
            )
        else:
            # task.py
            _write_to_file(
                full_path_to_file + '/task.py',
                FileContent.TASK_CODE_FILE
                .format(name_module=_handler_name_directory(name_module))
            )
        # locator.py
        _write_to_file(
            full_path_to_file + '/locator.py',
            FileContent.LOCATOR_CODE_FILE
        )
        if data_file:
            print(
                (
                    '\nsuccessfully create ->\n\n'
                    '\tname directory: {}\n'
                    '\tfiles: task.py, locator.py, data.py\n'
                    '\tfull path: {}\n'
                ).format(name_module, full_path_to_file)
            )
        else:
            print(
                (
                    '\nsuccessfully create ->\n\n'
                    '\tname directory: {}\n'
                    '\tfiles: task.py, locator.py\n'
                    '\tfull path: {}\n'
                ).format(name_module, full_path_to_file)
            )
    else:
        # выводит сообщение о необходимых модулях и
        # завершает работу
        _not_exists_message(text_not_exists)


def check(path_to: str):
    """Проверяем созданы ли необходимые для работы модули
    и завершаем работу.
    Если нет - выводим список модулей, которые отсутсвуют
    и завершаем работу

    Args:
        path_to (str): путь до проекта
    """
    exsists_list = _check_exists(path_to, PATHS=_PATHS)
    flag_exsists = exsists_list[0]
    text_not_exists = exsists_list[1]
    if flag_exsists:
        print('\nAll required modules are initialized\n')
        sys.exit()
    else:
        _not_exists_message(text_not_exists)


def check_name_test_file(name: str):

    if not '.py' in name:
        _handler_error(
            'name tests file should be "test_name.py" or "/dir/test_name.py"',
            ''
        )
        sys.exit()


def create_test_file(path_to: str, name_file: str, name_module: str):

    # путь до директории test
    PATH_TO_TEST = path_to + '/automation/tests/'
    # создаем путь до места куда должны положить файлы
    full_path_to_file = (PATH_TO_TEST + name_file).replace('//', '/')
    # проверяем существование директории, которую
    # необходимо создать.
    # Если она есть, выводим сообщение и завершаем
    # работу
    if _check_exists(PATH_TO_TEST, (name_file,))[0]:
        print(
            "\nalready exists -> {}\n"
            .format(full_path_to_file)
        )
        sys.exit()
    # создаение файла
    _write_to_file(
        full_path_to_file,
        FileContent.TEST_CODE_FILE
        .format(name_module=_handler_name_directory(name_module))
    )
    # сообщение о создании
    print(
        (
            '\nsuccessfully create ->\n\n'
            '\tfiles: {}\n'
            '\tfull path: {}\n'
        ).format(name_file, full_path_to_file)
    )


