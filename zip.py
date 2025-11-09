import zipfile
import os

def renomear_imagens_em_zip(caminho_zip: str, codigo_prefixo: str):
    diretorio_destino = r"C:\Pasta_VS_CODE\front_end_app\imagens_front\pessoa_preblema_coração"
    extensoes_imagem = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp', '.ico')

    try:
        os.makedirs(diretorio_destino, exist_ok=True)

        print(f"Processando arquivo ZIP: {caminho_zip}")
        print(f"Código de prefixo a ser usado: {codigo_prefixo}")
        
        with zipfile.ZipFile(caminho_zip, 'r') as zip_ref:
            lista_arquivos = zip_ref.namelist()
            contador = 0

            for nome_original_no_zip in lista_arquivos:
                nome_base = os.path.basename(nome_original_no_zip)
                if not nome_base or nome_base.endswith('/'):
                    continue
                
                if nome_base.lower().endswith(extensoes_imagem):
                    novo_nome_com_prefixo = codigo_prefixo + "_" + nome_base
                    caminho_novo = os.path.join(diretorio_destino, novo_nome_com_prefixo)
                    
                    try:
                        conteudo_imagem = zip_ref.read(nome_original_no_zip)
                        with open(caminho_novo, 'wb') as f:
                            f.write(conteudo_imagem)
                            
                        print(f"  ✅ Renomeado: '{nome_base}' -> '{novo_nome_com_prefixo}'")
                        contador += 1
                    except Exception as e:
                        print(f"  ❌ Erro ao processar o arquivo '{nome_original_no_zip}': {e}")
                        
            print(f"\nProcesso concluído! {contador} imagens renomeadas e salvas em '{diretorio_destino}'.")
            
    except FileNotFoundError:
        print(f"ERRO: Arquivo ZIP não encontrado em '{caminho_zip}'.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

# Configurações
NOME_DO_ARQUIVO_ZIP = "dia_5.zip"
CODIGO_DE_PREFIXO = "90a3432e"

if __name__ == "__main__":
    renomear_imagens_em_zip(NOME_DO_ARQUIVO_ZIP, CODIGO_DE_PREFIXO)
