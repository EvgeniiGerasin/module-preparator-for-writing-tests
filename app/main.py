from os import pardir
import typing
from lib import lib

import argparse


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-p', '--path',
        help='path to directory of project',
        metavar='<path to directiry>'
    )
    parser.add_argument(
        '-c', '--check',
        help='сhecking modules in a project',
        metavar='<path to directiry>'
    )
    parser.add_argument(
        '-s', '--source',
        type=str,
        help='create new module',
        metavar='<name_module>'
    )
    args = parser.parse_args()

    # проверка проекта на наличие модулей
    if args.check:
        lib.check(args.check)
    # создание директории и файлов в каталоге source
    if args.source:
        # проверка на наличие нужных параметров от пользователя
        # если таких нет, то выводим сообщение ошибки 
        # и завершаем работу
        if not args.path or not args.source:
            print(parser.error(
                'try "-p <path_to_directiry> -s <name_module>"'))
        lib.create_sourse_files(args.path, args.source)


if __name__ == "__main__":
    main()
