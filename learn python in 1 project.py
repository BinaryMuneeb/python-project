import random
MAX_LINES=3
MAX_BET=1000
MIN_BET=1
ROWS=3
COLS=3
symbol_count={
    'A':2,
    'B':3,
    'C':6,
    'D':8,
}
symbol_value={
    'A':5,
    'B':4,
    'C':3,
    'D':2,
}
def check_wining(columns,lines,bet,values):
    winings=0
    winings_lines=[]
    for line in range(lines):
        symbol=columns[0][line]
        for column in columns:
            symbol_to_check=column[line]
            if symbol!=symbol_to_check:
                break
        else:
            winings+=values[symbol]*bet
            winings_lines.append(lines)
    return winings,winings_lines




def get_slot_machine_spin(rows,cols,symbols):
    all_symbol=[]
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbol.append(symbol)
    columns=[]
    for _ in range(cols):
        column=[]
        current_symbols= all_symbol[:]
        for _ in range(rows):
            value=random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i!=len(columns)-1:
                print(column[row],'|',end='')
            else:
                print(column[row],end='')
        print()


def deposit():
    while True:
        amount=input('enter the amount would you like to deposit? $')
        if amount.isdigit():
            amount=int(amount)
            if amount > 0:
                break
            else:
                print('please enter rhe must be greater then zero')
        else:
            print('enter the number')
    return amount

def get_the_number_of_lines():
    while True:
        lines=input('enter the munber of linees to bet on(1-'+str(MAX_LINES)+')?')
        if lines.isdigit():
            lines=int(lines)
            if 1<= lines <= MAX_LINES:
                break
            else:
                print('please enter the valid number of lines')
        else:
            print('enter the number')
    return lines    
def get_bet():
    while True:
        amount=input('how many amount would you like to bet in eqch line? $')
        if amount.isdigit():
            amount=int(amount)
            if MIN_BET<= amount <=MAX_BET :
                break
            else:
                print(f'please enter the amount between {MIN_BET}-{MAX_BET}')
        else:
            print('enter the number')
    return amount
def game(balance):
    lines=get_the_number_of_lines()
    while True:
        bet=get_bet()
        total_bet=bet*lines
        if total_bet>balance:
            print(f'you do not have enugh amout to bet,your current balance is {balance}$')
        else:
            break
    print(f'you are betting ${bet} on {lines} lines . total bet is equal {total_bet}')
    slots=get_slot_machine_spin(ROWS,COLS,symbol_count)
    print_slot_machine(slots)
    
    winings,winings_lines=check_wining(slots,lines,bet,symbol_value)
    print(f'you won $ {winings}')
    print(f'you won on lines',*winings_lines)
    return winings-total_bet

def main():
    balance=deposit()
    while True:
        print(f'your current balance is ${balance}.')
        spin=input('enter if you wont  to spin again(q for quit)')
        if spin=='q':
            break
        balance+=game(balance)
    print(f'your current balance is {balance}')

main()