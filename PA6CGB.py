def decoder():
        
    iFile = open("Encrypted.txt", encoding = "utf8")

    oFile = open("DecryptedCGB.txt", 'w')

    code  = str(iFile.readlines())


    distance = int()
    plainText = ''
    for ch in code:
        ordValue = ord(ch)
        cipherValue = ordValue - distance
        if cipherValue < ord('a'):
            cipherValue = ord('z') - (distance - ord('a') - ordValue + 1)
            plainText += chr(cipherValue)
        elif cipherValue > ord('z'):
            cipherValue = ord('a') + distance - (ord('a') - ordValue + 1)



        oFile.write(str(ordValue))

    oFile.close()
        

def main():
    decoder()

main()
