import time
import os

dicionario = {
    '1)': {
        'pergunta': 'Escreva aqui sua pergunta: ',
        'respostas': {
            'a': 'Escolha1',
            'b': 'Escolha2',
            'c': 'Escolha3',
            'd': 'Escolha4',
        },
        'resposta_correta': 'a',  # Coloque a resposta correta
    },
    '2)': {
        'pergunta': 'Escreva aqui sua pergunta: ',
        'respostas': {
            'a': 'Escolha1',
            'b': 'Escolha2',
            'c': 'Escolha3',
            'd': 'Escolha4',
        },
        'resposta_correta': 'd',  # Coloque a resposta correta
    },
    '3)': {
        'pergunta': 'Escreva aqui sua pergunta: ',
        'respostas': {
            'a': 'Escolha1',
            'b': 'Escolha2',
            'c': 'Escolha3',
            'd': 'Escolha4',
        },
        'resposta_correta': 'a',  # Coloque a resposta correta
    },
    '4)': {
        'pergunta': 'Escreva aqui sua pergunta: ',
        'respostas': {
            'a': 'Escolha1',
            'b': 'Escolha2',
            'c': 'Escolha3',
            'd': 'Escolha4',
        },
        'resposta_correta': 'c',  # Coloque a resposta correta
    },
    '5)': {
        'pergunta': 'Escreva aqui sua pergunta: ',
        'respostas': {
            'a': 'Escolha1',
            'b': 'Escolha2',
            'c': 'Escolha3',
            'd': 'Escolha4',
            'e': 'Escolha5'
        },
        'resposta_correta': 'd',  # Coloque a resposta correta
    }
}


class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[38;5;14m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[38;5;118m'
    YELLOW = '\033[38;5;226m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'
    PINK = '\033[38;5;206m'



os.system('cls' if os.name == 'nt' else 'clear')
print()
inicio = "Seja bem vindx ao questionario!\n"
print(Color.BOLD, Color.PINK, Color.UNDERLINE + f"{inicio}" + Color.END)
r = Color.RED
n = Color.END
b = Color.BOLD
result = 0
for mq, ma in dicionario.items():
    print(Color.BOLD, Color.CYAN + f"{mq}: {ma['pergunta']}" + Color.END)
    print(Color.BOLD, Color.CYAN + "Answers:" + Color.END)
    print()
    for aq, aa in ma['respostas'].items():
        print(Color.GREEN + f"[{aq}]: {aa}" + Color.END)
        print()
    answer = input(f"{Color.YELLOW}Wich is the answer? {r}{b}")
    if answer.lower() == ma['resposta_correta']:
        print(f"{Color.CYAN}Opaa, você acertou!!!")
        print(f"{b}{Color.CYAN}Indo para a proxima pergunta...{n}")
        time.sleep(2)
        result += 1
    else:
        print(f"{Color.CYAN}Infelizmente não foi dessa vez, você errou!")
        print(f"A resposta certa era {Color.RED}{ma['resposta_correta'].upper()} {n}")
        print(f"{b}{Color.CYAN}Indo para a proxima pergunta...{n}")
        time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
qtd_q = len(dicionario)
p = result / qtd_q * 100
print(f"{Color.GREEN}Você acertou {r}{result}/{len(dicionario)}{Color.GREEN} questões{n}")
print(f"{Color.GREEN}A sua porcentagem foi de {r}{p}%")
time.sleep(5)
exit()
