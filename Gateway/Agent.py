import sys
from getpass import getpass
from WebClient import WebClient
from CommandLineInterface import *
from Serial9600 import *

DEBUG = True

def main():
    status = 0
    message = ''
    agent = None
    #Login
    while status != 200:
        clear()
        printAppName()
        if status!=0:
            printMessage(message)
        agent, status, message = WebClient.login(input("Email:    "), getpass())
    #Operation
    op = -1
    while op != 0:
        
        error = 0
        error1 = 0
        status = 0
        status1 = 0
        card_id = ''
        message = ''

        clear()
        printAppName()
        printWaitingMenu()
        try:
            card_id = deserializeCardId()
        except Exception as e:
            sys.exit(e)
        if DEBUG == False: #Debug
            clear()
        printAppName()
        printAppMenu()
        while op not in [0,1,2,3,4,5,6]:
            try:
                op = int(str(click.getchar()))
            except ValueError:
                op = -1
        match op:
            case 1:
                new_client = inputNewClient()
                if new_client is not None:
                    try:
                        error = serializeNewClient(new_client)
                    except Exception as e:
                        sys.exit(e)
                    if error == 0:
                        status, message = agent.postNewClient(new_client, card_id)
                if DEBUG == True: #Debug
                    print(f'Serialize error {error}')
                    print(f'POST /api/clients {status}')
                    break
            case 2:
                status1, contracts = agent.getContracts()
                if status1 == 200:
                    new_contract = inputNewContract(contracts)
                    if new_contract is not None:
                        try:
                            error = serializeNewContract(new_contract)
                        except Exception as e:
                            sys.exit(e)
                        if error == 0:
                            status, message = agent.postNewContract(new_contract, card_id)
                if DEBUG == True: #Debug
                    print(f'GET /api/contracts {status1}')
                    print(f'Serialize error {error}')
                    print(f'POST /api/contracts {status}')
                    break
            case 3:
                pass
                if DEBUG == True: #Debug
                    break
            case 4:
                status1, contracts = agent.getContracts()
                if status1 == 200:
                    new_ticket = inputNewTicket(contracts)
                    if new_ticket is not None:
                        try:
                            error = serializeNewTicket(new_ticket)
                        except Exception as e:
                            sys.exit(e)
                        if error == 0:
                            status, message = agent.postNewTicket(new_ticket, card_id)
                if DEBUG == True: #Debug
                    print(f'GET /api/contracts {status1}')
                    print(f'POST /api/tickets {status}')
                    print(f'Serialize error {error}')
                    break
            case 5: # Arduino Protocol Not Implemented: 2025-05-01
                status1, contracts = agent.getContracts()
                if status1 == 200:
                    ticket, error = deserializeTicket()
                if error == 0:
                    ticket = inputTicket(ticket, contracts)
                    if ticket is not None:
                        printWaitingMenu()
                        try:
                            card_id = deserializeCardId()
                            error1 = serializeNewTicket(ticket)
                            #error1 = 666 
                            if error1 == 0:
                                status, message = agent.putNewTicket(ticket, card_id)
                            if DEBUG == True: #Debug
                                print(f'PUT /api/tickets {status}')
                                print(f'GET /api/contracts {status1}')
                                print(f'Deserialize error {error}')
                                print(f'Serialize error {error1}')
                                break
                        except Exception as e:
                            sys.exit(e)
            case 6:
                try:
                    card = deserializeCard()
                except Exception as e:
                    sys.exit(e)
                printCardInfo(card)
                inputBack()
                if DEBUG == True: #Debug
                    break
            case 0:
                pass
                if DEBUG == True: #Debug
                    break
            case _:
                continue

if __name__=="__main__":
    WebClient.load_env()
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print()
