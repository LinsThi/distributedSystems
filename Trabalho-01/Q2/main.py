from Q1.entities.PessoaOutputSteam import PessoaOutputStream
from Q2.entities.PessoaInputStream import PessoaInputStream
from Q1.entities.OutputStream import *
from Q2.entities.InputStream import *

def main():
    # Criando as 2 opções de input de pessoas (TCP fica no lado do servidor)
    console_input_stream = PessoaInputConsoleStream();
    file_input_stream = PessoaInputFileStream();

    # Criando as 3 opções de print de pessoas
    output_print_stream = PessoaOutputPrintStream();
    output_file_stream = PessoaOutputFileStream();
    output_tcp_stream = PessoaOutputTCPStream();


    # Criando objeto para leitura
    # pessoa_input_stream = PessoaInputStream([], console_input_stream)
    pessoa_input_stream = PessoaInputStream([], file_input_stream)

    pessoa_input_stream.read_system()

    # Criando objeto para escrita
    pessoa_output_stream = PessoaOutputStream(pessoa_input_stream.people, output_print_stream)
    # pessoa_output_stream = PessoaOutputStream(pessoa_input_stream.people, output_file_stream)
    # pessoa_output_stream = PessoaOutputStream(pessoa_input_stream.people, output_tcp_stream)
    pessoa_output_stream.write_system();

if __name__ == "__main__":
    main()