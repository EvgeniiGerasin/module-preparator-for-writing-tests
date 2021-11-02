from os import pardir
import typing
from lib import lib

import argparse


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-c', '--check',
        help='сhecking modules in a project',
        action="store_true"
    )
    parser.add_argument(
        '-s', '--source',
        type=str,
        help='create new module',
        metavar='<name_module>'

    )
    parser.add_argument('path', help='path to project', type=str)
    args = parser.parse_args()

    print(args)

    # проверка проекта на наличие модулей
    if args.check:
        lib.check(args.path)


if __name__ == "__main__":
    main()
