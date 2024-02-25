from string import ascii_lowercase 
# Maverick Espinosa
# mespin11

# Open file titled sample.txt
my_sample_file = open('pride_prejudice.txt', 'r', encoding='utf-8-sig')

# Read the entire content of the file into a string
sample_text = my_sample_file.read().strip()
# make capital letters lowercase aswell
sample_text = sample_text.lower()

dic = {}
#M = total number of letters in sample_text
M = 0
# store frequency of each letter in alphabet
for x in ascii_lowercase:
    dic[x] = sample_text.count(x)
    M += dic[x]



# prompt user for encrypted message
message = input("Enter the encrypted message: ")
# make sure all characters are lower case
message = message.lower()

min_chi_squared = float('inf')
best_key = 0
chi_values = []

# Decrypt the message using all possible shifts/keys (1-25) and calculate chi-squared values 
for k in range(1,26):
    # decrypt the message for given shift/key k
    shifted_alphabet = ascii_lowercase[-k:] + ascii_lowercase[:-k]
    decrypted_message = ""
    for x in message:
        if x.isalpha():
            index = ascii_lowercase.find(x.lower())
            decrypted_message += shifted_alphabet[index]
        else:
            decrypted_message += x
            
    # N = length of decrypted message
    N = len(decrypted_message)
    
    chi_squared = 0
    
    # for each character in the alphabet from a - z calculate chi squared for decrypted message of shift/key k
    for c in ascii_lowercase:
        # n(alpha) = number of times specific char in ascii lowercase appears in decrypted message for a given shift/key value k
        n = decrypted_message.count(c)
        # x(alpha) = number of times a specific char alpha occurs in sample txt file
        x = dic[c]
        # p(alpha) = [x(alpha) = number of times a specific char alpha occurs in sample txt file]
          #/[M = total number of letters in sample txt]
        p = x/M
        X_key = ((n-p*N)**2)/(p*N)
        # add X value to previous X vals calculated for specific alpha
        chi_squared += X_key
    # set smallest chi squared value and best key/shift value
    if chi_squared < min_chi_squared:
        min_chi_squared = chi_squared
        best_key = k
    

shifted_alphabet = ascii_lowercase[-best_key:] + ascii_lowercase[:-best_key]
    
# decrypt solution message
decrypted_message = ""
for x in message:
    if x.isalpha():
        index = ascii_lowercase.find(x.lower())
        decrypted_message += shifted_alphabet[index]
    else:
        decrypted_message += x


# Print out decrypted message
print("The plaintext message is:",decrypted_message)