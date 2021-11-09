import re


# Processar um LOG em txt - Traze-lo para o ambiente python (Foi usado um txt com o mesmo conteudo da questão)
arquivo = open('Oficina2.txt')

# Listas a serem preenchidas com os dados colhidos
errorDias=[]
errorHorarios=[]
errorHora=[]

# Processar linha a linha em busca das informações
def processarDatasEHorarios():
    for line in arquivo.readlines():
        if re.search(r'ERROR', line) != None:
            errorDias.append(re.findall(r'\d{4}\W\d{2}\W\d{2}', line))
            errorHorarios.append(re.findall(r'\d{2}\W\d{2}\W\d{2}\W\d{3}', line))

# Subdivido os horários em itens de lista para depois processar as horas separadamente
def subDividirHoras():
    for i in range(len(errorHorarios)):
        errorHora.append(re.findall(r'\d{2}', errorHorarios[i][0])) # Não consegui "puxar" só as horas, então aqui puxo hora,min,sec,milisec e depois processo somente as horas

# Separação das horas
def selecaoDeHoras():
    for i in range(len(errorHora)):
        errorHora[i]= errorHora[i][0]

# Processamento dos passos anteriores para um posterior que depende deles
processarDatasEHorarios()
subDividirHoras()
selecaoDeHoras()

# Verificar qual mais se repete
def maisFrequentes(errorHora):
	counter = 0
	num = errorHora[0]
	
	for i in errorHora:
		curr_frequency = errorHora.count(i)
		if(curr_frequency> counter):
			counter = curr_frequency
			num = i

	return num


print("A quantidade de ERRORs é:", len(errorDias), "\nO horário em que mais acontecem é entre", maisFrequentes(errorHora), "e", str(0) + str(int(maisFrequentes(errorHora))+1), "horas.")

arquivo.close()