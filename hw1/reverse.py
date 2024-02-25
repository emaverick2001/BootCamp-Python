from string import ascii_lowercase 
# Maverick Espinosa
# mespin11


# prompt user for encrypted message
reversed_alphabet = ascii_lowercase[::-1]

decrypted_message = ""

# store user encrypted message
message = input("Enter the encrypted message: ")


# go through each character and apply decryption scheme for each char in message
for x in message:
    # x must be a lowercase letter
    if x.isalpha():
        index = ascii_lowercase.find(x)
        decrypted_message += reversed_alphabet[index]
     # if x is a whitespace character, continue to next char
    else:
        decrypted_message += x
        
   
# Print out decrypted message
print("The plaintext message is:",decrypted_message)