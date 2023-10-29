from Q1.entities.PessoaOutputSteam import PessoaOutputStream
from Q1.entities.OutputStream import *
from Q1.entities.Pessoa import Pessoa

def main():
    people_list = [Pessoa('Marcos', 123456789, 30), Pessoa('Judite', 123456789, 23), ]

    # Criando as 3 opções de print de pessoas
    print_stream = PessoaPrintStream();
    file_stream = PessoaFileStream();
    tcp_stream = PessoaTCPStream();

    # Criando objeto para escrita
    pessoa_output_stream = PessoaOutputStream(people_list, print_stream)
    # pessoa_output_stream = PessoaOutputStream(people_list, file_stream)
    # pessoa_output_stream = PessoaOutputStream(people_list, tcp_stream)
    pessoa_output_stream.write_system();

if __name__ == "__main__":
    main()