import PyPDF2
import time
import os

BB = "\033[34;1m" # Blue light
YY = "\033[33;1m" # Yellow light
GG = "\033[32;1m" # Green light
WW = "\033[0;1m"  # White light
RR = "\033[31;1m" # Red light
CC = "\033[36;1m" # Cyan light
B = "\033[34m"    # Blue
Y = "\033[33m"    # Yellow
G = "\033[32m"    # Green
W = "\033[0m"     # White
R = "\033[31m"    # Red
C = "\033[36m"    # Cyan

banner = R + '''
__________________
______¶¶¶¶¶¶¶¶¶¶¶¶¶_______
_____¶¶¶¶¶¶__¶¶¶¶¶¶¶______
____¶¶¶¶______¶¶¶¶____
___¶¶¶________¶¶¶___
___¶¶_________¶¶¶___
__¶¶¶__________¶¶___
__¶¶___________¶¶___
__¶¶____________¶___
_¶¶____________¶¶_
_¶¶__________¶__¶¶__
_¶¶__________¶¶¶¶¶¶¶_¶¶_
_¶¶_________¶¶_¶¶_¶_
_¶¶____________¶¶_¶¶
_¶¶¶¶___________¶_¶¶
_¶¶¶¶¶¶________¶¶¶¶¶¶¶¶¶_¶
_¶¶_¶_____¶¶_¶¶_¶¶__¶_
¶¶__________¶____¶
¶¶_¶¶¶¶¶____¶¶__¶¶¶¶¶¶___¶
_¶¶¶_¶¶¶¶¶_¶¶¶¶_¶¶¶__¶¶¶__¶_
_¶¶_¶_¶¶¶_¶¶¶_¶¶¶__¶¶¶__¶¶
__¶¶¶¶¶_¶¶¶_¶¶¶¶¶¶¶___¶¶¶__¶__
__¶¶¶__¶¶¶_¶¶____¶¶¶__¶¶__
__¶¶¶__¶¶_¶¶___¶¶_¶_¶¶__
__¶¶_¶¶¶¶¶¶_¶¶¶¶¶__¶¶¶_¶¶¶¶¶¶¶¶_
__¶¶___¶¶¶¶¶_¶¶¶¶¶¶____¶¶_
__¶___¶¶¶_¶¶¶¶¶_____¶¶¶¶__
__¶¶__¶¶¶__¶¶¶¶____¶¶¶¶___
__¶¶__¶___¶____¶¶¶¶___
___¶¶¶¶¶¶_____¶_¶¶¶_¶___
___¶¶¶_¶¶____¶¶¶¶¶¶¶¶__¶__
____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_¶¶__¶¶__
____¶¶¶¶¶¶¶¶¶¶¶¶¶_¶__¶__
____¶¶¶¶_¶¶¶¶¶_¶_¶__¶¶__
____¶¶¶¶¶¶_¶¶¶¶¶¶_¶_¶¶¶___
_PDF†_¶¶¶¶_¶¶¶¶¶¶¶¶__¶¶___
_____¶¶¶¶¶¶¶¶¶¶_¶¶_¶¶_____
_____¶¶______¶____
_____¶¶______¶______
_____¶¶______¶______
_____¶¶_____¶_____
_____¶_____¶______
_____¶¶¶____¶_______
______¶¶¶¶¶¶¶¶¶¶¶¶¶_______
Por:_Json Security__¶¶________
'''
os.system('clear')
print(banner)

val = R + '[' + W + '+' + R + '] '

try:
    name_pdf = input(val + C + 'Nombre del archivo •>> ' + G)
    file = open(name_pdf, 'rb')

    PDF_ = PyPDF2.PdfFileReader(file)

    pag_ = PDF_.numPages
    #print(cl, color.C + 'N° Páginas: ',color.G + h, pag_)

    pag_ -= 1
    pag = 0
    print(BB + 'Procesando...\n')
    for i in range(pag_):
        obj_ = PDF_.getPage(pag)
        pag += 1
        text_ = obj_.extractText()
        #print(color.G + "*"*30)
        file_ = open(r'Text.txt', 'a')
        file_.writelines(text_)
        time.sleep(.2)
        #print('\nContenido:\n', text_)
    file.close()
    time.sleep(1)
#†††††††★★★★★★

    filename = './Text.txt'

    with open(filename) as texto:
        lines = texto.readlines()

    large_str = ''
    for line in lines:
        large_str += line.rstrip()
    #print(large_str)

#print(large_str[ : 100])

    len_ = len(large_str)
    print(val + C + 'Carácteres: ' + G, len_)
    print(val + C + 'Páginas: ' + G, pag_,'\n')
    while True:
        buscar = input(val + Y + '•>> ' + G)
        if buscar in large_str:
            num = large_str.index(buscar)
            num_read = 100
            izq = num + 150
            der =abs(num - num_read)

            if num > der:
                print(large_str[der:izq])
            else:
                print(large_str[:izq])
        else:
            print(BB + 'No encontrado.')
            continue
except KeyboardInterrupt:
    print(BB + 'Saliendo...')
    time.sleep(.3)
