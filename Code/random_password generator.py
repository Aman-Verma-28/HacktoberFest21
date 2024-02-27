
import array
import secrets
  
# maximum length of password needed
# this can be changed to suit your password length
MAX_LEN = 12
  

DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']  
LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z']
  
UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
                     'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']
  
SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', 
           '*', '(', ')', '<']
  

COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS
  
# randomly select at least one character from each character set above
rand_digit = secrets.SystemRandom().choice(DIGITS)
rand_upper = secrets.SystemRandom().choice(UPCASE_CHARACTERS)
rand_lower = secrets.SystemRandom().choice(LOCASE_CHARACTERS)
rand_symbol = secrets.SystemRandom().choice(SYMBOLS)
  
# combine the character randomly selected above
# at this stage, the password contains only 4 characters but 
# we want a 12-character password
temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol
  
  

for x in range(MAX_LEN - 4):
    temp_pass = temp_pass + secrets.SystemRandom().choice(COMBINED_LIST)
  
    
    temp_pass_list = array.array('u', temp_pass)
    secrets.SystemRandom().shuffle(temp_pass_list)
  

# to form the password
password = ""
for x in temp_pass_list:
        password = password + x
          
# print out password
print(password)
