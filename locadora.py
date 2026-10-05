from abc import ABC, abstractmethod
from datetime import date


class Condutor:
    

    def __init__(self, nome: str, numero_cnh: str):
        self.nome = nome
        self.numero_cnh = numero_cnh

    def validar_cnh(self) -> bool:
        return len(self.numero_cnh) == 11 and self.numero_cnh.isdigit()

    def __str__(self):
        return f"{self.nome} (CNH: {self.numero_cnh})"


class Contrato:
    

    def __init__(self, cliente, veiculo, data_inicio: date,
                 data_termino: date, nome_condutor: str, cnh_condutor: str):
        self.cliente = cliente              
        self.veiculo = veiculo              
        self.data_inicio = data_inicio
        self.data_termino = data_termino
        self.status = "ativo"

        self.condutor = Condutor(nome_condutor, cnh_condutor)

        self.valor_total = self.calcular_valor_total()

    def calcular_valor_total(self) -> float:
        dias = (self.data_termino - self.data_inicio).days
        return self.veiculo.calcular_aluguel(dias)

    def finalizar(self):
        self.status = "finalizado"

    def cancelar(self):
        self.status = "cancelado"

    def __del__(self):
        self.condutor = None




class Manutencao:
    def __init__(self, data: date, tipo_servico: str, custo: float):
        self.data = data
        self.tipo_servico = tipo_servico
        self.custo = custo


class Veiculo(ABC):
    def __init__(self, placa: str, modelo: str, ano: int, valor_diaria: float):
        self.placa = placa
        self.modelo = modelo
        self.ano = ano
        self.valor_diaria = valor_diaria
        self._manutencoes: list[Manutencao] = []   

    def registrar_manutencao(self, data: date, tipo_servico: str, custo: float):
        self._manutencoes.append(Manutencao(data, tipo_servico, custo))

    def custo_total_manutencao(self) -> float:
        return sum(m.custo for m in self._manutencoes)

    @abstractmethod
    def calcular_aluguel(self, dias: int) -> float:
        ...




class Carro(Veiculo):
    def __init__(self, placa, modelo, ano, valor_diaria, numero_portas: int):
        super().__init__(placa, modelo, ano, valor_diaria)
        self.numero_portas = numero_portas

    def calcular_aluguel(self, dias: int) -> float:
        return self.valor_diaria * dias


class Caminhao(Veiculo):
    def __init__(self, placa, modelo, ano, valor_diaria, capacidade_carga: float):
        super().__init__(placa, modelo, ano, valor_diaria)
        self.capacidade_carga = capacidade_carga

    def calcular_aluguel(self, dias: int) -> float:
        return self.valor_diaria * dias * 1.10   




class Cliente(ABC):
    def __init__(self, nome: str, documento: str, telefone: str):
        self.nome = nome
        self.documento = documento
        self.telefone = telefone


class PessoaFisica(Cliente):
    pass


class PessoaJuridica(Cliente):
    pass




if __name__ == "__main__":
    cliente = PessoaFisica("Maria Silva", "123.456.789-00", "(86) 99999-0000")
    carro = Carro("ABC1D23", "Onix", 2023, 150.0, 4)

    contrato = Contrato(
        cliente=cliente,
        veiculo=carro,
        data_inicio=date(2026, 10, 5),
        data_termino=date(2026, 10, 10),
        nome_condutor="João Souza",
        cnh_condutor="12345678901",
    )

    print("Condutor:", contrato.condutor)
    print("CNH válida?", contrato.condutor.validar_cnh())
    print("Valor total: R$", contrato.valor_total)

    carro.registrar_manutencao(date(2026, 9, 1), "Troca de óleo", 250.0)
    carro.registrar_manutencao(date(2026, 9, 20), "Alinhamento", 120.0)
    print("Custo total de manutenção: R$", carro.custo_total_manutencao())