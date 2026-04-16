# Definindo o tamanho em KB
tamanho_kb = 100
# 1 KB = 1024 bytes. Cada caractere 'a' ocupa 1 byte.
tamanho_bytes = tamanho_kb * 1024

# Gerando a string
conteudo = 'a' * tamanho_bytes

# 1. Salvar em um arquivo .txt para conferência
nome_arquivo = "payload_100kb.txt"
with open(nome_arquivo, "w") as f:
    f.write(conteudo)

print(f"Arquivo '{nome_arquivo}' gerado com sucesso!")
print(f"Tamanho real: {tamanho_bytes} bytes (~100 KB)")
print("-" * 30)
print("DICA: Copie o conteúdo do arquivo e cole no campo 'body' do seu blackbox.yml")
