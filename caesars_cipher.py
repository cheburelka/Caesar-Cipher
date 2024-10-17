def choice_mode():
    print("Выберите направление(ш - шифрование или д - дешифрование): ")
    while True:
        mode = input()
        if mode == "ш" or mode == "д":
            return mode
        else:
            print('Вы ввели что-то не то, введите "ш" или "д"')


def choice_language():
    print("Выберите язык(р - русский или а - английский):")
    while True:
        language = input()
        if language.lower() == "р" or language.lower() == "а":
            return language
        else:
            print('Вы ввели что-то не то, введите "р" или "а"')


def text_checking(language, mode):
    if mode == "ш":
        print("Введите текст для шифрования")
    else:
        print("Введите текст для дешифровки")
    new_text = ""
    if language == "р":
        while True:
            text = input()
            for i in range(len(text)):
                if 41 <= ord(text[i]) <= 90 or 97 <= ord(text[i]) <= 122:
                    print("Вы ввели текст не на том языке, попробуйте снова!")
                    break
                else:
                    return text
    if language == "а":
        while True:
            text = input()
            for i in range(len(text)):
                if 1040 <= ord(text[i]) <= 1071 or 1072 <= ord(text[i]) <= 1103:
                    print("Вы ввели текст не на том языке, попробуйте снова!")
                    break
                else:
                    return text


def choice_step(mode):
    if mode == "ш":
        print("Введите шаг шифрования")
        while True:
            step = input()
            if step.isdigit() == True:
                step = int(step)
                return step
            else:
                print("Вы ввели не число, попробуйте снова")
    else:
        print("Введите шаг дешифрования")
        while True:
            step = input()
            if step.isdigit() == True:
                step = int(step)
                return step
            else:
                print("Вы ввели не число, попробуйте снова")


def encryption_text(step, language, text):
    encrypted_text = ""
    if language == "р":
        for i in range(len(text)):
            if 1040 <= ord(text[i]) <= 1071:
                num = ord(text[i]) + step
                if num > 1071:
                    num -= 32
                    encrypted_text += chr(num)
                    continue
                else:
                    encrypted_text += chr(num)
                    continue
            if 1072 <= ord(text[i]) <= 1103:
                num = ord(text[i]) + step
                if num > 1103:
                    num -= 32
                    encrypted_text += chr(num)
                    continue
                else:
                    encrypted_text += chr(num)
                    continue
            else:
                encrypted_text += text[i]

    if language == "а":
        for i in range(len(text)):
            if 65 <= ord(text[i]) <= 90:
                num = ord(text[i]) + step
                if num > 90:
                    num -= 26
                    encrypted_text += chr(num)
                    continue
                else:
                    encrypted_text += chr(num)
                    continue
            if 97 <= ord(text[i]) <= 122:
                num = ord(text[i]) + step
                if num > 122:
                    num -= 26
                    encrypted_text += chr(num)
                    continue
                else:
                    encrypted_text += chr(num)
                    continue
            else:
                encrypted_text += text[i]
    return encrypted_text


def decryption_text(step, language, text):
    encrypted_text = ""
    if language == "р":
        for i in range(len(text)):
            if 1040 <= ord(text[i]) <= 1071:
                num = ord(text[i]) - step
                if num < 1040:
                    num += 32
                    encrypted_text += chr(num)
                    continue
                else:
                    encrypted_text += chr(num)
                    continue
            if 1072 <= ord(text[i]) <= 1103:
                num = ord(text[i]) - step
                if num < 1072:
                    num += 32
                    encrypted_text += chr(num)
                    continue
                else:
                    encrypted_text += chr(num)
                    continue
            else:
                encrypted_text += text[i]

    if language == "а":
        for i in range(len(text)):
            if 65 <= ord(text[i]) <= 90:
                num = ord(text[i]) - step
                if num < 65:
                    num += 26
                    encrypted_text += chr(num)
                    continue
                else:
                    encrypted_text += chr(num)
                    continue
            if 97 <= ord(text[i]) <= 122:
                num = ord(text[i]) - step
                if num < 97:
                    num += 26
                    encrypted_text += chr(num)
                    continue
                else:
                    encrypted_text += chr(num)
                    continue
            else:
                encrypted_text += text[i]
    return encrypted_text


mode = choice_mode()
language = choice_language()
step = choice_step(mode)
text = text_checking(language, mode)
if mode == "ш":
    print()
    print("Зашифрованный текст: ", encryption_text(step, language, text))
else:
    print()
    print("Дешифрованный текст: ", decryption_text(step, language, text))
