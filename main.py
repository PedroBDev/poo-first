try:
    from pessoa import People
except ImportError as e:
    print(f"Erro ao importar o módulo: {e}")
    exit()

def parse_input(message):
    while True:
        response = input(message).strip().upper()
        if response in ('S', 'N'):
            return response == 'S'
        else:
            print("Por favor, responda apenas com 'S' ou 'N'.")

if __name__ == "__main__":
    name = input('Qual seu nome? ')

    while True:
        try:
            age = int(input('Qual sua idade? '))
            break
        except ValueError:
            print("Por favor, insira um número válido para a idade.")

    run = parse_input('Você está correndo? [S/N] ')
    eat = parse_input('Você está comendo? [S/N] ')

    pessoa_1 = People(name, age)
    pessoa_1.run(run)
    pessoa_1.eat(eat)




