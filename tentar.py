def divisao(a, b):
    try:
        resultado = a/b
        print(f"O resultado da divisão de {a} por {b} é {resultado}.")
    
    # Caso os parâmetros fornecidos não sejam numéricos
    except TypeError:
        print("Ambos os valores devem ser números.")
    
    # Caso tente uma divisão por zero
    except ZeroDivisionError:
        print("Não tente dividir por zero.")

    # Captura de erro inesperado
    except Exception as sinistro:
        print(f"Erro inesperado: {sinistro}")

    # O bloco Else é executado se o código dentro do try for bem sucedido
    else:
        print("Divisão realizada com sucesso.")

    # o bloco Finally é sempre executado, independente de erros ou acertos
    finally:
        print("Processo de divisão concluído.")

# Teste 1: Divisão normal
divisao(10, 2)

# Teste 2: Divisão por zero
divisao(10, 0)

# Teste 3: Divisão com tipos inválidos
divisao(10, 'dois')