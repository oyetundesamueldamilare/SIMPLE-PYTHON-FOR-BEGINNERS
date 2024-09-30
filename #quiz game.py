#quiz game

questions = ('How many planets are in the solar system:', 'How many days are there in a week: ', 'How many months are there in a year: ', 'How many hours are there in a day: ')
options = (('A. 9', 'B. 10', 'C. 11', 'D. 12'), ('A. 6', 'B. 7', 'C. 8', 'D. 9'), ('A. 9', 'B. 10', 'C. 11', 'D. 12'), ('A. 26', 'B. 21', 'C. 24', 'D. 22'))

answers = ('A', 'B', 'D', 'C')
guesses = []
score = 0
question_num = 0

for question in questions:
    print ('--------------------')
    print (question)
    for option in options [question_num]:
        print (option)

    guess= input('enter A B C or D').upper()
    guesses.append(guess)
    
    if guess == answers [question_num]:
        score+=1
        print ('correct')
    else:
        print ('incorrect')
        print (f'{answers[question_num]} is the correct answer')

    question_num+=1

    print ('answers:', end='')
    for answer in answers:
        print (answer, end= ' ')
    print()
    
    print ('guesses:', end= '')
    for guess in guesses:
        print (guess, end=' ')
    print ()
    print ('------------------')

    print (f'your score is {score}/4')



