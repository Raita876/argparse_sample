# ArgumentParser(argparse)とは
Pythonの標準ライブラリ。
コマンドライン引数の設定を色々できる優れもの。

# サンプルコード
```args.py
import argparse


def get_args():
    parser = argparse.ArgumentParser(description='This is sample argparse script')
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
```
# 使用例
```
$ python args.py -h
usage: args.py [-h] [-n NAME] [-a AGE] [-s {male,female}]

This is sample argparse script

optional arguments:
  -h, --help            show this help message and exit
  -n NAME, --name NAME  This is name.
  -a AGE, --age AGE     This is age
  -s {male,female}, --sex {male,female}
                        This is sex

$ python args.py -n 田中 -a 20 -s male
Namespace(age=20, name='田中', sex='male')
name: 田中
age : 20
sex : male
```

# 解説

## ArgumentParser()

parserの作成。descriptionには--helpで出てくる説明文の値をセットする。

```
parser = argparse.ArgumentParser(description='This is sample argparse script')
```

## add_argument()

引数を設定できるメソッド。

```
parser.add_argument('-n', '--name')
```

**default**でデフォルト値を設定できる。
実行時に引数を設定しない場合、デフォルトの値が反映される。

```
$ python args.py
Namespace(age=30, name='hogehoge', sex='male')
name: hogehoge
age : 30
sex : male
```

**type**で引数の型を指定できる。
違う型の値が渡されるとエラーとなる。

```
$ python args.py -a hogehoge
usage: args.py [-h] [-n NAME] [-a AGE] [-s {male,female}]
args.py: error: argument -a/--age: invalid int value: 'hogehoge'
```

**choices**で引数として許される値を指定することができる。
choicesで指定したもの以外の値が渡されるとエラーとなる。

```
$ python args.py -s man
usage: args.py [-h] [-n NAME] [-a AGE] [-s {male,female}]
args.py: error: argument -s/--sex: invalid choice: 'man' (choose from 'male', 'female')
```

**help**で引数の説明を加えることができる。

```
$ python args.py -h
usage: args.py [-h] [-n NAME] [-a AGE] [-s {male,female}]

This is sample argparse script

optional arguments:
  -h, --help            show this help message and exit
  -n NAME, --name NAME  This is name.
  -a AGE, --age AGE     This is age
  -s {male,female}, --sex {male,female}
                        This is sex
```


# Qiita記事

https://qiita.com/RW_876/items/d015313973bba3779d68
