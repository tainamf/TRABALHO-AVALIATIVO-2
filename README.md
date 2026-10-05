# TRABALHO-AVALIATIVO-2
# Relatório e Documentação: Sistema de Locadora de Veículos

## 1. Identificação de Classes
* `Veiculo` (Superclasse abstrata) / `Carro`, `Caminhao` (Subclasses)
* `Cliente` (Superclasse abstrata) / `PessoaFisica`, `PessoaJuridica` (Subclasses)
* `Contrato`
* `Condutor`
* `Manutencao`

---

## 2. Atributos e Métodos por Classe

* **Veiculo**
  * *Atributos:* `placa`, `modelo`, `ano`, `valor_diaria`, `_manutencoes`
  * *Métodos:* `registrar_manutencao()`, `custo_total_manutencao()`, `calcular_aluguel()` (abstrato)
* **Carro / Caminhao**
  * *Atributos:* Atributos herdados + `numero_portas` ou `capacidade_carga`
  * *Métodos:* Implementação específica de `calcular_aluguel()`
* **Cliente**
  * *Atributos:* `nome`, `documento`, `telefone`
* **Contrato**
  * *Atributos:* `cliente`, `veiculo`, `data_inicio`, `data_termino`, `status`, `condutor`, `valor_total`
  * *Métodos:* `calcular_valor_total()`, `finalizar()`, `cancelar()`
* **Condutor**
  * *Atributos:* `nome`, `numero_cnh`
  * *Métodos:* `validar_cnh()`
* **Manutencao**
  * *Atributos:* `data`, `tipo_servico`, `custo`

---

## 3. Herança e Polimorfismo
* **Hierarquia de Veículos:** A classe abstrata `Veiculo` padroniza o comportamento base, enquanto as subclasses (`Carro`, `Caminhao`) implementam as regras próprias de cálculo de diária (polimorfismo).
* **Hierarquia de Clientes:** A superclasse `Cliente` centraliza os dados comuns, permitindo e para pessoas físicas ou jurídicas.

---

## 4. Relacionamentos entre Classes
* **Contrato ↔ Condutor (Composição):** O condutor é instanciado diretamente dentro do contrato e depende dele para existir no escopo da regra de negócio.
* **Veículo ↔ Manutenção (Agregação / 1 para N):** Um veículo mantém uma lista de registros de manutenção ao longo do tempo.
* **Contrato ↔ Cliente / Veículo (Associação):** O contrato referencia instâncias já existentes de cliente e veículo.

    print("Condutor:", contrato.condutor)
    print("CNH válida?", contrato.condutor.validar_cnh())
    print("Valor total: R$", contrato.valor_total)

    carro.registrar_manutencao(date(2026, 9, 1), "Troca de óleo", 250.0)
    carro.registrar_manutencao(date(2026, 9, 20), "Alinhamento", 120.0)
    print("Custo total de manutenção: R$", carro.custo_total_manutencao())
