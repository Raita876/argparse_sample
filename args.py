import argparse


def get_args():
    parser = argparse.ArgumentParser(description='This is sample argparse script')

    # 引数設定
    parser.add_argument('-n', '--name', default='hogehoge', type=str, help='This is name.')
    parser.add_argument('-a', '--age', default=30, type=int, help='This is age')
    parser.add_argument('-s', '--sex', default='male', type=str, choices=['male', 'female'], help='This is sex')

    return parser.parse_args()


def main():
    args = get_args()
    print(args)
    print("name: %s" % args.name)
    print("age : %d" % args.age)
    print("sex : %s" % args.sex)


if __name__ == '__main__':
    main()
