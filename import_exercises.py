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
    