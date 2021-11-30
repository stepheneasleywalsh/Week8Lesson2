# Student Number: 2123456

# This is the loop for inputting Term 1 results
while True:
    print(" # # # Term 1 # # # ")
    try:
        # This code asks for the grades
        AES1 = int(input("AES: "))
        Maths1 = int(input("Maths 1: "))
        Physics1 = int(input("Physics 1: "))
        ComputerProgramming1 = int(input("Computer Programming 1: "))
        # This if checks that grades are between 0 and 100
        if AES1 < 0 or Maths1 < 0 or Physics1 < 0 or ComputerProgramming1 < 0 or AES1 > 100 or Maths1 > 100 or Physics1 > 100 or ComputerProgramming1 > 100:
            print("That is not a valid input.")
        else:
            # ALL GOOD! END THE LOOP I.E. BREAK OUT OF THE WHILE LOOP
            print("Thank you, Term 1 is inputted.")
            break
    except:
        # If they don't give a number, print this error message!
        print("That is not a number.")

# This is the loop for inputting Term 2 results
while True:
    print(" # # # Term 2 # # # ")
    try:
        # This code asks for the grades
        AES2 = int(input("AES: "))
        Maths2 = int(input("Maths 2: "))
        Physics2 = int(input("Physics 2: "))
        Chemistry1 = int(input("Computer Programming 1: "))
        # This if checks that grades are between 0 and 100
        if AES2 < 0 or Maths2 < 0 or Physics2 < 0 or Chemistry1 < 0 or AES2 > 100 or Maths2 > 100 or Physics2 > 100 or Chemistry1 > 100:
            print("That is not a valid input.")
        else:
            # ALL GOOD! END THE LOOP I.E. BREAK OUT OF THE WHILE LOOP
            print("Thank you, Term 2 is inputted.")
            break
    except:
        # If they don't give a number, print this error message!
        print("That is not a number.")

# This is the loop for inputting Term 3 results
while True:
    print(" # # # Term 3 # # # ")
    try:
        # This code asks for the grades
        AES3 = int(input("AES: "))
        Maths3 = int(input("Maths 3: "))
        Physics3 = int(input("Physics 3: "))
        CreativeDesign = int(input("Creative Design: "))
        # This if checks that grades are between 0 and 100
        if AES3 < 0 or Maths3 < 0 or Physics3 < 0 or CreativeDesign < 0 or AES3 > 100 or Maths3 > 100 or Physics3 > 100 or CreativeDesign > 100:
            print("That is not a valid input.")
        else:
            # ALL GOOD! END THE LOOP I.E. BREAK OUT OF THE WHILE LOOP
            print("Thank you, Term 3 is inputted.")
            break
    except:
        # If they don't give a number, print this error message!
        print("That is not a number.")

# Did they progress?
TotalAverage = (AES1+Maths1+Physics1+ComputerProgramming1+AES2+Chemistry1+Maths2+Physics2+AES3+Maths3+Physics3+CreativeDesign)/12
MathsAverage = (Maths2+Maths3)/2

# First check if they scored at least 40% in every subject
if AES1 < 40 or Maths1 < 40 or Physics1 < 40 or ComputerProgramming1 < 40 or AES2 < 40 or Chemistry1 < 40 or Maths2 < 40 or Physics2 < 40 or AES3 < 40 or Maths3 < 40 or Physics3 < 40 or CreativeDesign < 40:
    print("Sorry, you do not progress because you did not get at least 40% in each subject")
elif TotalAverage < 60: # Checks that total average is at least 60
    print("Sorry, you do not progress because you must have at least an average of 60% overall.")
elif MathsAverage < 65: # Averaged 65 in Maths 2 and Maths 3
    print("Sorry, you do not progress because you must have at least an average of 65% in Maths 2 and Maths 3.")
elif AES3 < 60: # Got at least 60 in AES Term 3
    print("Sorry, you do not progress because you must score at least 60 in Term 3 in AES.")
else: # Otherwise they progessed (no failures)
    print("WELL DONE :) YOU PROGRESS!!")

# QUIT
quit()