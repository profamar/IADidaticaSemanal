import os
import subprocess

# Caminho da imagem e do repositório
image_path = "./path/to/your/image.jpg"
repo_path = "./path/to/your/repository"

# Mensagem de commit
commit_message = "Adiciona imagem de exemplo ao repositório"

# Move para o diretório do repositório
os.chdir(repo_path)

# Adiciona a imagem ao repositório
subprocess.run(["git", "add", image_path], check=True)

# Cria um commit com a mensagem especificada
subprocess.run(["git", "commit", "-m", commit_message], check=True)

# Optional: envia as mudanças para o repositório remoto (GitHub)
subprocess.run(["git", "push"], check=True)

print("Imagem adicionada com sucesso ao repositório!")
