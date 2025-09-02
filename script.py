import random
from PIL import Image

QRVERSION = 6
#Versão do QR code, pra ficar mais facil definir o tamanho, eu acho

TAMANHOQR = 21 + ((QRVERSION - 1) * 4)
# Sempre valor impar para tamanho de QR code!

ESCALA = 10
# Tamanho dos pixeis, nesse caso, cada pixel do qr code vai ter 10x10 de tamanho

QUIETZONE = 1
# Tamanho da borda branca

TAMANHOIMG = TAMANHOQR + (QUIETZONE * 2)

# matrix = [[random.randint(0, 1) for _ in range(TAMANHOIMG)] for _ in range(TAMANHOIMG)]
# valor aleatorio
img = Image.new('1', (TAMANHOIMG * ESCALA, TAMANHOIMG * ESCALA))
matrix = [[1 for _ in range(TAMANHOIMG)] for _ in range(TAMANHOIMG)]


def desenhaQrCode():
    for y in range(TAMANHOIMG): 
            for x in range(TAMANHOIMG):
                    for iy in range(ESCALA):
                            for ix in range(ESCALA):
                                    img.putpixel((x * ESCALA + ix, y * ESCALA + iy), matrix[y][x])

def desenhaQuietzone():
    for y in range(TAMANHOIMG):
       for x in range(TAMANHOIMG):
              if x < QUIETZONE or y < QUIETZONE or x > TAMANHOIMG - (QUIETZONE + 1) or y > TAMANHOIMG - (QUIETZONE + 1) :
                     matrix[y][x] = 1

def desenhaFinder (x0, y0):
        pattern_finder = [
               [1,1,1,1,1,1,1,1,1],
               [1,0,0,0,0,0,0,0,1],
               [1,0,1,1,1,1,1,0,1],
               [1,0,1,0,0,0,1,0,1],
               [1,0,1,0,0,0,1,0,1],
               [1,0,1,0,0,0,1,0,1],
               [1,0,1,1,1,1,1,0,1],
               [1,0,0,0,0,0,0,0,1],
               [1,1,1,1,1,1,1,1,1]]
        
        for y in range(9):
            for x in range(9):
                    matrix[y0 + y][x0 + x] = pattern_finder[y][x]

def desenhaTimings():
    tamanho_timing = TAMANHOQR - (8 * 2) 
    pixel = False
    for y in range(tamanho_timing) :
        matrix[QUIETZONE + 8 + y][QUIETZONE + 8 - 2] = int(pixel)
        pixel = not pixel
    pixel = False
    for x in range(tamanho_timing) :
        matrix[QUIETZONE + 8 - 2][(QUIETZONE) + 8 + x] = int(pixel)
        pixel = not pixel

def desenhaTipoDados():
      tiposDeDados = {
            "numerico" : [0, 0, 0, 1],
            "alfanumerico" : [0, 0, 1, 0],
            "byte" : [0, 1, 0, 0],
            "kanji" : [1, 0, 0, 0],
      }

def desenhaFormatInfo():
      firstLine = [0, 0, 0, 0, 0, 0, 0]
      secondLine = [0, 0, 0, 0, 0, 0, 0, 0]

def desenhaPadrao():
    desenhaQuietzone()
    desenhaFinder((0 + (QUIETZONE - 1)), (0 + (QUIETZONE - 1)))
    desenhaFinder((0 + (QUIETZONE - 1)), (TAMANHOIMG - 9 - (QUIETZONE - 1)))
    desenhaFinder((TAMANHOIMG - 9 - (QUIETZONE - 1)), (0 + (QUIETZONE - 1)))
    desenhaTimings()


desenhaPadrao()
desenhaQrCode()

img.save('teste.png')
img.show()