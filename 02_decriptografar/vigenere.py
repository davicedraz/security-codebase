alphabet = "abcdefghijklmnopqrstuvwxyz".upper()

text = "mllvo gjw axie, viog vlgbg dfptll n zoe fe gyyom j xof nr tuegr fg tfusfe ayqwxt rrpjnfy xg, mlm nbnju, tphuc kzg fltrf i ytamuyvi ig pzi qs or rrzzrgmtt spg acwfq, ux nnz xj eiqln ry akgphrfy"

decriptedMessage = ""

def vetorize(string):
    listText = []
    for letter in string:
        listText.append(letter)
    return listText


def getIndex(letter, vector):
    for i in range(len(vector)):
        if vector[i] == letter:
            return i

def normalizeKey(text, key):
    key = vetorize(key)
    keyNormalized = ""

    for letter in text:
        if letter == " " or letter == ",":
            keyNormalized += letter
        else:
            aux = ""          
            
            aux = key[0]
            key.pop(0)
            keyNormalized += aux
            key.append(aux)

    return keyNormalized


def decript(text, key, alphabet):
    text = text.upper()
    key = key.upper()
    alphabet = list(alphabet)
    
    key = normalizeKey(text, key)
    decriptedMessage = ""

    for i in range(len(text)):
        if text[i] == " " or text[i] == ",":
            decriptedMessage += text[i]
        else:
            decriptedMessage += alphabet[getIndex(text[i], alphabet) - getIndex(key[i], alphabet) + 26 % 26]

    return decriptedMessage


def main(): 
    documentKeys = open('words.txt', 'r') #possiveis chaves de 4 letras
    documentDecripts1 = open('attempts.txt', 'w') #tentativas

    for line in documentKeys.readlines():
        
        #line = line.replace("\n", "")
        line = line[:4].upper()

        decriptedMessage = decript(text, line, alphabet)
        
        if('AMOR' in decriptedMessage):
            documentDecripts1.writelines(line + "\n")
        
    documentDecripts1.close()
    documentKeys.close()

    documentDecripts1 = open('attempts.txt', 'r')
    documentDecripts2 = open('results.txt', 'w')
    

    for line in documentDecripts1.readlines():

        documentKeys = open('words.txt', 'r')
        print(line)

        for rest in documentKeys.readlines():

            rest = rest[:4].upper()
            line = line[:4].upper()

            decriptedMessage = decript(text, line + rest, alphabet)
            
            if('AMOR' in decriptedMessage):
                #no documento, cada linha de tentativa sera listadas no padrao: Chave $ Texto descriptografado
                documentDecripts2.writelines(line + rest + " $ " + decriptedMessage + "\n")

            documentKeys.close()

    documentDecripts2.close()
    documentDecripts1.close()
    
main()