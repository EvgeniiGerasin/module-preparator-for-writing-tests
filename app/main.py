from lib import lib

def main():
    path: str = "/home/evgenii/Work/edu-eschool/"
    # check = check_exists(path, PATHS)
    # print(check)
    lib.create_sourse_files(
        '/home/evgenii/python-code/other/module-preparator-for-writing-tests/',
        '/register_AD',
        True
    )


if __name__ == "__main__":
    main()


