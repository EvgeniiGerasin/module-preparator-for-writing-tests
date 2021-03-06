from lib import lib

import argparse


def main():

    parser = argparse.ArgumentParser('Preparer pattern (version alpha)')
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
    parser.add_argument(
        '-t', '--test_file',
        type=str,
        help=(
            'create test file. name should be like '
            '"test_name.py"'
        ),
        metavar='<name_test_file>'
    )
    args = parser.parse_args()

    # проверка на наличие аргументов иначе открывается справка
    if not args.path and not args.source and not args.test_file and not args.check:
        parser.print_help()

    # проверка проекта на наличие модулей
    if args.check:
        lib.check(args.check)
    # создание директории и файлов в каталоге source
    if args.source:
        if args.test_file:
            # проверка на наличие нужных параметров от пользователя
            # если таких нет, то выводим сообщение ошибки
            # и завершаем работу
            if not args.path:
                print(parser.error(
                    'try "-p <path_to_directiry> -t <name_test_file>"')
                )
            # проверка имени тестового файла. Если ошибка, то
            # выводит сообщение и завершает работу
            lib.check_name_test_file(args.test_file)
        # проверка на наличие нужных параметров от пользователя
        # если таких нет, то выводим сообщение ошибки
        # и завершаем работу
        if not args.path or not args.source:
            print(parser.error(
                'try "-p <path_to_directiry> -s <name_module>"'))
        lib.create_sourse_files(args.path, args.source)
        if args.test_file:
            lib.create_test_file(args.path, args.test_file, args.source)


if __name__ == "__main__":
    main()
