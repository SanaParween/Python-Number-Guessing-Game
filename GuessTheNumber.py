import random
    
def BeginGame():
    
    i=random.randint(1,20)
    print('Guess the number \n')
    
    for x in range(0,5):
        ip=int(input())
        if ip>i:
            print('Number entered is greater. Try again with a smaller number \n')
        elif ip<i:
            print('Number entered is smaller. Try again with a greater number \n')
        else:
            print('Viola! You guessed it right!!! YOU WIN! \n')
            break
    if x==4:
        print('You\'re a LOSER! Go TRY AGAIN BIIYYYAAATCHH! \nThe correct answer is: ',i)
        

while True:
    try:
        print('Press 1 for a new game\nPress 2 to exit',end='\n')
        i=int(input())
        if i is not 1 and i is not 2:
            print('Try again!')
            
        if i is 2:
            print('Thanks for your time. Get lost!')
            break

        if i is 1:
            BeginGame()
            print('Play again?')
    except Exception as e:
        print('Better try again with a number this time you jerk!!')
    
