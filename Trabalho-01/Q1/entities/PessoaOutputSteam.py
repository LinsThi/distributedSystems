import io
from typing import List
from Q1.entities.OutputStream import OutputStream

class PessoaOutputStream(io.IOBase):
    def __init__(self, people: List[str], os_: OutputStream):
        self.people = people
        self.os_ = os_
    
    def write_system(self):
        lengthPeople = len(self.people)
        title = f'Quantidade de pessoas: {lengthPeople}\n\n'
        message = self.os_.write(title, self.people)
        return message