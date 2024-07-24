import random
import string
def main():
    print("Welcome to the password Generator")
    while True:
        try:
            length=int(input("\nEnter a Length of Your Password\n"))
            if length<=0:
                raise ValueError("\nPlease Enter the Positive Integer\n")
            break
        except ValueError as e:
            print(e)
            continue
    
    
        
    while True:
        try:
            complexity=int(input("\nEnter a Complexcity of a password from 1 to 4\n"))
            list=[1,2,3,4]
            if complexity not in list:
                 raise ValueError("\nPlease Enter a value of Complexity is between 1 to 4\n")
            break
                
        except ValueError as e:
            print(e)
            continue
    passw=generate_pass(length,complexity)
    print("\nThe Generated Password Is\n ",passw)
def generate_pass(length,complexity):
    character=""
    if(complexity>=1):
        character+=string.ascii_lowercase
    if(complexity>=2):
        character+=string.ascii_uppercase
    if(complexity>=3):
        character+=string.digits
    if(complexity>=4):
        character+=string.punctuation
    if not character:
        raise ValueError("\nPlease Enter a value of Complexity is between 1 to 4\n")
    passw=''.join(random.choice(character)for i in range(length))
    return passw
if __name__=="__main__":
    main()
        
