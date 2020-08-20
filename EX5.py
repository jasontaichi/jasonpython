myDict = {"dog": "狗", "cat": "貓" }

def English_to_Chinese():
    wordInput = input('請輸入英文單字')
    if wordInput in myDict.keys():
        print(f'{wordInput} => {myDict[wordInput]}')
    else:
        print('查無此單字')

def Chinese_to_English():
    wordInput = input('請輸入中文單字')
    if wordInput in myDict.values():
        print(f'{wordInput} => {list(myDict.keys())[list(myDict.values()).index(wordInput)]}')
    else:
        print('查無此單字')

def main():
    Choice = int(input('請輸入指令: 1. 英翻中  2. 中翻英  3.離開  '))

    while Choice == 3:
        break
    else:
        if Choice == 1:
            English_to_Chinese()
        elif Choice == 2:
            Chinese_to_English()
        else:
            print('請輸入正確的指令!')
        main()

main()
