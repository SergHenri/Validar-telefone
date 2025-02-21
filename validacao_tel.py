import re

# Função para validar o número de telefone
def validate_numero_telefone(phone_number):
    # Define o padrão da expressão regular para o formato (XX) 9XXXX-XXXX
    pattern = r"^\(\d{2}\) 9\d{4}-\d{4}$"
    
    # Verifica se o número de telefone corresponde ao padrão
    if re.match(pattern, phone_number):
        return "Número de telefone válido."
    else:
        return "Número de telefone inválido."

# Solicita ao usuário que insira um número de telefone
phone_number = input('Informe o numero de telefone: ')

# Chama a função para validar o número de telefone
result = validate_numero_telefone(phone_number)

# Imprime o resultado
print(result)
