# Ceaser Cypher Encryptor By Adding Message And Key

# Inputting Message and Key
message = input('Enter the message you want to encrypt: ')
key = int(input('Enter the key(integer): '))
key = key % 26

# Splitting Message into Words
msg_words = message.split()

# Splitting Words into Characters
msg_ch = list()
for i in msg_words:
    for char in i:
        msg_ch.append(char)
# List of Encrypted Message Characters
msg_enc = list()

# Encrypting Message Letter by Letter and Appending to  List
for i in msg_ch:
    if(ord(str(i)) >= ord('a') and ord(str(i)) <= ord('z')):
        if (ord(str(i)) + key) <= ord('z'):
            msg_enc.append(chr(ord(str(i)) + key))
        else:
            msg_enc.append(chr(ord(str(i)) + key-26))
    elif(ord(str(i)) >= ord('A') and ord(str(i)) <= ord('Z')):
        if (ord(str(i)) + key) <= ord('Z'):
            msg_enc.append(chr(ord(str(i)) + key))
        else:
            msg_enc.append(chr(ord(str(i)) + key - 26))
    else:
        msg_enc.append(i)

for i in msg_enc:
    print(i, end=" ")
print('')
