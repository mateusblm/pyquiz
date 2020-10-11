import time
import os

dictionary = {
    '1)': {
        'question': 'Write here your question:  ',
        'answers': {
            'a': 'Choice 1',
            'b': 'Choice 2',
            'c': 'Choice 3',
            'd': 'Choice 4',
        },
        'right_answer': 'a',  # Put the right answer
    },
    '2)': {
        'question': 'Write here your question:  ',
        'answers': {
            'a': 'Choice 1',
            'b': 'Choice 2',
            'c': 'Choice 3',
            'd': 'Choice 4',
        },
        'right_answer': 'd',  # Put the right answer
    },
    '3)': {
        'question': 'Write here your question:  ',
        'answers': {
            'a': 'Choice 1',
            'b': 'Choice 2',
            'c': 'Choice 3',
            'd': 'Choice 4',
        },
        'right_answer': 'a',  # Put the right answer
    },
    '4)': {
        'question': 'Write here your question:  ',
        'answers': {
            'a': 'Choice 1',
            'b': 'Choice 2',
            'c': 'Choice 3',
            'd': 'Choice 4',
        },
        'right_answer': 'c',  # Put the right answer
    },
    '5)': {
        'question': 'Write here your question:  ',
        'answers': {
            'a': 'Choice 1',
            'b': 'Choice 2',
            'c': 'Choice 3',
            'd': 'Choice 4',
            'e': 'Choice 5'
        },
        'right_answer': 'd',  # Put the right answer
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
start = "Welcome to the Quiz!\n"
print(Color.BOLD, Color.PINK, Color.UNDERLINE + f"{start}" + Color.END)
r = Color.RED
n = Color.END
b = Color.BOLD
result = 0
for mq, ma in dictionary.items():
    print(Color.BOLD, Color.CYAN + f"{mq}: {ma['question']}" + Color.END)
    print(Color.BOLD, Color.CYAN + "Answers:" + Color.END)
    print()
    for aq, aa in ma['answers'].items():
        print(Color.GREEN + f"[{aq}]: {aa}" + Color.END)
        print()
    answer = input(f"{Color.YELLOW}Wich is the answer? {r}{b}")
    if answer.lower() == ma['right_answer']:
        print(f"{Color.CYAN}Wow, you got it right!!!")
        print(f"{b}{Color.CYAN}Going to the next question...{n}")
        time.sleep(2)
        result += 1
    else:
        print(f"{Color.CYAN}Ops, unfortunately it wasn't this time!")
        print(f"The right answer was {Color.RED}{ma['right_answer'].upper()} {n}")
        print(f"{b}{Color.CYAN}Going to the next question...{n}")
        time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
qtd_q = len(dictionary)
p = result / qtd_q * 100
print(f"{Color.GREEN}You got {r}{result}/{len(dictionary)}{Color.GREEN} questions right{n}")
print(f"{Color.GREEN}Its percentage is {r}{p}%")
time.sleep(5)
exit()
