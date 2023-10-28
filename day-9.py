#100 days of code day 8

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print("CAESAR CIPHER")

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
new_letters = []
#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
if shift > len(alphabet):
  shift = shift % 26


def caesar (text, shift, direction):
  text_characters = list(text)
  shifted_by = int(shift)
  if direction == "encode":
    for letter in range(0, len(text_characters)):
      current_letter_index = alphabet.index(text[letter])
      shifter = current_letter_index + shifted_by
      caesar_letters = alphabet[shifter]
      new_letters.append(caesar_letters)
      ciphered_word = ''.join(new_letters)
    print(f"The encoded word is {ciphered_word}")
  if direction == "decode":
    for letter in range(0, len(text_characters)):
      current_letter_index = alphabet.index(text[letter])
      shifter = current_letter_index - shifted_by
      caesar_letters = alphabet[shifter]
      new_letters.append(caesar_letters)
      enciphered_word = ''.join(new_letters)
    print(f"The decoded word is {enciphered_word}")
    
    
caesar(text,shift,direction)
# def encrypt(text, shift):
#   text_characters = list(text)
#   shifted_by = int(shift)
  # for letter in range(0, len(text_characters)):
  #   current_letter_index = alphabet.index(text[letter])
  #   shifter = current_letter_index + shifted_by
  #   new_letters.append(alphabet[shifter])
  #   ciphered_word = ''.join(new_letters)
  # print(f"The encoded word is {ciphered_word}")


# def decrypt(text, shift):
#   text_characters = list(text)
#   shifted_by = int(shift)
#   for letter in range(0, len(text_characters)):
#     current_letter_index = alphabet.index(text[letter])
#     shifter = current_letter_index - shifted_by
#     new_letters.append(alphabet[shifter])
#     print()
#     enciphered_word = ''.join(new_letters)
#   print(f"The decoded word is {enciphered_word}")
    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

   

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 
