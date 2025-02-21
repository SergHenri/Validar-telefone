import re  # Importa o módulo 're' (expressões regulares) que fornece funções para trabalhar com padrões de texto.

# Função para validar o número de telefone
def validate_numero_telefone(phone_number):  # Define a função 'validate_numero_telefone' que recebe um número de telefone como argumento.
    # Define o padrão da expressão regular para o formato (XX) 9XXXX-XXXX
    pattern = r"^\(\d{2}\) 9\d{4}-\d{4}$"  # Define a expressão regular para validar o formato do número de telefone: (XX) 9XXXX-XXXX.
    # A expressão regular:
    # ^: Início da string
    # \(\d{2}\): "(XX)" com 2 dígitos numéricos
    # 9: O número deve começar com 9
    # \d{4}: 4 dígitos numéricos
    # -: Um hífen
    # \d{4}: Mais 4 dígitos numéricos
    # $: Fim da string
    
    # Verifica se o número de telefone corresponde ao padrão
    if re.match(pattern, phone_number):  # Usa a função 're.match()' para verificar se a string 'phone_number' corresponde ao padrão 'pattern'.
        return "Número de telefone válido."  # Se corresponder, retorna "Número de telefone válido."
    else:
        return "Número de telefone inválido."  # Se não corresponder, retorna "Número de telefone inválido."

# Solicita ao usuário que insira um número de telefone
phone_number = input('Informe o numero de telefone: ')  # Usa a função 'input()' para pedir ao usuário um número de telefone e armazena o valor em 'phone_number'.

# Chama a função para validar o número de telefone
result = validate_numero_telefone(phone_number)  # Chama a função 'validate_numero_telefone' passando 'phone_number' como argumento e armazena o resultado em 'result'.

# Imprime o resultado
print(result)  # Exibe o resultado da validação na tela (se é válido ou inválido).
