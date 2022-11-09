def is_two(num):
    '''
    This function accepts number or string 2 
    and returns True
    otherwise, it will return False
    '''
    if num == 2 or num == '2':
        return True
    else:
        return False
    



# 2
# This function functions correctly

def is_vowel(letter):
    if letter.lower() in 'aeiou':
        return True
    else:
        return False
    



# 3 in-class

def is_conson(string):
    return len(string) == 1 and not is_vowel3(string) and string.isalpha()



# 4
# Define a function that accepts a string that is a word. The function 
    # should capitalize the first letter of the word if the word starts with a consonant.


# 4 in-class

def capit(string):
    first_letter = string[0]
    if is_conson(first_letter):
        string = string.capitalize()
    return string




# 5
## Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) 
# and the bill total and return the amount to tip.

# 5 in-class

# total_bill = int(input('Enter total bill : '))
#tip_pc = int(input('Enter tip percentage : '))
#leave_tip = total_bill / tip_pc

#print(f'You should leave {leave_tip} as the tip.')


## 6
## Define a function named apply_discount. It should accept a original price, 
##  and a discount percentage, and return the price after the discount is applied.

def apply_discount(price, disc_pc):
    discount = price * disc_pc
    return price - discount
apply_discount(100, .20)




# 7 
## Define a function named handle_commas. It should accept a string that is a number that 
 ## contains commas in it as input, and return a number as output.

def handling_commas(string):
    string = string.replace(',', "")
    return string




# 8 
## Define a function named get_letter_grade. It should accept a number and 
  ## return the letter grade associated with that number (A-F).
    
def is_letter_grade(score):
    if(score < 60):
        return 'F'
    elif(score < 70):
        return 'D'
    elif(score < 80):
        return 'C'
    elif(score < 90):
        return 'B'
    elif(score < 101):
        return 'A'
    





# 9
# remove vowels and return string with vowels removed.

def remove_vowels(string):
    vowel = ('a','e','i','o','u')
    for x in string.lower():
        if x in vowel:
            string = string.replace(x, "")
    print(string)
    



# 10
# Define a function named normalize_name. It should accept a string and 
  ## return a valid Python identifier:
def normalise_name(string):
    string = string.replace("$", "")
    string = string.replace("%", "")
    string = string.replace("!", "")
    string = string.replace("?", "")
    string = string.replace("&", "")
    string = string.replace(" ", "_")
    string = string.lower()
    return(string)



# 11
## Write a function named cumulative_sum that accepts a list of numbers and returns a list 
  ## that is the cumulative sum of the numbers in the list.
    # cumulative_sum([1, 1, 1]) returns [1, 2, 3]
    # cumulative_sum([1, 2, 3, 4]) returns [1, 3, 6, 10]

    
def cumulative_sums(nums):
    output = []
    total = 0
    for num in nums:
        total += num
        output.append(total)
    return output
