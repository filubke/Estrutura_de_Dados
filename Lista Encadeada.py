class Nodo:
	def __init__(self, numero, cor):
		self.numero = numero
		self.cor = cor
		self.proximo = None

	def __str__(self):
		return f"[{self.cor}-{self.numero}]"

class ListaEncadeada:
	def __init__(self):
		self.head = None
		self.proximo_numero_v = 1
		self.proximo_numero_a = 201

	def inserirSemPrioridade(self, novo_nodo):
		if self.head is None:
			self.head = novo_nodo
			return
		atual = self.head
		while atual.proximo is not None:
			atual = atual.proximo
		atual.proximo = novo_nodo
		print(f"Paciente {novo_nodo} adicionado ao final da fila.")

	def inserirComPrioridade(self, novo_nodo):
		if self.head is None:
			self.head = novo_nodo
			print(f"Paciente {novo_nodo} adicionado como primeiro da fila.")
			return
		if self.head.cor == 'V':
			novo_nodo.proximo = self.head
			self.head = novo_nodo
			print(f"Paciente {novo_nodo} adicionado como primeiro da fila de prioridade.")
			return
		atual = self.head
		anterior = None
		while atual is not None and atual.cor == 'A':
			anterior = atual
			atual = atual.proximo
		if anterior is not None:
			novo_nodo.proximo = atual
			anterior.proximo = novo_nodo
			print(f"Paciente {novo_nodo} adicionado no final da fila de prioridade.")
		else:
			novo_nodo.proximo = self.head
			self.head = novo_nodo
			print(f"Paciente {novo_nodo} adicionado no início da fila de prioridade.")

	def inserir(self):
		while True:
			cor = input("Digite a cor do cartão (A para Amarelo, V para Verde): ").upper()
			if cor in ['A', 'V']:
				break
			else:
				print("Cor inválida. Por favor, digite 'A' ou 'V'.")
		numero = 0
		if cor == 'V':
			numero = self.proximo_numero_v
			self.proximo_numero_v += 1
		elif cor == 'A':
			numero = self.proximo_numero_a
			self.proximo_numero_a += 1
		novo_nodo = Nodo(numero, cor)
		if self.head is None:
			self.head = novo_nodo
			print(f"Paciente {novo_nodo} adicionado como primeiro da fila.")
		elif cor == 'V':
			self.inserirSemPrioridade(novo_nodo)
		elif cor == 'A':
			self.inserirComPrioridade(novo_nodo)

	def imprimirListaEspera(self):
		if self.head is None:
			print("A fila de espera está vazia.")
			return
		print("Fila de Espera:")
		atual = self.head
		fila_str = ""
		while atual is not None:
			fila_str += str(atual)
			if atual.proximo is not None:
				fila_str += " -> "
			atual = atual.proximo
		print(fila_str)

	def atenderPaciente(self):
		if self.head is None:
			print("Não há pacientes na fila para atendimento.")
			return
		paciente_atendido = self.head
		self.head = self.head.proximo
		print(f"Chamando paciente para atendimento: Cartão {paciente_atendido.cor}{paciente_atendido.numero}.")

def menu():
	lista_espera = ListaEncadeada()
	while True:
		print("\n--- Menu do Sistema de Triagem ---")
		print("1 - Adicionar paciente à fila")
		print("2 - Mostrar pacientes na fila")
		print("3 - Chamar paciente")
		print("4 - Sair")
		opcao = input("Escolha uma opção: ")
		if opcao == '1':
			lista_espera.inserir()
		elif opcao == '2':
			lista_espera.imprimirListaEspera()
		elif opcao == '3':
			lista_espera.atenderPaciente()
		elif opcao == '4':
			print("Encerrando o programa.")
			break
		else:
			print("Opção inválida. Por favor, escolha uma opção de 1 a 4.")

if __name__ == "__main__":
	menu()