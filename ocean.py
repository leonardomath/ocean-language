globals_variables = []

def show(line, index=None):
	variable_name = line.split('(')[1]
	variable_name = variable_name[:-2]

	for index, value in enumerate(globals_variables):
		if variable_name in globals_variables[index].keys():
			print(globals_variables[index][variable_name][0]['value'])

def gets_value(variable_name, index):
	value = input('')
	globals_variables[index][variable_name][0]['value'] = value

def gets(input, index):
	if not input:
		print('invalid syntax')

	variable = input
	variable_name = variable.split(' = ')[0]
	message = variable.split(' = ')[1]

	message = message[6:-3]

	globals_variables.append({
		variable_name: [
			{'message': message},
			{'value': None}
		]
	})

	print(message)
	gets_value(variable_name, index)


while True:
	user_input = input('Ocean>> ')
	if user_input == 'ocean --v':
		print('Ocean version 0.1')
	
	if 'ocean run' in user_input:
		program_name = user_input[10:len(user_input)+1]

		program = open(program_name, 'r')
		contador = 0
		for index,line in enumerate(program):
			if 'gets' in line:
				gets(line, contador)
				contador+=1
			elif 'show' in line:
				show(line)
			else:
				continue

	if user_input == 'get':
	    gets()

	

	
