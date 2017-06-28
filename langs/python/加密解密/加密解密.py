# -*- coding: utf-8-*-
__author__ = 'Wings'
import sys


def encrypt_string(input_str, n):
    s = ''
    strlen = len(input_str)
    if strlen % n != 0:
        print('你输入的字符长度不够 enter使用空格补全 你也可以输入一个字符进行补全')
        print ('输入你要补全的字符')
        placeholder_char = input()
        if not placeholder_char:
            placeholder_char = ' '
        placeholder = n - strlen % n
        input_str += placeholder * placeholder_char[0]
        print ()
        strlen = len(input_str)  # update str_length

    for i in range(0, n, 1):
        for j in range(0, strlen, n):
            if (i + j ) == strlen:
                break
            if (i + j ) > strlen:
                pass
            else:
                s += input_str[i + j]
    return s


def decode_string(str_decode, n):
    js = ''
    strlen = len(str_decode)
    group = int(strlen / n)
    # while strlen % n != 0:
    #     print ('你输入的密文好像格式不对呐 检查一下是否遗留了空格')
    #     print  ('重新输入一下？')
    #     str_decode = input();
    #     strlen = len(str_decode)
    #     group = int(strlen / n)

    for i in range(0, group, 1):
        for j in range(0, strlen, group):
            if (i + j ) == strlen:
                break
            if (i + j ) > strlen:
                pass
            else:
                js += str_decode[i + j]
    return js


def main():
    print ('1.encrypt 2.decode 3.暴力破解')
    print ('please input the function number !')
    num = input()
    if num == '1':
        print ('请输入要加密的字符串')
        encrypt_str = input()
        print ('请输入要加密的圈数')
        n = input()
        print (encrypt_string(encrypt_str, int(n)))
    if num == '2':
        print ( '请输入要解密的字符串')
        decode_str = input()
        print ('请输入要解密的圈数')
        n = input()
        print (decode_string(decode_str, int(n)))
    if num == '3':
        print ('暴力破解 直接输入字符串')
        tmp_str = input()
        max = len(tmp_str)
        n = 1
        while max / 2 >= n:
            print ('移动了{num}位 解码后是   {code}'.format(num=n, code=decode_string(tmp_str, n)))
            n += 1


def test():
    placeholder_char = input()
    input_str = input()
    placeholder = 5
    input_str += placeholder * placeholder_char[0]


if __name__ == '__main__':
    main()