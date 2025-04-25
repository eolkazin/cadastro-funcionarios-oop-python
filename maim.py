# Sistema de Gestão de Funcionários
class Funcionario:
    def __init__(self, nome, cargo, salario_base):
        self.nome = nome
        self.cargo = cargo
        self.salario_base = salario_base
        self.horas_extras = 0

    def calcular_salario(self):
        # Salário com horas extras (10% por hora extra)
        salario_extra = self.horas_extras * (self.salario_base * 0.1)
        return self.salario_base + salario_extra

    def adicionar_horas_extras(self, horas):
        self.horas_extras += horas

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Cargo: {self.cargo}")
        print(f"Salário Base: R${self.salario_base:.2f}")
        print(f"Horas Extras: {self.horas_extras}")
        print(f"Salário Total: R${self.calcular_salario():.2f}")
        print("-" * 30)


# Criando a classe Empresa para gerenciar os funcionários
class Empresa:
    def __init__(self, nome):
        self.nome = nome
        self.funcionarios = []

    def contratar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

    def exibir_relatorio(self):
        print(f"Relatório da Empresa: {self.nome}")
        print("=" * 30)
        for funcionario in self.funcionarios:
            funcionario.exibir_dados()


# Criando a empresa
empresa = Empresa("Tech Solutions")

# Criando funcionários
f1 = Funcionario("Lucas", "Desenvolvedor", 3500)
f2 = Funcionario("Ana", "Gerente", 5500)
f3 = Funcionario("João", "Designer", 3000)

# Adicionando horas extras
f1.adicionar_horas_extras(10)
f2.adicionar_horas_extras(5)

# Contratando funcionários
empresa.contratar_funcionario(f1)
empresa.contratar_funcionario(f2)
empresa.contratar_funcionario(f3)

# Exibindo o relatório completo
empresa.exibir_relatorio()
