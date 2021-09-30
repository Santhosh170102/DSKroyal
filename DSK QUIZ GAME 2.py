print("Welcome to Genious Quiz Game!")

playing = input("DO you want to Play__with__MR.Santhosh Quiz?")

if playing.lower() != "yes":
    quit()

print("Okay! let's play_with_Genious SANTHOSH Brain:) ")
score = 0

answer = input("THE FULL FORM OF__GATE exam?")
if answer.lower() == "graduate aptitude test in engineering":
    print("Well said your__CORRECT!")
    print("Mr.SANTHOSH say best of LUCK to you :) ")
    score += 1
else:
    print("SORRY your INCORRECT answer!")

answer = input("What is full form of DNA?")
if answer.lower() == "deoxyribonuclic acid":
    print("Great it's absoutely CORRECT!")
    score += 1
else:
    print("SORRY think AGAIN!")

answer = input("who is intially created the BULB?")
if answer.lower() == "AGASTYA MAHARSHI":
    print("Amaizing again you said Coorect!")
    score +=1
else:
    print("Mr.SANTHOSH saying to TRY AGAIN!")

answer = input("Full FORM OF__ATM?")
if answer.lower() == "automated teller machine":
    print("you say CORRECT answer!")
    score += 1
else:
    print("WRONG ANSWER!")

answer = input("Full Form of__PAN card?")
if answer.lower() == "permenant account number":
    print("yes it's CORRECT!")
else:
    print("it's WRONG!")

answer = input("FIRST UNIVERSITY IN THE WORLD?")
if answer.lower() == "TAKSHA SHILA":
    print("CORRECT answer!")
else:
    print("it's WRONG ANSWER!")

answer = input("FULL FORM OF__IFSC code?")
if answer.lower() == "indian financial system code!":
    print("it's CORRECT!")
else:
    print("sorry this WRONG!")

answer = input("in one gram of DNA can store?")
if answer.lower() == "215 petabytes":
    print("yes it's CORRECT!")
    print("Mr.SANTHOSH KUMAR saying to CONGRATULATION'S!")
    score += 1
else:
    print("it's WRONG answer!")
    
    
print("Mr.SANTHOSH KUMAR gving score for you!")

print("you got " + str(score) + " questions correct!")
print("you got " + str((score / 4) * 100) + "%.")
