# Set inputs to be invalid
validTerm1 = False
validTerm2 = False
validTerm3 = False

# Input loop for term 1
while validTerm1 == False:
    try:
        print(" # # # Term 1 # # #")
        term1AES = float(input("AES: "))
        term1Mathterm1AES = float(input("Maths 1: "))
        term1Physicterm1AES = float(input("Physics 1: "))
        term1ComputerProgramming1 = float(input("Computer Programming 1: "))
    except:
        print("That is not a number.")
    if term1AES < 0 or term1Mathterm1AES < 0 or term1Physicterm1AES < 0 or term1ComputerProgramming1 < 0 or term1AES > 100 or term1Mathterm1AES > 100 or term1Physicterm1AES > 100 or term1ComputerProgramming1 > 100:
        print("That is not a valid input.")
    else:
        print("Thank you, Term 1 is inputted.")
        validTerm1 = True

# Input loop for term 2
while validTerm2 == False:
    try:
        print(" # # # Term 2 # # #")
        term2AES = float(input("AES: "))
        term2Chemistry1 = float(input("Chemistry 1: "))
        term2Mathterm1Mathterm1AES = float(input("Maths 2: "))
        term2Physicterm1Mathterm1AES = float(input("Physics 2: "))
    except:
        print("That is not a number.")
    if term2AES < 0 or term2Chemistry1 < 0 or term2Mathterm1Mathterm1AES < 0 or term2Physicterm1Mathterm1AES < 0 or term2AES > 100 or term2Chemistry1 > 100 or term2Mathterm1Mathterm1AES > 100 or term2Physicterm1Mathterm1AES > 100:
        print("That is not a valid input.")
    else:
        print("Thank you, Term 2 is inputted.")
        validTerm2 = True

# Input loop for term 3
while validTerm3 == False:
    try:
        print(" # # # Term 3 # # ")
        term3AES = float(input("AES: "))
        term3Mathterm1Physicterm1AES = float(input("Maths 3: "))
        term3Physicterm1Physicterm1AES = float(input("Physics 3: "))
        term3CreativeDesign = float(input("Creative Design: "))
    except:
        print("That is not a number.")
    if term3AES < 0 or term3Mathterm1Physicterm1AES < 0 or term3Physicterm1Physicterm1AES < 0 or term3CreativeDesign < 0 or term3AES > 100 or term3Mathterm1Physicterm1AES > 100 or term3Physicterm1Physicterm1AES > 100 or term3CreativeDesign > 100:
        print("That is not a valid input.")
    else:
        print("Thank you, Term 3 is inputted.")
        validTerm3 = True

# Calculates average for all 12 and for Maths 2 and 3
average1 = (term1AES+term1Mathterm1AES+term1Physicterm1AES+term1ComputerProgramming1+term2AES+term2Chemistry1+term2Mathterm1Mathterm1AES+term2Physicterm1Mathterm1AES+term3AES+term3Mathterm1Physicterm1AES+term3Physicterm1Physicterm1AES+term3CreativeDesign)/12
average2 = (term2Mathterm1Mathterm1AES+term3Mathterm1Physicterm1AES)/2

# Check if progress conditions are met
if average1 < 60:
    print("Sorry, you did not progress because your average was",average1,"which is less than 60.")
elif term1AES < 40 or term1Mathterm1AES < 40 or term1Physicterm1AES < 40 or term1ComputerProgramming1 < 40 or term2AES < 40 or term2Chemistry1 < 40 or term2Mathterm1Mathterm1AES < 40 or term2Physicterm1Mathterm1AES < 40 or term3AES < 10 or term3Mathterm1Physicterm1AES < 40 or term3Physicterm1Physicterm1AES < 40 or term3CreativeDesign < 40:
    print("Sorry, you did not progress because you must score at least 40 in each subject.")
elif term3AES < 60:
    print("Sorry, you did not progress because you must score at least 60 in Term 3 in AES")
elif average2 < 65:
    print("Sorry, you did not progress because you averaged",average2,"in Maths 2 and 3 which is less than 65.")
else:
    print("Well done, you progressed! :)")

#Quit
quit()