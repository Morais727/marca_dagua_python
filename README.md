# Marca d'água em PDF com Python

Este projeto oferece uma solução para adicionar marca d'água em arquivos PDF, permitindo inserir tanto texto quanto imagens. Ele foi desenvolvido em Python usando as bibliotecas `PyMuPDF` (`fitz`) e `Pillow`. Com este código, você pode personalizar a marca d'água, definindo tamanho, rotação, opacidade e posição centralizada nas páginas do PDF.

## Requisitos

Instale as bibliotecas necessárias:

```bash
pip install pymupdf pillow
```

## Funcionalidades

O projeto fornece três funções principais:

1. **`add_text_watermark`**: Adiciona uma marca d'água de texto em um arquivo PDF. Você pode personalizar o texto, o tamanho da fonte, a rotação e a opacidade.

2. **`add_image_watermark`**: Adiciona uma marca d'água de imagem em um arquivo PDF. Permite definir a imagem, a rotação, a opacidade e o fator de escala.

3. **`add_watermark`**: Função principal que decide entre adicionar uma marca d'água de texto ou de imagem, dependendo dos parâmetros fornecidos.

## Uso

Abaixo, um exemplo de uso do código para adicionar uma marca d'água de texto e uma marca d'água de imagem:

```python
# Exemplo de uso
input_pdf = 'exemplo.pdf'
output_pdf_text = 'arquivo_com_marca_dagua_texto.pdf'
output_pdf_image = 'arquivo_com_marca_dagua_imagem.pdf'

# Adicionar marca d'água de texto
add_watermark(input_pdf, output_pdf_text, text="CONFIDENCIAL", font_path="DeliusUnicase-Bold.ttf", font_size=30, rotation=135, opacity=0.3)

# Adicionar marca d'água de imagem
add_watermark(input_pdf, output_pdf_image, image_path="Rag.png", rotation=135, opacity=0.3, scale=0.5)
```

### Parâmetros

- **input_pdf**: Caminho para o PDF de entrada.
- **output_pdf**: Caminho para salvar o PDF com a marca d'água.
- **text**: (Opcional) Texto a ser usado como marca d'água. Requer o parâmetro `font_path`.
- **font_path**: (Opcional) Caminho para o arquivo de fonte `.ttf` para o texto da marca d'água.
- **font_size**: (Opcional) Tamanho da fonte para o texto.
- **image_path**: (Opcional) Caminho para a imagem a ser usada como marca d'água.
- **rotation**: Ângulo de rotação da marca d'água (para texto e imagem).
- **opacity**: Opacidade da marca d'água, com valores entre 0 e 1.
- **scale**: (Opcional) Fator de escala para ajustar o tamanho da imagem.

### Funções

#### `add_text_watermark(input_pdf, output_pdf, text, font_path, font_size, rotation, opacity)`

Adiciona uma marca d'água de texto no centro de cada página do PDF.

#### `add_image_watermark(input_pdf, output_pdf, image_path, rotation, opacity, scale=1.0)`

Adiciona uma marca d'água de imagem no centro de cada página do PDF.

#### `add_watermark(input_pdf, output_pdf, text=None, font_path=None, font_size=30, image_path=None, rotation=0, opacity=0.3, scale=1.0)`

Função principal que decide se usará `add_text_watermark` ou `add_image_watermark` com base nos parâmetros fornecidos. Levanta um erro se nem `text` nem `image_path` forem fornecidos.

---

## Observações

- Para usar uma marca d'água de texto, forneça os parâmetros `text` e `font_path`.
- Para usar uma marca d'água de imagem, forneça o parâmetro `image_path`.
- É necessário um PDF de entrada e um caminho para salvar o PDF de saída.

## Licença

Este projeto é distribuído sob a licença MIT. Consulte o arquivo [LICENSE](./LICENSE) para mais detalhes.
