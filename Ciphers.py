#all of this was caused from me going on a gravity falls tangent, yay

#http://easy-ciphers.com/
#https://www.instructables.com/Best-Codes/
#http://practicalcryptography.com/ciphers/

message = "hello i am greg, i want to test stuff & things. 2022"

#! Ceaser Cypher & ROT13 Cipher
alphabet = [chr(value) for value in range(97, 123)]
CeaserOrder = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","u","u","v","w","x","y","z"]
def CeaserEncrypter(message, key = 13):#default is the ROT13 cipher
    CeaserEncryptedMessage = ''
    for letter in message:
        if letter  == " ":
            CeaserEncryptedMessage += " "
        elif letter.isalpha():
            CeaserEncryptedMessage += CeaserOrder[(alphabet.index(letter) + key)%26]
        else:
            CeaserEncryptedMessage += letter
    return CeaserEncryptedMessage

def CeaserDecrypter(message, key = 13):
    CeaserDecryptedMessage = ""
    for letter in message:
        if letter == " ":
            CeaserDecryptedMessage += " "
        elif letter.isalpha():
            CeaserDecryptedMessage += CeaserOrder[((alphabet.index(letter) - key) + 1)%26]
        else:
            CeaserDecryptedMessage += letter
    return CeaserDecryptedMessage

print(message)
CeaserEncryptedMessage = CeaserEncrypter(message)
print(CeaserEncryptedMessage)
CeaserDecryptedMessage = CeaserDecrypter(CeaserEncryptedMessage)
print(CeaserDecryptedMessage)

#! Atbash Cipher, reverse alphabet
reverseAlphabet = alphabet.reverse()
def AtbashEncrypter(message):
    AtbashEncryptedMessage = ""
    for letter in message:
        if letter.isalpha():
            AtbashEncryptedMessage += reverseAlphabet[alphabet.index(letter)]
        else:
            AtbashEncryptedMessage += letter
    return AtbashEncryptedMessage
#TODO
def atbashDecrypter(message):
    atbashDecryptedMessage = ''
    for letter in message:
        if letter.isalpha():
            pass

#! keyboard cipher, keyboard order mapped to alphabet
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","u","u","v","w","x","y","z"]
keyboardOrder = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
def keyboardEncypter(message):
    keyboardEncryptedMessage = ''
    for letter in message:
        if letter == " ":
            keyboardEncryptedMessage += letter
        elif letter.isalpha():
            keyboardEncryptedMessage += alphabet[keyboardOrder.index(letter)]
        else:
            pass
    return keyboardEncryptedMessage

def keyboardDecrypter(message):
    keyboardDecryptedMessage = ''
    for letter in message:
        if letter == " ":
            keyboardDecryptedMessage += letter
        elif letter.isalpha():
            keyboardDecryptedMessage += keyboardOrder[alphabet.index(letter)]
        else:
            pass
    return keyboardDecryptedMessage

newMessage = keyboardEncypter(message)
print(newMessage)
print(keyboardDecrypter(newMessage))

#! Baconian Cipher
#https://www.geeksforgeeks.org/baconian-cipher/
#I think thse can technically be any binary representation, 0 - 25
BaconianDict = {
        'A':'aaaaa', 'B':'aaaab', 'C':'aaaba', 'D':'aaabb', 'E':'aabaa',
        'F':'aabab', 'G':'aabba', 'H':'aabbb', 'I':'abaaa', 'J':'abaab',
        'K':'ababa', 'L':'ababb', 'M':'abbaa', 'N':'abbab', 'O':'abbba',
        'P':'abbbb', 'Q':'baaaa', 'R':'baaab', 'S':'baaba', 'T':'baabb',
        'U':'babaa', 'V':'babab', 'W':'babba', 'X':'babbb', 'Y':'bbaaa',
        'Z':'bbaab'}

def BaconianEncrypter(message):
    messageUppercase = message.upper()
    BaconianEncryptedMessage = ''
    for letter in messageUppercase:
        if letter == " ":
            keyboardDecryptedMessage += letter
        elif letter.isalpha():
            BaconianEncryptedMessage += BaconianDict[letter] + " "
        else:
            pass
    return BaconianEncryptedMessage
#TODO
def BaconianDecrypter(message):
    BaconianDecryptedMessage = ''
    for index, letters in enumerate(message):#? check groups of 5 letters??
        #? how to search a string in counts of 5???
        if letters in list(BaconianDict.values()):
            pass
        print("bruh")
    return BaconianDecryptedMessage
        


#TODO
#! Polybius Square

#TODO
#! Permutation Cipher


