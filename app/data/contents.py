class Files:

    LOCATOR_CODE_FILE = (
        "class Locator:\n"
        "    pass"
    )
    DATA_CODE_FILE = (
        "class Data:\n"
        "    pass"
    )
    TASK_CODE_FILE_WITH_DATA = (
        "from source.{name_module}.locator import Locator\n"
        "from source.{name_module}.data import Data\n"
        "from source.desktop.task import MainPage\n"
        "from utility.exceptions import InvalidTestConditionsException\n"
        "\n"
        "\n"
        "class Task???(MainPage):\n"
        "    pass"
    )
    TASK_CODE_FILE = (
        "from source.{name_module}.locator import Locator\n"
        "from source.desktop.task import MainPage\n"
        "from utility.exeptions import InvalidTestConditionsException\n"
        "\n"
        "\n"
        "class Task???(MainPage):\n"
        "    pass"
    )

    TEST_CODE_FILE = (
        "from source.{name_module}.task import ???\n"
        "from source.description import Description\n"
        "\n"
        "import allure\n"
        "import pytest\n"
    )