import subprocess


def run_mafft(input_file, output_file):
    try:
        # Caminho para o executável MAFFT
        mafft_path = r"C:\Program Files\MAFFT\mafft.bat"

        # Executa o MAFFT
        result = subprocess.run(
            [mafft_path, input_file],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True,
        )

        # Escreve o alinhamento no arquivo de saída
        with open(output_file, "w") as f:
            f.write(result.stdout)
        print(f"Alinhamento salvo em -> {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Erro ao executar o MAFFT -> {e.stderr}")
    except FileNotFoundError as e:
        print(f"MAFFT não encontrado -> {e}")


# Arquivo de entrada e saída
input_file = "sequences.fasta"
output_file = "aligned_sequences.fasta"

# Chama a função para executar o MAFFT
run_mafft(input_file, output_file)
