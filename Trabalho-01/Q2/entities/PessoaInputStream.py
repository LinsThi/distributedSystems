import io
from typing import List
from Q2.entities.InputStream import InputStream


class PessoaInputStream(io.IOBase):
    def __init__(self, people: List[str], is_: InputStream):
        self.people = people
        self.is_ = is_

    def read_system(self, newPeople=None):
        self.is_.read(self.people, newPeople)