# Remover Fundo de Imagem com Python 🖼️

Este projeto utiliza a biblioteca [rembg](https://github.com/danielgatis/rembg) para remover o fundo de imagens de forma automática e eficiente.

## 🚀 Funcionalidades

- Remoção de fundo de imagens.
- Suporte para salvar imagens com transparência (formato PNG).
- Fácil de usar e configurar.

## 📦 Requisitos

- Python 3.7 ou superior.
- As seguintes bibliotecas Python:
  - `rembg`
  - `Pillow`

## 🛠️ Instalação

1. **Clone este repositório**:
   ```bash
   git clone https://github.com/bbeltrame01/RemoveBackground.git
   cd RemoveBackground
   ```

2. **Crie um ambiente virtual (opcional, mas recomendado)**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. **Instale as dependências**:
   ```bash
   pip install rembg pillow
   ```

## 🖥️ Uso

### Executando o script:

1. Inclua sua imagem dentro da pasta `/images` com o nome `input.jpg`.
2. Execute o script:
   ```bash
   python main.py
   ```
3. O resultado será salvo como `output.png` no mesmo diretório.

## 🖼️ Exemplo de antes e depois:

| Antes | Depois |
|-------|--------|
| ![Antes](./images/input.jpg) | ![Depois](./images/output.png) |

## 📝 Observações

- O formato de saída padrão é PNG, pois suporta transparência.
- Imagens bem iluminadas e com contraste claro entre o objeto e o fundo geram melhores resultados.

## 🤝 Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir **issues** ou enviar um **pull request**.