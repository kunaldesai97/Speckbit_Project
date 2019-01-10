import csv
import random

with open('questions.csv') as csvfile: #Read CSV File
    readCSV = csv.reader(csvfile, delimiter = ',')
    question_no = []
    questions = []
    choices = [[]]
    answers = []
    i = 0
    choices = [[] for i in range(5)]
    for row in readCSV: #Separate into question numbers, questions, choices and answers
        question_no.append(row[0])
        questions.append(row[1])
        choices[i].append(row[2])
        choices[i].append(row[3])
        choices[i].append(row[4])
        choices[i].append(row[5])
        answers.append(row[6])
        i+=1

while(True):
    c = int(input('1.Play Quiz\n2.Exit\n'))
    points = 0
    numbers = []
    if c==1: #Play quiz
        while len(numbers)<3:
            n = random.randrange(len(question_no)) #Select random question numbers
            if n not in numbers:
                numbers.append(n)
        #Display questions and choices, ask for an answer and evaluate it
        for i in range(len(numbers)):
            print('Question %d' % (i+1))
            print(questions[numbers[i]])
            print('Your choices are')
            for j in choices[numbers[i]]:
                print(j)
            ans = input('Enter your answer\n')
            ans = ans.strip(' ')
            if ans.lower() ==  answers[numbers[i]].lower():
                print('Your answer is correct\n')
                points+=1
            else:
                print('Wrong answer, the correct answer is: %s\n' % answers[numbers[i]])
        print('Your score: %d\n' % points)

    elif c==2:
        break;

    else:
        print('Invalid Option')
