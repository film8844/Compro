"""doc"""


def roman_to_int(sen):
    """doc"""
    romanint = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500}
    summ = 0
    for i in range(len(sen)):
        if i > 0 and romanint[sen[i]] > romanint[sen[i - 1]]:
            summ += romanint[sen[i]] - (romanint[sen[i - 1]]) * 2
        else:
            summ += romanint[sen[i]]
    print(summ)


roman_to_int(input())

