# Importa a função para analisar comentários a partir de texto
from comment_parser import comment_parser

def mostrar_comentarios():
    """ function to show comments using comment parser"""
  
    codigo = """# comentário

        def soma(a, b):
            #isto e um comentario
            
            b = a+b
            
            return a + b  # comentário
       
    """
        
    p = codigo.splitlines()
    lines = [line for line in p if line.strip()]
    
    print(lines)
    # Extrai comentários diretamente da string
    comentarios = comment_parser.extract_comments_from_str(
        codigo,
        mime='text/x-python'  # especifica que é código Python
    )

    # Exibe os comentários encontrados
    print("--- Comentários encontrados ---")
    for i, c in enumerate(comentarios, start=1):
        print(f"[{i}] {c.text().strip()}")

    def func():
        pass
    
# Executa a função principal
if __name__ == "__main__":
    mostrar_comentarios()
    print(__doc__)
