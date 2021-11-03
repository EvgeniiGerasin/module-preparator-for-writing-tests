class FileContent:

    LOCATOR_CODE_FILE = (
        "class Locator:\n"
        "\n\tpass\n"
    )
    DATA_CODE_FILE = (
        "class Data:\n"
        "\n\tpass\n"
    )
    TASK_CODE_FILE_WITH_DATA = (
        "from source.{name_module}.locator import Locator\n"
        "from source.{name_module}.data import Data\n"
        "from source.desktop.task import MainPage\n"
        "from utility.exceptions import InvalidTestConditionsException\n"
        "\n"
        "\n"
        "class Task???(MainPage):\n"
        "\n\tpass\n"
    )
    TASK_CODE_FILE = (
        "from source.{name_module}.locator import Locator\n"
        "from source.desktop.task import MainPage\n"
        "from utility.exeptions import InvalidTestConditionsException\n"
        "\n"
        "\n"
        "class Task???(MainPage):\n"
        "\n\tpass\n"
    )

    TEST_CODE_FILE = (
        "from source.{name_module}.task import ???\n"
        "from config.config_test import DataTest\n"
        "from source.description import Description\n"
        "\n"
        "import allure\n"
        "import pytest\n"
        "\n"
        "\n"
        "@allure.epic('')\n"
        "@allure.feature('')\n"
        "class Test???:\n\n"
        "\t@allure.story('')\n"
        "\t@allure.title('')\n"
        "\t@allure.description()\n"
        "\tdef test_???(self, web_driver):\n\n"
        "\t\ttask = ???\n"
    )
