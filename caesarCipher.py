alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def encrypt(text, shift_number):
    cipherText = ""
    for letter in text:
        position = alphabet.index(letter)
        new_position = position + shift_number
        new_letter = alphabet[new_position]
        cipherText += new_letter
    print(f"The encoded text is: {cipherText}")

def decrypt(text, shift_number):
    decryptedText = ""
    for letter in text:
        position = alphabet.index(letter)
        new_position = position - shift_number
        new_letter = alphabet[new_position]
        decryptedText += new_letter
    print(f"The decrypted text is: {decryptedText}")



print("""   ___                           
  / __\__ _  ___  ___  __ _ _ __ 
 / /  / _` |/ _ \/ __|/ _` | '__|
/ /__| (_| |  __/\__ \ (_| | |   
\____/\__,_|\___||___/\__,_|_|   
                                 
   ___ _       _                 
  / __(_)_ __ | |__   ___ _ __   
 / /  | | '_ \| '_ \ / _ \ '__|  
/ /___| | |_) | | | |  __/ |     
\____/|_| .__/|_| |_|\___|_|     
        |_|                      """)

while True:


    direction = input("Would you like to encrypt(encode) or decrypt(decode) a text?: ")
    if direction == "encode":

        text = input("Type your message: ")
        shift_number = int(input("Shift amount: "))
        encrypt(text, shift_number)
        goAgane = input("Would you look to go again?(y/n):  ").lower()
        if goAgane == "y":
            continue
        elif goAgane == "n":
            break
        else:
            print("Enter either y/n: ")
        

    elif direction == "decode":
        text = input("Type your message: ")
        shift_number = int(input("Shift amount: "))
        decrypt(text, shift_number)
        goAgane = input("Would you look to go again?(y/n): ").lower()
        if goAgane == "y":
            continue
        elif goAgane == "n":
            break
        else:
            print("Enter either y/n: ")
    else:
        print("Write either encode / decode.")