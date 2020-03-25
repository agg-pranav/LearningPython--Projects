# Ceaser Cypher Decryptor By Adding Message And Key

# Inputting Message and Key
message = input('Enter the message you want to decrypt: ')
key = int(input('Enter the key(integer): '))
key = key % 26

# Splitting Message into Words
msg_words = message.split()

# Splitting Words into Characters
msg_ch = list()
for i in msg_words:
    for char in i:
        msg_ch.append(char)
# List of Decrypted Message Characters
msg_dec = list()

# Decrypting Message Letter by Letter and Appending to  List
for i in msg_ch:
    if(ord(str(i)) >= ord('a') and ord(str(i)) <= ord('z')):
        if (ord(str(i)) - key) >= ord('a'):
            msg_dec.append(chr(ord(str(i)) - key))
        else:
            msg_dec.append(chr(ord(str(i)) - key + 26))
    elif(ord(str(i)) >= ord('A') and ord(str(i)) <= ord('Z')):
        if (ord(str(i)) - key) >= ord('A'):
            msg_dec.append(chr(ord(str(i)) - key))
        else:
            msg_dec.append(chr(ord(str(i)) - key + 26))
    else:
        msg_dec.append(i)

for i in msg_dec:
    print(i, end=" ")
print('')
