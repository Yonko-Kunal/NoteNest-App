print("  ")
print("{WELCOM USER TO KBC KAUN BANEGA CROREPATI}")
print("~~~~~~~~~RULES~~~~~~~~~~")
print("Their will be of total 10 Questions,each question will have 4 options and only one of them will be the right answer on every correct answer you will win cash rewards ")
print("cash price on every answer \n 1st question 10,000Rs \n 2nd question 30,000Rs \n 3rd question 60,000Rs \n 4th question 1,00,000Rs \n 5th question 2,00,000Rs \n 6th question 4,00,000Rs \n 7th question 8,00,000Rs \n 8th question 1,00,00,000Rs \n 9th question 3,00,00,000Rs \n 10th question 7,00,00,000Rs")

# print("Question No. 1")
# print("What is the name of the current President of America")
# question1 = ["(a) Donald Trump", "(b) Vladimir Putin",
#              "(c) Joe Biden", "(d)Barack Obama "]
# print(question1)

# answer1 = input("What is your answer :")

# print(question1.index("(b) Vladimir Putin"))
# if (answer1 == question1[0]):
#     print("Sorry, you have answered worng the correct answer is option (c) Joe Biden well better luck next time")
# elif (answer1 == question1[1]):
#     print("Sorry, you have answered worng the correct answer is option (c) Joe Biden well better luck next time")
# elif (answer1 == question1[2]):
#     print("Excellent !! your answer and absolutely correct, you won your 1st price 10,000Rs")
# elif (answer1 == question1[3]):
#     print("Sorry, you have answered worng the correct answer is option (c) Joe Biden well better luck next time")

questions = [
    [f"What is the name of the current President of America", "(a) Donald Trump", "(b) Vladimir Putin",
     "(c) Joe Biden", "(d)Barack Obama ", 3],
    [f"What is the name of the current President of America", "(a) Donald Trump", "(b) Vladimir Putin",
     "(c) Joe Biden", "(d)Barack Obama ", 3],
    [f"What is the name of the current President of America", "(a) Donald Trump", "(b) Vladimir Putin",
     "(c) Joe Biden", "(d)Barack Obama ", 3],
    [f"What is the name of the current President of America", "(a) Donald Trump", "(b) Vladimir Putin",
     "(c) Joe Biden", "(d)Barack Obama ", 3],
    [f"What is the name of the current President of America", "(a) Donald Trump", "(b) Vladimir Putin",
     "(c) Joe Biden", "(d)Barack Obama ", 3],
    [f"What is the name of the current President of America", "(a) Donald Trump", "(b) Vladimir Putin",
     "(c) Joe Biden", "(d)Barack Obama ", 3],
    [f"What is the name of the current President of America", "(a) Donald Trump", "(b) Vladimir Putin",
     "(c) Joe Biden", "(d)Barack Obama ", 3],
    [f"What is the name of the current President of America", "(a) Donald Trump", "(b) Vladimir Putin",
     "(c) Joe Biden", "(d)Barack Obama ", 3],
    [f"What is the name of the current President of America", "(a) Donald Trump", "(b) Vladimir Putin",
     "(c) Joe Biden", "(d)Barack Obama ", 3],
    [f"What is the name of the current President of America", "(a) Donald Trump", "(b) Vladimir Putin",
     "(c) Joe Biden", "(d)Barack Obama ", 3],
    [f"What is the name of the current President of America", "(a) Donald Trump", "(b) Vladimir Putin",
     "(c) Joe Biden", "(d)Barack Obama ", 3],
    [f"What is the name of the current President of America", "(a) Donald Trump", "(b) Vladimir Putin",
     "(c) Joe Biden", "(d)Barack Obama ", 3],
    [f"What is the name of the current President of America", "(a) Donald Trump", "(b) Vladimir Putin",
     "(c) Joe Biden", "(d)Barack Obama ", 3],
    [f"What is the name of the current President of America", "(a) Donald Trump", "(b) Vladimir Putin",
     "(c) Joe Biden", "(d)Barack Obama ", 3],
    [f"What is the name of the current President of America", "(a) Donald Trump", "(b) Vladimir Putin",
     "(c) Joe Biden", "(d)Barack Obama ", 3],
    [f"What is the name of the current President of America", "(a) Donald Trump", "(b) Vladimir Putin",
     "(c) Joe Biden", "(d)Barack Obama ", 3],
    [f"What is the name of the current President of America", "(a) Donald Trump", "(b) Vladimir Putin",
     "(c) Joe Biden", "(d)Barack Obama ", 3],

]
levels = [
    "1,000", "2,000", "3,000", "5,000", "10,000", "20,000", "40,000", "80,000", "1,60,000", "3,20,000", "6,40,000", "12,50,000", "25,00,000", "50,00,000", "75,00,000", "1,00,00,000", "7,50,00,000"
]

for i in range(0, len(questions)):
    question = questions[i]
    print(f"your question for Rs {levels[i]} on your screen")
    print(f"{question[1]}        {question[2]}")
    print(f"{question[3]}        {question[4]}")
    answer = int(input("Select the correct option 1-4 :"))
    if (answer == question[5]):
        print(f"Excellint !! You have won {levels[i]}")
    else:
        print("sorry your answer is wrong")
