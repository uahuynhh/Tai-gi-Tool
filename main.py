import re


def addTone(s, n):
    if s == 'a':
        if n == 1:
            return 'a'
        if n == 2:
            return 'á'
        if n == 3:
            return 'à'
        if n == 4:
            return 'a'
        if n == 5:
            return 'â'
        if n == 7:
            return 'ā'
        if n == 8:
            return 'a̍'
        if n == 9:
            return 'ă'
    elif s == 'i':
        if n == 1:
            return 'i'
        if n == 2:
            return 'í'
        if n == 3:
            return 'ì'
        if n == 4:
            return 'i'
        if n == 5:
            return 'î'
        if n == 7:
            return 'ī'
        if n == 8:
            return 'i̍'
        if n == 9:
            return 'ĭ'
    elif s == 'u':
        if n == 1:
            return 'u'
        if n == 2:
            return 'ú'
        if n == 3:
            return 'ù'
        if n == 4:
            return 'u'
        if n == 5:
            return 'û'
        if n == 7:
            return 'ū'
        if n == 8:
            return 'u̍̍'
        if n == 9:
            return 'ŭ'
    elif s == 'e':
        if n == 1:
            return 'e'
        if n == 2:
            return 'é'
        if n == 3:
            return 'è'
        if n == 4:
            return 'e'
        if n == 5:
            return 'ê'
        if n == 7:
            return 'ē'
        if n == 8:
            return 'e̍'
        if n == 9:
            return 'ĕ'
    elif s == 'o':
        if n == 1:
            return 'o'
        if n == 2:
            return 'ó'
        if n == 3:
            return 'ò'
        if n == 4:
            return 'o'
        if n == 5:
            return 'ô'
        if n == 7:
            return 'ō'
        if n == 8:
            return 'o̍'
        if n == 9:
            return 'ŏ'


def compChar(s):
    complete = ''
    for x in s:
        complete += x
    return complete


a = input()


def main(d):
    d = re.split('(\d+)', d)
    d_vowel = re.findall(r'[aiueo]', d[0])
    d_notVowel = re.split(r'[aiueo]', d[0])
    if len(d) != 1:
        if d[1] != '':
            if len(d_vowel) > 1:
                d_vowel[1] = addTone(d_vowel[1], int(d[1]))
            else:
                d_vowel[0] = addTone(d_vowel[0], int(d[1]))
        d_notVowel.insert(1, compChar(d_vowel))
    else:
        d_notVowel.insert(1, compChar(d_vowel))

    print(compChar(d_notVowel))


main(a)
