from rembg import remove
from PIL import Image
import io

# Carregar a imagem de entrada
input_path = "./images/input.jpg"  # Caminho da imagem original
output_path = "./images/output.png"  # Caminho para salvar a imagem sem fundo

# Abrir a imagem
with open(input_path, "rb") as file:
  input_image = file.read()

# Remover o fundo
output_image = remove(input_image)

# Salvar a nova imagem com fundo removido
with open(output_path, "wb") as file:
  file.write(output_image)

print("Fundo removido com sucesso!")
