while True:
	first = float (input("введите первое число: "))
	simbol = input ("укжите операцию:(+,-,/,*,^) ")
	second = float(input ("введите второе число: "))
	if simbol == "+":
		answer = first + second 
		print("ответ: " + str(answer))
		oper = ["no", 'N', 'No', 'net']
		cont = input("повторить? Y/N ")
		if cont in oper:
			print("операция завершена")
			break


	elif simbol == "-":
		answer = first - second 
		print("ответ: " + str(answer))
		cont = input("повторить? Y/N")
		if cont == "N":
			print("операция завершена")
			break
	
	elif simbol == "/":
		if int (second) != 0:
			answer = first/second
			print ("ответ: " + str (answer))
			cont = input("repit? Y/N")
			if cont == "N" :
				break
		else:
			print ("деление на ноль невозможно!")
			cont = input("pepit ?")
			if cont == "N":
				break

	elif simbol == "*":
		answer = first * second 
		print("ответ: " + str(answer))
		cont = input("повторить? Y/N")
		if cont == "N":
			print("операция завершена")
			break
	elif simbol == "^":
		answer = first ** second 
		print("ответ: " + str(answer))
		cont = input("повторить? Y/N")
		if cont == "N":
			print("операция завершена")
			break
	else:
		print ("упс ошибка!")
