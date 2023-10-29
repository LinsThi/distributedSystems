import io
from Q1.entities.Pessoa import Pessoa
from typing import List

class InputStream (io.IOBase):
  def read(self, people: List[Pessoa], newPerson=None):
    pass
   
class PessoaInputConsoleStream(InputStream):
  def read(self, people: List[Pessoa], newPerson=None):
    name = input("Digite o nome da pessoa:")
    cpf = float(input("Digite o CPF:"))
    age = int(input("Digite a idade:"))

    people.append(Pessoa(name, cpf, age))

class PessoaInputFileStream(InputStream):
  def read(self, people: List[Pessoa], newPerson=None):
    with open('Q1/input/peoples_q1.txt', 'r') as file:
      for line in file:
        line = line.strip()
        arraySplited = line.split(',')
        personInfo = map(lambda arr: arr.split(': ')[1], arraySplited)
        # Pegando os valores separados na linha de cima, e transformando em list para criar uma nova pessoa
        personInfo = list(personInfo)
        newPerson = Pessoa(*personInfo)
        people.append(newPerson)

class PessoaInputTCPStream(InputStream):
  def read(self, people: List[Pessoa], personInfo: str):
    personInfo = personInfo.split(',')
    newPerson = Pessoa(*personInfo)
    people.append(newPerson)