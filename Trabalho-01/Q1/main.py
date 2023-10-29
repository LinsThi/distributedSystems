from Q1.entities.PessoaOutputSteam import PessoaOutputStream
from Q1.entities.OutputStream import *
from Q1.entities.Pessoa import Pessoa

def main():
    people_list = [Pessoa('Marcos', 123456789, 30), Pessoa('Judite', 123456789, 23), ]

    # Criando as 3 opções de print de pessoas
    output_print_stream = PessoaOutputPrintStream();
    output_file_stream = PessoaOutputFileStream();
    output_tcp_stream = PessoaOutputTCPStream();

    # Criando objeto para escrita
    pessoa_output_stream = PessoaOutputStream(people_list, output_print_stream)
    # pessoa_output_stream = PessoaOutputStream(people_list, output_file_stream)
    # pessoa_output_stream = PessoaOutputStream(people_list, output_tcp_stream)
    pessoa_output_stream.write_system();

if __name__ == "__main__":
    main()