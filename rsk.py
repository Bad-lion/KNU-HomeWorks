game = ["R",'S',"P"]
import random
while 1 :
    guess = input("your turn ")
    comp = random.choice(game)
    if guess.upper() == comp:
    	print(f'comp choise {comp}')
    	print ('draw')
    elif guess.upper() != comp:
        if guess.upper() == "S":
            if comp == "R":
            	print(f'comp choise {comp}')
                print("you lose")

            elif comp == "P":
            	print(f'comp choise {comp}')
                print('you win')
                b = input("you want exit?")
                if b.upper() == 'Y':
                    break
                else :
                    continue
        if guess.upper() == "R":
            if comp == "P":
            	print(f'comp choise {comp}')
                print("you lose")
            elif comp == "S":
            	print(f'comp choise {comp}')
                print('you win')
                b = input("you want exit?")
                if b.upper() == 'Y':
                    break
                else :
                    continue
        if guess.upper() == "P":
            if comp == "S":
            	print(f'comp choise {comp}')
                print("you lose")
            elif comp == "R":
            	print(f'comp choise {comp}')
                print('you win')
                b = input("you want exit?")
                if b.upper() == 'Y':
                    break
                else :
                    continue
        else :
            print('this command no this game')