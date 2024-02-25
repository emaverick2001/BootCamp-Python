# Maverick Espinosa
# mespin11

# 1.1 Encoder
# Task 1
# write a function that can decode info stored in DNA samples

BinaryPair_base_mapping = {0:'A',1:'T',2:'C',3:'G'}

def encode_sequence (sequence):
    """
    Function: encode_sequence : encodes a string into a DNA sequence
    Arguments : 
        
    sequence : String string to be encoded
    
    Returns :
    String DNA encoded sequence
    """
    # error handling to check if arg is a string?
    # go through each character in string sequence
    encoded_sequence = ""
    for c in sequence:
        # get binary representation of characters ascii value in bits
        # need to make sure binary string is 8 bits, and omit '0b' prefix
        binary_string = bin(ord(c))[2:].zfill(8)
        # for each pair of bits, change to associated DNA base using dictionary
        for i in range(0, len(binary_string),2):
            pair = int(binary_string[i:i+2],2)
            encoded_sequence += BinaryPair_base_mapping[pair]
    return encoded_sequence       

# 1.2 Decoder
# Task 2
# Write a function called decode_sequence which inverts DNA sequence back into English text.

base_BinaryPair_mapping = {'A':0,'T':1,'C':2,'G':3}

def decode_sequence (encoded_sequence):
    """
    Function: decode_sequence : decodes a DNA sequence string into string message
    Arguments : 
        
    encoded_sequence : String DNA sequence to be decoded
    
    Returns :
    String decoded message
    """
    decoded_sequence = ""
    binary_string = ""
    # for each char in DNA sequence change to associated pair of binary bits
    for base in encoded_sequence:
        print("base:",base)
        binary_string += format(base_BinaryPair_mapping[base],'02b')
        print("binary string:",binary_string)
        if (len(binary_string) == 8):
            decoded_sequence += chr(int(binary_string,2))
            print("decoded sequence:",decoded_sequence)
            binary_string = ""
            # continue until we have 8 bits then convert binary string into ascci value then to character
            # if binary string == 8 convert to ascii valaue then to char and add to encoded string
            # clear binary string so that new bits can be converted to character
    return decoded_sequence

# 1.3 Encryption
# Task 3
# Write a function named encrypt_decrypt that takes as arguments
# a required string to be encoded and an optional string representing the key

def encrypt_decrypt(input_string, key='CAT'):
    """
    Function: encrypt_decrypt : Encrypts or decrypts a string using XOR encryption with a given key.
    
    Arguments:
    input_string: String to be encrypted or decrypted.
    key: Key used for XOR encryption. Default is 'CAT'.
    
    Returns:
    String Encrypted or decrypted message.
    """
    # Define the mapping of characters to binary representations
    mapping = {'A': '00', 'T': '01', 'C': '10', 'G': '11'}
    
    # Create a reverse mapping for binary to characters
    reverse_mapping = {v: k for k, v in mapping.items()}
    
    # Initialize an empty string for the result
    result = list(input_string)
    
    # Iterate through each character in the input string
    for k in key:
        for i,base in enumerate(result):

            # Perform XOR operation on the binary representations of base and key_char
            binary_result = bin(int(mapping[base], 2) ^ int(mapping[k], 2))[2:].zfill(2)
            
            # Convert the result back to a character using the reverse mapping
            result_char = reverse_mapping[binary_result]
            
            # Add the result character to the final result
            result[i] = result_char
    
    return ''.join(result)
            
# 1.4 Error assessment


# Task 4
# Write a function synthesizer that simulates this manufacturing process
# r function should takes a sequence (string) as input and return the sequence (string) of DNA synthesized by the robot
import random

def synthesizer (sequence):
    """
    Function: synthersizer : synthesizes a DNA sequence based on probabilities for each base
    
    Arguments:
    sequence: DNA sequence to be synthesized
    
    Returns:
    String synthesized DNA sequence
    """
    synthesized_sequence = ""
    # for each base in the sequence
    for base in sequence:
        rand_prob = random.random() * 100
        if base == 'A' :
            synthesized_sequence += base
        elif base == 'T' :
            if rand_prob < 90:
                synthesized_sequence += 'T'
            elif rand_prob < 95:
                synthesized_sequence += 'A'
            elif rand_prob < 98:
                synthesized_sequence += 'C'
            else:
                synthesized_sequence += 'G'
        elif base == 'C':
            if rand_prob < 97:
                synthesized_sequence += 'C'
            elif rand_prob < 98:
                synthesized_sequence += 'G'
            elif rand_prob < 99:
                synthesized_sequence += 'T'
            else:
                synthesized_sequence += 'A'
        elif base == 'G':
            if rand_prob < 95:
                synthesized_sequence += 'G'
            elif rand_prob < 97:
                synthesized_sequence += 'C'
            elif rand_prob < 99:
                synthesized_sequence += 'T'
            else:
                synthesized_sequence += 'A'
    return synthesized_sequence


# Task 5

def error_count (sequence,ref_sequence):
    """
    Function: error_count : counts number of mismatches between a sequence and its reference sequence
    
    Arguments:
    sequence: Sequence to be compared to reference sequence
    ref_sequence: reference sequence to compare sequence against
    
    Returns:
    number of mismatches found between sequence and ref_sequence
    """
    num_mismatch = 0
    # for each base in the sequence and ref_base in the reference sequence, check to see if they are equal
    for index,base in enumerate(sequence):
        if base != ref_sequence[index]:
            num_mismatch += 1
    return num_mismatch
        
# 1.5 Redundancy

# Task 6
#  for each encryption repeat synthesis n times

def redundancy (n,sequence):
    """
    Function: redundancy : creates n copies of a sequence and compares all n copies to find the correct letter in each position
    
    Arguments:
    n: number of copies to make of DNA sequence
    sequence: Sequence to be corrected

    Returns:
    corrected synthesized DNA sequence
    """
    corrected_sequence = ""
    copies = []
    bases = {'A': 0, 'T': 0,'C': 0, 'G': 0}
    frequencies = []
    
    # create n copies of sequence
    copies = [synthesizer(sequence) for i in range(n)]
    
    # initialize frequencies with a list of dictionaries for each position in the sequence
    frequencies = [bases.copy() for j in range(len(sequence))]

    # update frequency of bases in n copies
    for copy in copies:
        for index, base in enumerate(copy):          
            # Increase the frequency of the char corresponding to the base in the sequence copy
            frequencies[index][base] += 1

    # for each position, find the base with the highest frequency
    for freq_dict in frequencies:
        max_base = max(freq_dict, key=freq_dict.get)
        corrected_sequence += max_base
    return corrected_sequence

# Task 7
# test scheme

sequence = "TTTTGGGGCCCCGGGGTTTTCCCCAAAATTTTGGGGTTTTGGGGCCCCGGGGTTTTTTTTGGGGCCCCGGGGTTTTCCCCAAAATTTTGGGGTTTTGGGG"
synth_sequence = synthesizer(sequence)
corrected_sequence = redundancy(100, sequence)
print("desiredd sequence:",sequence)
print("actual sequence:",synth_sequence)
print("num mismatch:",error_count(sequence, synth_sequence))
print("corrected:",corrected_sequence)
print("num mismatch:",error_count(sequence, corrected_sequence))