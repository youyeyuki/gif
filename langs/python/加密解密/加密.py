# -*- coding: utf-8-*-
__author__ = 'Wings'
import sys
reload(sys)
sys.setdefaultencoding('utf-8')



def encrypt_string(input_str, n):
    s = ''
    strlen = len(input_str)
    if strlen % n != 0:
        print '你输入的字符长度不够 enter使用空格补全 你也可以输入一个字符进行补全'
        print '输入你要补全的字符'
        placeholder_char = raw_input()
        if not placeholder_char:
            placeholder_char = ' '
        placeholder = n - strlen % n
        input_str += placeholder * placeholder_char[0]
        print input_str
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
    group = strlen / n
    while strlen % n != 0:
        print '你输入的密文好像格式不对呐 检查一下是否遗留了空格'
        print  '重新输入一下？'
        str_decode = raw_input();
        strlen = len(str_decode)
        group = strlen / n

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
    print '1.encrypt 2.decode 3.暴力破解'
    print 'please input the function number !'
    num = raw_input()
    if num == '1':
        print '请输入要加密的字符串'
        encrypt_str = raw_input()
        print '请输入要加密的圈数'
        n = raw_input()
        print encrypt_string(encrypt_str, int(n))
    if num == '2':
        print '请输入要解密的字符串'
        decode_str = raw_input()
        print '请输入要解密的圈数'
        n = raw_input()
        print decode_string(decode_str, int(n))
    if num == '3':
        print '暴力破解 直接输入字符串'
        tmp_str = raw_input()
        max = len(tmp_str)
        n = 1
        while max / 2 >= n:
            if 0 == max % n:
                print '移动了{num}位 解码后是{code}'.format(num=n, code=decode_string(tmp_str, n))
            n += 1
def test():
    placeholder_char = raw_input()
    input_str = raw_input()
    placeholder = 5
    input_str += placeholder * placeholder_char[0]
    print input_str


if __name__ == '__main__':
    main()