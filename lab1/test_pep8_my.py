import string
import time  

shift = 3
PI = 3.14  

def print_time(time_now):
    if time_now:
        print(time.ctime())


def main():
    choice_mode = input("would you like to encode or decode?")
    word = input("Please enter text")
    LETTERS = string.ascii_letters + string.punctuation + string.digits  
    encoded = ""

    if choice_mode == "encode":
        for letter in word:
            if letter == " ":
                encoded = encoded + " "
            else:
                encoded_symvol = LETTERS.index(letter) + shift  
                encoded = encoded + LETTERS[encoded_symvol]

    if choice_mode == "decode":  
        for letter in word:
            if letter == " ":
                encoded = encoded + " "
            else:
                encoded_symvol = LETTERS.index(letter) - shift  
                encoded = encoded + LETTERS[encoded_symvol]

    print(encoded)
    print(word)


if __name__ == '__main__':
    main()