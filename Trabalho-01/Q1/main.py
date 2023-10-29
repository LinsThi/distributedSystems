from Q1.entities.PessoaOutputSteam import PessoaOutputStream
from Q1.entities.PessoaInputStream import PessoaInputStream
from Q1.entities.OutputStream import *
from Q1.entities.InputStream import *

def main():
    # Criando as 2 opções de input de pessoas (TCP fica no lado do servidor)
    console_input_stream = PessoaInputConsoleStream();
    file_input_stream = PessoaInputFileStream();

    # Criando as 3 opções de print de pessoas
    print_stream = PessoaPrintStream();
    file_stream = PessoaFileStream();
    tcp_stream = PessoaTCPStream();


    # Criando objeto para leitura
    # pessoa_input_stream = PessoaInputStream([], console_input_stream)
    pessoa_input_stream = PessoaInputStream([], file_input_stream)

    pessoa_input_stream.read_system()

    # Criando objeto para escrita
    pessoa_output_stream = PessoaOutputStream(pessoa_input_stream.people, print_stream)
    # pessoa_output_stream = PessoaOutputStream(pessoa_input_stream.people, file_stream)
    # pessoa_output_stream = PessoaOutputStream(pessoa_input_stream.people, tcp_stream)
    pessoa_output_stream.write_system();

if __name__ == "__main__":
    main()