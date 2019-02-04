import string

#   INPUT: text as a string and an integer for the shift value.
  #   OUTPUT: The shifted text after being run through the Caeser cipher.

  #   Create a normal plain alphabet
  #   Create a shifted version of this alphabet
  #   (Try slicing using the shift and then reconcatenating the two parts)
  # return
  #   Use a for loop to go through each character in the original message.
  #   Then figure out its index match in the shifted alphabet and replace.
  #   It might be helpful to create an output variable to hold the new message.

  #   Keep in mind you may want to skip punctuation with an if statement.

  #   Return the shifted message. Use ''.join() method
  #   if you still have it as a list.
# alphabet = string.ascii_lowercase
# print(alphabet)
# print(list(alphabet))

def encrypt(text,shift):
  alphabet = list(string.ascii_lowercase)
  shiftedAlphabet = alphabet[shift:] + alphabet[:shift]
  enumerateText = list(enumerate(text))
  # print(enumerateText)
  # print(shiftedAlphabet[1])
  output = list(range(len(text)))

  for i, letter in enumerateText:
    # for ind, lett in alphabet
    if letter.lower() in alphabet:
      alphabetIndex = alphabet.index(letter.lower())
      newLetter =  shiftedAlphabet[alphabetIndex]
      output[i] = newLetter
    else:
      output[i] = letter

  return ''.join(output)

print(encrypt('Get this message to the main server',13))

    # INPUT: A shifted message and the integer shift value
    # OUTPUT: The plain text original message.
    # Create a normal plain alphabet
    # Create a shifted version of this alphabet with the shift value.
    # Use a for loop to go through each character in the encrypted message.
    # Then figure out its index match in the plain alphabet and replace.
    # It might be helpful to create an output variable to hold the new message.
    # Keep in mind you may want to skip punctuation with an if statement.
    # Return the original message. Use ''.join() method
    # if you still have it as a list.

def decrypt(text,shift):
  alphabet = list(string.ascii_lowercase)
  shiftedAlphabet = alphabet[shift:] + alphabet[:shift]
  enumerateText = list(enumerate(text))

  output = list(range(len(text)))

  for i, letter in enumerateText:
    # for ind, lett in alphabet
    if letter.lower() in shiftedAlphabet:
      shiftedAlphabetIndex = shiftedAlphabet.index(letter.lower())
      newLetter =  alphabet[shiftedAlphabetIndex]
      output[i] = newLetter
    else:
      output[i] = letter

  return ''.join(output)

print(decrypt('trg guvf zrffntr gb gur znva freire',13))


def brute_force(message):
  for i in list(range(14)):
    print("using shift value of {}".format(i))
    print(decrypt(message,i))
    """
    INPUT: A shifted message
    OUTPUT: Prints out every possible shifted message.
            One of the printed outputs should be readable.
    """

    # Use your previous decrypt() method and call it for every possible shift
    # using a For Loop.

    # Print out the result of each shift.


brute_force('trg guvf zrffntr gb gur znva freire')


