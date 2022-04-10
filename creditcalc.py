import math
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--type', )
parser.add_argument('--principal', type=float)
parser.add_argument('--periods', type=int)
parser.add_argument('--interest', type=float)
parser.add_argument('--payment', type=float)
args = parser.parse_args()


def principal_paying(payment, period, interest):
    i = interest / (12 * 100)
    A = payment / ((i * pow((1 + i), period)) / (pow((1 + i), period) - 1))
    overpayment = (period * payment) - A
    print(f'Your loan principal = {math.floor(A)}!')
    print(f'Overpayment = {math.ceil(overpayment)}')


def annuity_payments(principal, period, interest):
    i = interest / (12 * 100)
    annuity_payment = math.ceil(principal * ((i * pow((1 + i), period)) / (pow((1 + i), period) - 1)))
    overpayment = int(annuity_payment * period - principal)
    print(f'Your monthly payment = {annuity_payment}!')
    print(f'Overpayment = {overpayment}')


def differentiated_payments(principal, period, interest):
    over = []
    i = interest / (12 * 100)
    for count in range(1, period + 1):
        D = math.ceil((principal / period) + i * (principal - (principal * (count - 1) / period)))
        print(f'Month {count}: payment is {D}')
        over.append(D)
    overpayment = int(sum(over) - principal)
    print()
    print(f'Overpayment = {overpayment}')


def annuity_how_long(principal, payment, interest):
    i = interest / (12 * 100)
    num_month = math.ceil(math.log((payment / (payment - i * principal)), 1 + i))
    years = math.floor(num_month / 12)
    month = math.ceil(num_month / 12 - years + 1)
    overpayment = int(num_month * payment - principal)
    if years == 1:
        print(f'It will take {years} year and {month} months to repay this loan!')
    else:
        print(f'It will take {years} years and {month} months to repay this loan!')
    print(f'Overpayment = {overpayment}')


if args.type == 'diff':
    try:
        differentiated_payments(principal=args.principal, period=args.periods, interest=args.interest)
    except TypeError:
        print('Incorrect parameters.')

elif args.type == 'annuity' and args.periods is None:
    try:
        annuity_how_long(principal=args.principal, payment=args.payment, interest=args.interest)
    except TypeError:
        print('Incorrect parameters.')

elif args.type == 'annuity' and args.payment is not None:
    try:
        principal_paying(payment=args.payment, period=args.periods, interest=args.interest)
    except TypeError:
        print('Incorrect parameters.')
elif args.type == 'annuity':
    try:
        annuity_payments(principal=args.principal, period=args.periods, interest=args.interest)
    except TypeError:
        print('Incorrect parameters.')
