import csv

import requests


# Função para ler os IDs do CSV
def read_ids_from_csv(file_path):
    ids = set()  # Usamos um set para evitar duplicatas
    with open(file_path, mode="r") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            ids.update([row["ITS"], row["BenA"], row["CaM"], row["RPB2"]])
    # Remover 'n.a.' do conjunto de IDs
    ids.discard("n.a.")
    return list(ids)


# Lista de IDs extraídos do CSV
ids = read_ids_from_csv("myenv/csv/genes_ids.csv")

# Juntar os IDs em uma string separada por vírgulas
id_string = ",".join(ids)

# URL base para a requisição E-utilities
base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"

# Parâmetros da requisição
params = {
    "db": "nucleotide",  # Banco de dados
    "id": id_string,  # IDs das sequências
    "rettype": "fasta",  # Tipo de retorno (FASTA)
    "retmode": "text",  # Modo de retorno (texto)
}

# Fazer a requisição
response = requests.get(base_url, params=params, verify=False)

# Verificar se a requisição foi bem sucedida
if response.status_code == 200:
    # Salvar as sequências em um arquivo
    with open("sequences.fasta", "w") as file:
        file.write(response.text)
    print("Sequências salvas em sequences.fasta")
else:
    print(f"Erro na requisição: {response.status_code}")
