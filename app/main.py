from lib import lib

def main():
    path: str = "/home/evgenii/Work/edu-eschool/"
    # check = check_exists(path, PATHS)
    # print(check)
    lib.create_objects(
        '/home/evgenii/Work/bfo-mchs-ui/',
        'income_forecasting/register_AD',
        data_file=True,
        test_file=True
    )


if __name__ == "__main__":
    main()


