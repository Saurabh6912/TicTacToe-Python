import random
def check(board) :
    x = 'a'
    for i in range(3):
        for j in range(3):
            x = board[i][j]
            if x==" " :
                return True
    return False
CHOICE = int(input('Enter 1 if you want to play with Bot 2 if want to play with frnd : '))
row1 = [" "," "," "]
row2 = [" "," "," "]
row3 = [" "," "," "]


map = [row1,row2,row3]
# horizontal = random.randint(0,2) 
# vertical = random.randint(0,2) 
# selected_row = map[horizontal]
# selected_row[vertical] = 'O'
print(f"{row1}\n{row2}\n{row3}")

# position = input("Player-1 Move\nWhere do you want to put the treasure? : ")
# horizontal = int(position[0])-1 #2
# vertical = int(position[1])-1
i=0
cndn = False
if CHOICE==1:
    position = input("Where do you want to put the treasure? place(Enter as ixj) : ")
    horizontal = int(position[0])-1 #2
    vertical = int(position[1])-1
    while cndn == False :
        if i%2==0 and check(map) == True:
            while(map[horizontal][vertical] != " "):

                position = input("Where do you want to put the treasure place(Enter as ixj),put at blank place? : ")
                # if user enter 23 then
                horizontal = int(position[0])-1 #2
                vertical = int(position[1])-1 #3

            selected_row = map[horizontal]
            selected_row[vertical] = 'X'

            print('Your Move --\n\n')
            print(f"{row1}\n{row2}\n{row3}")
            print('\n\n')
            if (map[0][0] == 'X' and map[0][1] == 'X' and map[0][2] == 'X'):
                cndn = True
                print('You won the game!')
                break
            elif (map[0][0] == 'X' and map[1][0] == 'X' and map[2][0] == 'X'):
                cndn = True
                print('You won the game!')
                break
            elif (map[2][0] == 'X' and map[2][1] == 'X' and map[2][2] == 'X'):
                cndn = True
                print('You won the game!')
                break
            elif (map[0][2] == 'X' and map[1][2] == 'X' and map[2][2] == 'X'):
                cndn = True
                print('You won the game!')
                break
            elif (map[0][0] == 'X' and map[1][1] == 'X' and map[2][2] == 'X'):
                cndn = True
                print('You won the game!')
                break
            elif (map[0][2] == 'X' and map[1][1] == 'X' and map[2][0] == 'X'):
                cndn = True
                print('You won the game!')
                break
            elif (map[0][1] == 'X' and map[1][1] == 'X' and map[2][1] == 'X'):
                cndn = True
                print('You won the game!')
                break
            elif (map[1][0] == 'X' and map[1][1] == 'X' and map[1][2] == 'X'):
                cndn = True
                print('You won the game!')
                break
            else:
                cndn = False

        elif i%2!=0 and check(map) == True:
            while(map[horizontal][vertical] != " "):
                horizontal = random.randint(0,2) #2
                vertical = random.randint(0,2) #3
            selected_row = map[horizontal]
            selected_row[vertical] = 'O'

            print('Boat Move --\n\n')
            print(f"{row1}\n{row2}\n{row3}")
            print('\n\n')
            if (map[0][0] == 'O' and map[0][1] == 'O' and map[0][2] == 'O'):
                cndn = True
                print('Bot won the game,You loss!')
                break
            elif (map[0][0] == 'O' and map[1][0] == 'O' and map[2][0] == 'O'):
                cndn = True
                print('Bot won the game,You loss!')
                break
            elif (map[2][0] == 'O' and map[2][1] == 'O' and map[2][2] == 'O'):
                cndn = True
                print('Bot won the game,You loss!')
                break
            elif (map[0][2] == 'O' and map[1][2] == 'O' and map[2][2] == 'O'):
                cndn = True
                print('Bot won the game,You loss!')
                break
            elif (map[0][0] == 'O' and map[1][1] == 'O' and map[2][2] == 'O'):
                cndn = True
                print('Bot won the game,You loss!')
                break
            elif (map[0][2] == 'O' and map[1][1] == 'O' and map[2][0] == 'O'):
                cndn = True
                print('Bot won the game,You loss!')
                break
            elif (map[0][1] == 'O' and map[1][1] == 'O' and map[2][1] == 'O'):
                cndn = True
                print('Bot won the game,You loss!')
                break
            elif (map[1][0] == 'O' and map[1][1] == 'O' and map[1][2] == 'O'):
                cndn = True
                print('Bot won the game,You loss!')
                break
            else:
                cndn = False
            
        else:
            print("Game Draw!")
            break
        i = i+1
elif CHOICE==2:
    name1 = input("Enter the name of player-1 : ")
    name2 = input("Enter the name of player-2 : ")
    print(name1)
    position = input("Where do you want to put the treasure? place(Enter as ixj) : ")
    horizontal = int(position[0])-1 #2
    vertical = int(position[1])-1
    while cndn == False :
        if i%2==0 and check(map) == True:
            print(f"{name1}'s Move --\n\n")
            while(map[horizontal][vertical] != " "):

                position = input("Where do you want to put the treasure place(Enter as ixj),put at blank place? : ")
                # if user enter 23 then
                horizontal = int(position[0])-1 #2
                vertical = int(position[1])-1 #3

            selected_row = map[horizontal]
            selected_row[vertical] = 'X'

            print(f"{row1}\n{row2}\n{row3}")
            print('\n\n')
            if (map[0][0] == 'X' and map[0][1] == 'X' and map[0][2] == 'X'):
                cndn = True
                print(name1,' won the game!')
                break
            elif (map[0][0] == 'X' and map[1][0] == 'X' and map[2][0] == 'X'):
                cndn = True
                print(name1,' won the game!')
                break
            elif (map[2][0] == 'X' and map[2][1] == 'X' and map[2][2] == 'X'):
                cndn = True
                print(name1,' won the game!')
                break
            elif (map[0][2] == 'X' and map[1][2] == 'X' and map[2][2] == 'X'):
                cndn = True
                print(name1,' won the game!')
                break
            elif (map[0][0] == 'X' and map[1][1] == 'X' and map[2][2] == 'X'):
                cndn = True
                print(name1,' won the game!')
                break
            elif (map[0][2] == 'X' and map[1][1] == 'X' and map[2][0] == 'X'):
                cndn = True
                print(name1,' won the game!')
                break
            elif (map[0][1] == 'X' and map[1][1] == 'X' and map[2][1] == 'X'):
                cndn = True
                print(name1,' won the game!')
                break
            elif (map[1][0] == 'X' and map[1][1] == 'X' and map[1][2] == 'X'):
                cndn = True
                print(name1,' won the game!')
                break
            else:
                cndn = False

        elif i%2!=0 and check(map) == True:
            print(f"{name2}'s Move--\n\n")
            while(map[horizontal][vertical] != " "):

                position = input("Where do you want to put the treasure place(Enter as ixj),put at blank place? : ")
                # if user enter 23 then
                horizontal = int(position[0])-1 #2
                vertical = int(position[1])-1 #3
            selected_row = map[horizontal]
            selected_row[vertical] = 'O'

            print(f"{row1}\n{row2}\n{row3}")
            print('\n\n')
            if (map[0][0] == 'O' and map[0][1] == 'O' and map[0][2] == 'O'):
                cndn = True
                print(name2,' won the game!')
                break
            elif (map[0][0] == 'O' and map[1][0] == 'O' and map[2][0] == 'O'):
                cndn = True
                print(name2,' won the game!')
                break
            elif (map[2][0] == 'O' and map[2][1] == 'O' and map[2][2] == 'O'):
                cndn = True
                print(name2,' won the game!')
                break
            elif (map[0][2] == 'O' and map[1][2] == 'O' and map[2][2] == 'O'):
                cndn = True
                print(name2,' won the game!')
                break
            elif (map[0][0] == 'O' and map[1][1] == 'O' and map[2][2] == 'O'):
                cndn = True
                print(name2,' won the game!')
                break
            elif (map[0][2] == 'O' and map[1][1] == 'O' and map[2][0] == 'O'):
                cndn = True
                print(name2,' won the game!')
                break
            elif (map[0][1] == 'O' and map[1][1] == 'O' and map[2][1] == 'O'):
                cndn = True
                print(name2,' won the game!')
                break
            elif (map[1][0] == 'O' and map[1][1] == 'O' and map[1][2] == 'O'):
                cndn = True
                print(name2,' won the game!')
                break
            else:
                cndn = False
            
        else:
            print("Game Draw!\n\n")
            break
        i = i+1
else :
    print("Inorrect input!")
# j=0

        
