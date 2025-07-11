import os

def addRevisionBits():
    questionsAmount = int(input("How many questions would you like to add (make sure you know the answer to them or have them available): "))
    subject = input("Which subject is it for? ").lower()
    for i in range(questionsAmount):
        question = input("Question: ")
        answer = input("Main points of the answer: ")
        with open(f"Subjects/{subject}.txt", "a+") as f:
            f.write(f"{question}\n")
        with open(f"Subjects/{subject}Answers.txt", "a+") as f:
            f.write(f"{answer}\n")
        
def readRevision():
    subject = input("Which subject would you like to revise? ").lower()
    with open(f"Subjects/{subject}.txt", "r+") as f:
        revision = f.readlines()
    for questions in revision:
        print(questions)
        next = input("Press enter when you are done.")
        if not next:
            continue
        else:
            continue

def poseQuestions():
    subject = input("Which subject would you like to revise? ").lower()
    with open(f"Subjects/{subject}.txt", "r+") as f:
        revision = f.readlines()
    with open(f"{subject}Answers.txt", "r") as f:
        answers = f.readlines()
    for questions in revision:
        print(checkAnswers(answer=input(f"{questions}: "), mainPoints=answers[revision.index(questions)].split(" ")))

def checkAnswers(answer, mainPoints) -> str:
    removedPoints = []
    length = len(mainPoints)
    print(length)
    answer = answer.split(" ")
    mainPoint = 0
    for words in answer:
        if words in mainPoints:
            mainPoint += 1
            removedPoints.append(mainPoints.pop(mainPoint - 1))

    print(mainPoint)
    
    if mainPoint == length:
        return "You got the answer correct!"
    elif (mainPoint + 1) == length:
        return f"You got it almost right! You were just missing 1 point which was: {''.join(mainPoints)}"
    elif (mainPoint + 2) == length:
        return f"You nearly got it! You were just missing 2 points which were: {' | '.join(mainPoints)}"
    else:
        return f"You either got it wrong or missed on a lot of very important points which were: {' | '.join(mainPoints)}"

def main():
    while True:
        options = input("""
    (1) Add A Section To Revise
    (2) Read A Section
    (3) Answer Questions On A Section
    (Q) Quit
    """).lower()
        if options == "1":
            addRevisionBits()
        elif options == "2":
            readRevision()
        elif options == "3":
            poseQuestions()
        elif options == "q":
            quit()
        else:
            print("Invalid Request.")
            continue

if __name__ == "__main__":
    main()