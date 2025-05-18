import os
import click
from Display import *

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def printAppName():
    print("\n\t* * * Komboios de Portugal * * * \n")
      
def printAuthenticationOption():
    print("\t  -- Authentication --   \n")

def printMessage(message):
    print(f'\n{message}\n')

def printNewClientOption():
    print("\t  -- New Client --   \n")

def printNewContractOption():
    print("\t  -- New Contract --   \n")

def printNewTicketOption():
    print("\t  -- New Ticket --   \n")

def printWaitingMenu():
    print("\t  --- Waiting ---    \n")
    print("\nColoque o cartão no leitor.\n")

def printAppMenu():
    print("\t  --- Menu ---    \n")
    print("1- New Client")
    print("2- New Contract")
    print("3- Pay Contract")
    print("4- New Ticket")
    print("5- Add Tickets")
    print("6- Read Card")
    print("\n0- Exit\n")

def inputNewClient():

    new_client = {
        'email': '',
        'first_name': '',
        'last_name': '',
    }

    op = 2
    while op == 2:
        clear()
        printAppName()
        printNewClientOption()
        printNewClientInfo(new_client)
        new_client['email'] = input("Insert the client personal email: ")
        clear()
        printAppName()
        printNewClientOption()
        printNewClientInfo(new_client)
        new_client['first_name'] = input("Insert the client first name: ")
        clear()
        printAppName()
        printNewClientOption()
        printNewClientInfo(new_client)
        new_client['last_name'] = input("Insert the client last name: ")
        #Confirmation
        clear()
        printAppName()
        printNewClientOption()
        printNewClientInfo(new_client)
        print("It's the client info correct?")
        print('1. Yes')
        print('2. No')
        print()
        print('0. Cancel')
        print()
        op = -1
        while op != 0 and op != 1 and op != 2:
            try:
                op = int(str(click.getchar()))
            except ValueError:
                op = -1
    if op == 1:
        return new_client
    return None

def inputNewContract(contracts):

    new_contract = {
        'contract': '',
        'c_zone1': '',
        'c_zone2': '',
        'c_price': '',
        'c_expire': '',
        'c_until': 16*'#',
        'c_zone': 16*'#',
        'c_date': 16*'#',
    }

    op = 2
    while op == 2:
        #Tipo
        clear()
        printAppName()
        printNewContractOption()
        printNewContractInfo(new_contract)
        print('Type of contract:\n')
        types = list(contracts['contracts'].keys())
        for i in range(0,len(types)):
            print(f'{i+1}- {types[i]}\n')
        o = -1
        while o not in [i+1 for i in range(0,len(types))]:
            try:
                o = int(str(click.getchar()))
            except ValueError:
                o = -1
        new_contract['contract'] = types[o-1]
        #Origem
        clear()
        printAppName()
        printNewContractOption()
        printNewContractInfo(new_contract)
        print('From:\n')
        for i in range(0,len(contracts['stops'])):
            print(f'{i+1}- {contracts["stops"][i]}\n')
        o = -1
        while o not in [i+1 for i in range(0,len(contracts['stops']))]:
            try:
                o = int(str(click.getchar()))
            except ValueError:
                o = -1
        new_contract['c_zone1'] = contracts['stops'][o-1]
        #Destino
        clear()
        printAppName()
        printNewContractOption()
        printNewContractInfo(new_contract)
        print('To:\n')
        for i in range(0,len(contracts['stops'])):
            print(f'{i+1}- {contracts["stops"][i]}\n')
        o = -1
        while o not in [i+1 for i in range(0,len(contracts['stops']))]:
            try:
                o = int(str(click.getchar()))
            except ValueError:
                o = -1
        new_contract['c_zone2'] = contracts['stops'][o-1]
        #Price
        zs = 0
        z1 = contracts['stops'].index(new_contract['c_zone1'])
        z2 = contracts['stops'].index(new_contract['c_zone2'])
        if z1 > z2:
            zs = contracts['zones'][z1][z2]
        else:
            zs = contracts['zones'][z2][z1]
        new_contract['c_price'] = f'{contracts["contracts"][new_contract["contract"]][zs]:.2f}'
        #Expire
        new_contract['c_expire'] = str(contracts['expire'])
        #Confirmation
        clear()
        printAppName()
        printNewContractOption()
        printNewContractInfo(new_contract)
        print("It's the contract info correct?")
        print('1. Yes')
        print('2. No')
        print()
        print('0. Cancel')
        print()
        op = -1
        while op != 0 and op != 1 and op != 2:
            try:
                op = int(str(click.getchar()))
            except ValueError:
                op = -1
    if op == 1:
        return new_contract
    return None

def inputNewTicket(contracts):

    new_ticket = {
        'ticket': '',
        't_zone1': '',
        't_zone2': '',
        't_amount': '',
        't_price': '', #helper variable
        't_zone': 16*'#',
        't_date': 16*'#',
    }

    op = 2
    while op == 2:
        #Tipo
        clear()
        printAppName()
        printNewTicketOption()
        printNewTicketInfo(new_ticket)
        print('Type of contract:\n')
        types = list(contracts['tickets'].keys())
        for i in range(0,len(types)):
            print(f'{i+1}- {types[i]}\n')
        o = -1
        while o not in [i+1 for i in range(0,len(types))]:
            try:
                o = int(str(click.getchar()))
            except ValueError:
                o = -1
        new_ticket['ticket'] = types[o-1]
        #Origem
        clear()
        printAppName()
        printNewTicketOption()
        printNewTicketInfo(new_ticket)
        print('From:\n')
        for i in range(0,len(contracts['stops'])):
            print(f'{i+1}- {contracts["stops"][i]}\n')
        o = -1
        while o not in [i+1 for i in range(0,len(contracts['stops']))]:
            try:
                o = int(str(click.getchar()))
            except ValueError:
                o = -1
        new_ticket['t_zone1'] = contracts['stops'][o-1]
        #Destino
        clear()
        printAppName()
        printNewTicketOption()
        printNewTicketInfo(new_ticket)
        print('To:\n')
        for i in range(0,len(contracts['stops'])):
            print(f'{i+1}- {contracts["stops"][i]}\n')
        o = -1
        while o not in [i+1 for i in range(0,len(contracts['stops']))]:
            try:
                o = int(str(click.getchar()))
            except ValueError:
                o = -1
        new_ticket['t_zone2'] = contracts['stops'][o-1]
        #Price
        zs = 0
        z1 = contracts['stops'].index(new_ticket['t_zone1'])
        z2 = contracts['stops'].index(new_ticket['t_zone2'])
        if z1 > z2:
            zs = contracts['zones'][z1][z2]
        else:
            zs = contracts['zones'][z2][z1]
        new_ticket['t_price'] = f'{contracts["tickets"][new_ticket["ticket"]][zs]:.2f}'
        #Amount
        clear()
        printAppName()
        printNewTicketOption()
        printNewTicketInfo(new_ticket)
        print('Amount:\n')
        print('1. 1 Ticket')
        print('2. 2 Tickets')
        print('3. 3 Tickets')
        print('4. 4 Tickets')
        print('5. 5 Tickets')
        print('6. 10 Tickets\n')
        op = -1
        while op not in [1,2,3,4,5,6]:
            try:
                op = int(str(click.getchar()))
            except ValueError:
                op = -1
        if op == 6:
            op = 10
        new_ticket['t_amount'] = str(op)
        new_ticket['t_price'] = f'{op * contracts["tickets"][new_ticket["ticket"]][zs]:.2f}'
        #Confirmation
        clear()
        printAppName()
        printNewTicketOption()
        printNewTicketInfo(new_ticket)
        print("Confirm ticket?")
        print('1. Yes')
        print('2. No')
        print()
        print('0. Cancel')
        print()
        op = -1
        while op != 0 and op != 1 and op != 2:
            try:
                op = int(str(click.getchar()))
            except ValueError:
                op = -1
    if op == 1:
        return new_ticket
    return None

def inputTicket(ticket, contracts):

    new_ticket = {
        'ticket': ticket['ticket'],
        't_zone1': ticket['t_zone1'],
        't_zone2': ticket['t_zone2'],
        't_amount': ticket['t_amount'],
        't_price': '', #helper variable
        't_zone': ticket['t_zone'],
        't_date': ticket['t_date'],
    }

    op = 2
    while op == 2:
        # Current amount
        new_ticket['t_amount'] = ticket['t_amount']
        #Price
        zs = 0
        z1 = contracts['stops'].index(new_ticket['t_zone1'])
        z2 = contracts['stops'].index(new_ticket['t_zone2'])
        if z1 > z2:
            zs = contracts['zones'][z1][z2]
        else:
            zs = contracts['zones'][z2][z1]
        new_ticket['t_price'] = f'{contracts["tickets"][new_ticket["ticket"]][zs]:.2f}'
        #Amount
        clear()
        printAppName()
        printNewTicketOption()
        printNewTicketInfo(new_ticket)
        print('Amount:\n')
        print('1. 1 Ticket')
        print('2. 2 Tickets')
        print('3. 3 Tickets')
        print('4. 4 Tickets')
        print('5. 5 Tickets')
        print('6. 10 Tickets\n')
        op = -1
        while op not in [1,2,3,4,5,6]:
            try:
                op = int(str(click.getchar()))
            except ValueError:
                op = -1
        if op == 6:
            op = 10
        new_ticket['t_amount'] = str(op + int(new_ticket['t_amount']))
        new_ticket['t_price'] = f'{op * contracts["tickets"][new_ticket["ticket"]][zs]:.2f}'
        #Confirmation
        clear()
        printAppName()
        printNewTicketOption()
        printNewTicketInfo(new_ticket)
        print("Confirm ticket?")
        print('1. Yes')
        print('2. No')
        print()
        print('0. Cancel')
        print()
        op = -1
        while op != 0 and op != 1 and op != 2:
            try:
                op = int(str(click.getchar()))
            except ValueError:
                op = -1
    if op == 1:
        return new_ticket
    return None

def inputBack():
    print()
    print('0. Back')
    op = -1
    while op != 0:
        try:
            op = int(str(click.getchar()))
        except ValueError:
            op = -1
