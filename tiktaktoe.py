thetheBoard = {
    '1':' ', '2':' ', '3':' '
    , '4':' ','5':' ','6':' '
    ,'7':' ','8':' ','9':' '
}
theBoard_keys = []

for key in thetheBoard:
    theBoard_keys.append(key)

def printtheBoard(theBoard):
    print(theBoard['7']+'|'+ theBoard['8']+ '|' + theBoard['9'])
    print ('-+-+-')
    print(theBoard['4']+'|'+ theBoard['5']+ '|' + theBoard['6'])
    print ('-+-+-')
    print(theBoard['1']+'|'+ theBoard['2']+ '|' + theBoard['3'])

def game():
    turn = 'X'
    count = 0

    for i in range(10):
        printtheBoard(thetheBoard)
        print("it's your turn ," + turn + '.Move to which place?')

        move = input()

        if thetheBoard[move] ==' ':
            thetheBoard[move] = turn
            count +=1
        else:
            print("That place is allready filled. \n")
            continue

        if count >=5 :
            if thetheBoard['7'] == thetheBoard['8'] == thetheBoard['9'] != ' ':
                printtheBoard(thetheBoard)
                print('\nGame Over.\n')
                print('*****' + turn +' Won. ******')
                break

            elif thetheBoard['4'] == thetheBoard['5'] == thetheBoard['6'] != ' ':
                printtheBoard(thetheBoard)
                print('\nGame Over.\n')
                print('*****' + turn +' Won. ******')
                break

            elif  thetheBoard['1'] == thetheBoard['2'] == thetheBoard['3'] != ' ':
                printtheBoard(thetheBoard)
                print('\nGame Over.\n')
                print('*****' + turn +' Won. ******')
                break
            elif  thetheBoard['1'] == thetheBoard['4'] == thetheBoard['7'] != ' ':
                printtheBoard(thetheBoard)
                print('\nGame Over.\n')
                print('*****' + turn +' Won. ******')
                break
            elif  thetheBoard['2'] == thetheBoard['5'] == thetheBoard['8'] != ' ':
                printtheBoard(thetheBoard)
                print('\nGame Over.\n')
                print('*****' + turn +' Won. ******')
                break
            elif thetheBoard['3'] == thetheBoard['6'] == thetheBoard['9'] != ' ':
                printtheBoard(thetheBoard)
                print('\nGame Over.\n')
                print('*****' + turn +' Won. ******')
                break
            elif thetheBoard['7'] == thetheBoard['5'] == thetheBoard['3'] != ' ':
                printtheBoard(thetheBoard)
                print('\nGame Over.\n')
                print('*****' + turn +' Won. ******')
                break
            elif thetheBoard['1'] == thetheBoard['5'] == thetheBoard['9'] != ' ':
                printtheBoard(thetheBoard)
                print('\nGame Over.\n')
                print('*****' + turn +' Won. ******')
                break
        if count == 9 :
            print('\nGameOver.\n')
            print("it's a Tie!")
        
        if turn == 'X' :
            turn ='O'
        else:

            turn = 'X'
    
    

    restart = input('Do want to play Again?(y/n)')
    if restart == 'y' or restart == 'Y':
        for key in theBoard_keys:
            thetheBoard[key] = ' '

       
if __name__ == '__main__':
    game()