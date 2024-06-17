MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100


def deposit():
    while True:
        amount = input('Enter an amount you want to deposit : $')
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            print('Amount must be greater than 0')
        print('Please enter a number')

    return amount

def get_number_of_lines():
    while True:
        lines = input('Enter the number of lines ton bet on (1-'+ str(MAX_LINES) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            print('Enter a valid number of lines.')
        print('Please enter a number')

    return lines

def get_bet():
    while True:
        bet = input('How much would you like to bet : $')
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            print(f'Bet must be in between {MIN_BET} - {MAX_BET}')
        print('Please enter a number')

    return bet


def main():
    balance = deposit()
    lines = get_number_of_lines()
    
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f'You do not have enough balance to bet ${total_bet}. Your current balance is ${balance}')
        else:
            break

    print(f'You are betting ${bet} on {lines} lines. Total bet is ${total_bet}')


main()
