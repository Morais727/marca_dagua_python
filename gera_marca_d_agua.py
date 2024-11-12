import fitz  # PyMuPDF
from PIL import Image, ImageDraw, ImageFont
import io

def add_text_watermark(input_pdf, output_pdf, text, font_path, font_size, rotation, opacity):
    pdf_document = fitz.open(input_pdf)
    
    # Define as propriedades da marca d'água
    watermark = Image.new('RGBA', (500, 500), (255, 255, 255, 0))
    draw = ImageDraw.Draw(watermark)
    
    # Configura a fonte
    font = ImageFont.truetype(font_path, font_size)
    text_width, text_height = draw.textsize(text, font=font)
    
    # Define a posição centralizada do texto na imagem da marca d'água
    text_position = ((watermark.width - text_width) / 2, (watermark.height - text_height) / 2)
    draw.text(text_position, text, fill=(0, 0, 0, int(255 * opacity)), font=font)
    
    # Rotaciona a marca d'água corretamente
    watermark = watermark.rotate(rotation, expand=True)
    
    # Converte a imagem de marca d'água para bytes e depois para Pixmap
    byte_io = io.BytesIO()
    watermark.save(byte_io, format='PNG')
    byte_io.seek(0)
    
    # Insere a marca d'água em cada página centralizada
    for page_number in range(pdf_document.page_count):
        page = pdf_document[page_number]
        page_width, page_height = page.rect.width, page.rect.height
        
        # Cria o Pixmap diretamente do objeto de bytes
        pix = fitz.Pixmap(byte_io)
        
        # Calcula a posição para centralizar a marca d'água na página
        x = (page_width - pix.width) / 2
        y = (page_height - pix.height) / 2
        
        # Insere a imagem da marca d'água na posição centralizada
        page.insert_image(fitz.Rect(x, y, x + pix.width, y + pix.height), pixmap=pix, overlay=True)

    pdf_document.save(output_pdf)

def add_image_watermark(input_pdf, output_pdf, image_path, rotation, opacity, scale=1.0):
    pdf_document = fitz.open(input_pdf)
    
    # Abre a imagem da marca d'água e aplica escala
    image = Image.open(image_path).convert("RGBA")
    width, height = image.size
    image = image.resize((int(width * scale), int(height * scale)), Image.LANCZOS)
    
    # Aplica a opacidade
    alpha = image.split()[3]
    alpha = alpha.point(lambda p: p * opacity)
    image.putalpha(alpha)
    
    # Rotaciona a imagem da marca d'água
    image = image.rotate(rotation, expand=True)
    
    # Converte a imagem de marca d'água para bytes e depois para Pixmap
    byte_io = io.BytesIO()
    image.save(byte_io, format='PNG')
    byte_io.seek(0)
    
    # Insere a marca d'água em cada página centralizada
    for page_number in range(pdf_document.page_count):
        page = pdf_document[page_number]
        page_width, page_height = page.rect.width, page.rect.height
        
        # Cria o Pixmap diretamente do objeto de bytes
        pix = fitz.Pixmap(byte_io)
        
        # Calcula a posição para centralizar a marca d'água na página
        x = (page_width - pix.width) / 2
        y = (page_height - pix.height) / 2
        
        # Insere a imagem da marca d'água na posição centralizada
        page.insert_image(fitz.Rect(x, y, x + pix.width, y + pix.height), pixmap=pix, overlay=True)

    pdf_document.save(output_pdf)

def add_watermark(input_pdf, output_pdf, text=None, font_path=None, font_size=30, image_path=None, rotation=0, opacity=0.3, scale=1.0):
    if text and font_path:
        add_text_watermark(input_pdf, output_pdf, text, font_path, font_size, rotation, opacity)
    elif image_path:
        add_image_watermark(input_pdf, output_pdf, image_path, rotation, opacity, scale)
    else:
        raise ValueError("Você deve fornecer um texto com caminho para a fonte ou um caminho para uma imagem.")

# Exemplo de uso
input_pdf = 'exemplo.pdf'
output_pdf_text = 'arquivo_com_marca_dagua_texto.pdf'
output_pdf_image = 'arquivo_com_marca_dagua_imagem.pdf'

# Adicionar marca d'água de texto
# add_watermark(input_pdf, output_pdf_text, text="CONFIDENCIAL", font_path="DeliusUnicase-Bold.ttf", font_size=30, rotation=135, opacity=0.3)

# Adicionar marca d'água de imagem
add_watermark(input_pdf, output_pdf_image, image_path="Rag.png", rotation=180, opacity=0.3, scale=0.5) 
