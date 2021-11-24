import os
from pathlib import Path
from lib.lib import (
    _handler_error, _check_exists, _create_directory
)

import unittest
import shutil


class TestMainComponents(unittest.TestCase):

    def test_handler_error(self):
        TEST_ERROR = 'Test error'
        DISCRIPTION = 'test description'
        reference_result = f'\n wrong -> {TEST_ERROR} :: {DISCRIPTION} \n'
        result = _handler_error(
            text_error=TEST_ERROR,
            discription=DISCRIPTION
        )
        self.assertEqual(result, reference_result)

    def test_check_exists_ok(self):
        # создание директории для теста
        PATH = './'
        NAME_DIR = 'test_dir'
        Path(PATH + NAME_DIR).mkdir(parents=True, exist_ok=False)

        result = _check_exists(path_to=PATH, PATHS=(NAME_DIR,))
        try:
            self.assertEqual(result[0], True)
            self.assertEqual(result[1], '')
        except AssertionError:
            raise AssertionError
        finally:
            # очистка от тестовых данных
            shutil.rmtree(PATH + NAME_DIR, ignore_errors=True)

    def test_check_exists_none(self):
        # создание директории для теста
        PATH = './'
        NAME_DIR = 'test_dir'
        result = _check_exists(path_to=PATH, PATHS=(NAME_DIR,))
        self.assertEqual(result[0], False)
        self.assertEqual(result[1], "not exists -> {} \n".format(NAME_DIR))

    def test_create_directory(self):
        PATH = './'
        NAME_DIR = 'test_dir'
        _create_directory(path_to=PATH, name_directory=NAME_DIR)
        try:
            assert os.path.exists(PATH + NAME_DIR)
        except AssertionError:
            raise AssertionError
        finally:
            # очистка от тестовых данных
            shutil.rmtree(PATH + NAME_DIR, ignore_errors=True)


if __name__ == "__main__":
    unittest.main()
