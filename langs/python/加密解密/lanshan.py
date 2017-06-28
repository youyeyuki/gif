# -*- coding: utf-8 -*-
def main():
    str = '1234567'
    s = ''
    js = ''
    strlen = len(str)
    n = 3
    group = strlen / n
    placeholder_char = raw_input()

    placeholder = n - strlen % n
    print str + placeholder * placeholder_char
    for i in range(0, n, 1):
        for j in range(0, strlen, n):
            if (i + j) == strlen:  # 数组中没第8个 所以在这里必须要退出
                break
            if (i + j ) > strlen:  # 越界pass
                pass
            else:
                s += str[i + j]

    print s

    # 奇数时候
    if ~(strlen % 2 == 0) and strlen % n != 0:
        group += 1
        print group

    for i in range(0, group, 1):
        for j in range(0, strlen, group):  # 总长除以解密栏数
            if (i + j) == strlen:
                break;
            if (i + j) > strlen:
                pass
            else:
                js += s[i + j]
    print js


if __name__ == '__main__':
    main()
