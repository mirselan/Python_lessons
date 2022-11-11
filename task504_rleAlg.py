# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
############################################################################
with open('task504_textIn.txt', 'r', encoding='UTF-8') as t_in:
    text_in = t_in.readline()

#text_in = 'dfsdfdfdffffsdfdfds dcsdcvsvrv dcefefe deeeevvsfsrvr'


def encoder(data):
    text_out = ''
    text_pred = ''
    count = 1

    for j in text_in:
        if j != text_pred:
            if text_pred:
                text_out += str(count) + j
            elif not text_pred:
                text_out += str(count) + j
            count = 1
            text_pred = j
        else:
            count += 1

    return text_out

encod_text = encoder(text_in)
with open('encod.txt', 'w', encoding='UTF-8') as enc:
    enc.write(encod_text)


def decoder(data):
    text_decod = ''
    count = ''

    for i in data:
        if i.isdigit():
            count += i
        else:
            text_decod += i * int(count)
            count = ''
    return text_decod

decod_text = decoder(encod_text)
with open('decod.txt', 'w', encoding='UTF-8') as dec:
    dec.write(decod_text)