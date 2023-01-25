import pyautogui as spam
import time

limite_msg = int(input("Limite de mensagens: "))
msg = str(input("Digite a mensagem: "))
i = 0
time.sleep(3)
while i < limite_msg:
    for c in range(0, len(msg)):
        if msg[c] in 'çÇ':
            if msg[c] in "ç":
                spam.hotkey("altright", ",")
            if msg[c] in "Ç":
                spam.hotkey("Shift", "altright", ",")
        if msg[c] in "ÃãÁáÀàÂâ":
            if msg[c] in "ã":
                spam.hotkey("Shift", "`")
                spam.typewrite('a')
            if msg[c] in "â":
                spam.hotkey("Shift", "6")
                spam.typewrite('a')
            if msg[c] in "á":
                spam.hotkey("'", "a")
            if msg[c] in"à":
                spam.hotkey("`", "a")
            if msg[c] in "Ã":
                spam.hotkey("Shift", "`")
                spam.typewrite('A')
            if msg[c] in "Â":
                spam.hotkey("Shift", "6")
                spam.typewrite('A')
            if msg[c] in "Á":
                spam.hotkey("'", "A")
            if msg[c] in"À":
                spam.hotkey("`", "A")

        if msg[c] in "ÊêÈèÉé":
            if msg[c] in "Ê":
                spam.hotkey("Shift", "6")
                spam.typewrite('E')
            if msg[c] in "É":
                spam.hotkey("'", "E")
            if msg[c] in"È":
                spam.hotkey("`", "E")
            if msg[c] in "ê":
                spam.hotkey("Shift", "6")
                spam.typewrite('e')
            if msg[c] in "é":
                spam.hotkey("'", "e")
            if msg[c] in"è":
                spam.hotkey("`", "e")

        if msg[c] in "ÌìÍí":
            if msg[c] in "Ì":
                spam.hotkey("'", "I")
            if msg[c] in "Í":
                spam.hotkey("`", "I")
            if msg[c] in "í":
                spam.hotkey("'", "i")
            if msg[c] in "ì":
                spam.hotkey("`", "i")

        if msg[c] in "ÕõÔôÒòÓó":
            if msg[c] in "Õ":
                spam.hotkey("Shift", "`")
                spam.typewrite('O')
            if msg[c] in "Ô":
                spam.hotkey("Shift", "6")
                spam.typewrite('O')
            if msg[c] in "Ó":
                spam.hotkey("'", "O")
            if msg[c] in"Ò":
                spam.hotkey("`", "O")
            if msg[c] in "õ":
                spam.hotkey("Shift", "`")
                spam.typewrite('o')
            if msg[c] in "ô":
                spam.hotkey("Shift", "6")
                spam.typewrite('o')
            if msg[c] in "ó":
                spam.hotkey("'", "o")
            if msg[c] in"ò":
                spam.hotkey("`", "o")

        if msg[c] in "ÛûÚúÙù":
            if msg[c] in "Û":
                spam.hotkey("Shift", "6")
                spam.typewrite('U')
            if msg[c] in "Ú":
                spam.hotkey("'", "U")
            if msg[c] in "Ù":
                spam.hotkey("`", "U")
            if msg[c] in "û":
                spam.hotkey("Shift", "6")
                spam.typewrite('u')
            if msg[c] in "ú":
                spam.hotkey("'", "u")
            if msg[c] in "ù":
                spam.hotkey("`", "u")
        spam.typewrite(msg[c])
        if msg[c] in ',.!?':
            time.sleep(0.05)

        time.sleep(0.01)
    spam.press("Enter")
    i += 1
