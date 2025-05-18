def printNewClientInfo(new_client):
    header = [
        'Email',
        'First',
        'Last'
    ]
    pad = 1
    header_gap = 2
    fill_gap = 2
    max_input = 32
    max_header = 0
    for h in header:
        if len(h) > max_header:
            max_header = len(h)
    fill_header = header_gap + max_header + max_input
    display = '\n'
    display += pad*' ' + header_gap*'#' + fill_header*'#' + '\n'
    display += '#' + header_gap*' ' + fill_header*' ' + '#' + '\n'
    display += '#' + header_gap*' ' + header[0] + ':' + (max_header + header_gap - len(header[0]))*' ' + new_client['email'] + (max_input - len(new_client['email']) - pad)*' ' + '#' + '\n'
    display += '#' + header_gap*' ' + fill_header*' ' + '#' + '\n'
    display += '#' + header_gap*' ' + header[1] + ':' + (max_header + header_gap - len(header[1]))*' ' + new_client['first_name'] + (max_input - len(new_client['first_name']) - pad)*' ' + '#' + '\n'
    display += '#' + header_gap*' ' + fill_header*' ' + '#' + '\n'
    display += '#' + header_gap*' ' + header[2] + ':' + (max_header + header_gap - len(header[2]))*' ' + new_client['last_name'] + (max_input - len(new_client['last_name']) - pad)*' ' + '#' + '\n'
    display += '#' + header_gap*' ' + fill_header*' ' + '#' + '\n'
    display += pad*' ' + header_gap*'#' + fill_header*'#' + '\n'
    print(display)

def printNewContractInfo(new_contract):
    header = [
        'Contract',
        'Zone1',
        'Zone2',
        'Price',
        'Expiration date'
    ]
    pad = 1
    header_gap = 2
    fill_gap = 2
    max_input = 32
    max_header = 0
    for h in header:
        if len(h) > max_header:
            max_header = len(h)
    fill_header = header_gap + max_header + max_input
    display = '\n'
    display += pad*' ' + header_gap*'#' + fill_header*'#' + '\n'
    display += '#' + header_gap*' ' + fill_header*' ' + '#' + '\n'
    display += '#' + header_gap*' ' + header[0] + ':' + (max_header + header_gap - len(header[0]))*' ' + new_contract['contract'] + (max_input - len(new_contract['contract']) - pad)*' ' + '#' + '\n'
    display += '#' + header_gap*' ' + fill_header*' ' + '#' + '\n'
    display += '#' + header_gap*' ' + header[1] + ':' + (max_header + header_gap - len(header[1]))*' ' + new_contract['c_zone1'] + (max_input - len(new_contract['c_zone1']) - pad)*' ' + '#' + '\n'
    display += '#' + header_gap*' ' + fill_header*' ' + '#' + '\n'
    display += '#' + header_gap*' ' + header[2] + ':' + (max_header + header_gap - len(header[2]))*' ' + new_contract['c_zone2'] + (max_input - len(new_contract['c_zone2']) - pad)*' ' + '#' + '\n'
    display += '#' + header_gap*' ' + fill_header*' ' + '#' + '\n'
    display += '#' + header_gap*' ' + header[3] + ':' + (max_header + header_gap - len(header[3]))*' ' + new_contract['c_price'] + (max_input - len(new_contract['c_price']) - pad)*' ' + '#' + '\n'
    display += '#' + header_gap*' ' + fill_header*' ' + '#' + '\n'
    display += '#' + header_gap*' ' + header[4] + ':' + (max_header + header_gap - len(header[4]))*' ' + new_contract['c_expire'] + (max_input - len(new_contract['c_expire']) - pad)*' ' + '#' + '\n'
    display += '#' + header_gap*' ' + fill_header*' ' + '#' + '\n'
    display += pad*' ' + header_gap*'#' + fill_header*'#' + '\n'
    print(display)

def printNewTicketInfo(new_ticket):
    header = [
        'Ticket',
        'Zone1',
        'Zone2',
        'Amount',
        'Price'
    ]
    pad = 1
    header_gap = 2
    fill_gap = 2
    max_input = 32
    max_header = 0
    for h in header:
        if len(h) > max_header:
            max_header = len(h)
    fill_header = header_gap + max_header + max_input
    display = '\n'
    display += pad*' ' + header_gap*'#' + fill_header*'#' + '\n'
    display += '#' + header_gap*' ' + fill_header*' ' + '#' + '\n'
    display += '#' + header_gap*' ' + header[0] + ':' + (max_header + header_gap - len(header[0]))*' ' + new_ticket['ticket'] + (max_input - len(new_ticket['ticket']) - pad)*' ' + '#' + '\n'
    display += '#' + header_gap*' ' + fill_header*' ' + '#' + '\n'
    display += '#' + header_gap*' ' + header[1] + ':' + (max_header + header_gap - len(header[1]))*' ' + new_ticket['t_zone1'] + (max_input - len(new_ticket['t_zone1']) - pad)*' ' + '#' + '\n'
    display += '#' + header_gap*' ' + fill_header*' ' + '#' + '\n'
    display += '#' + header_gap*' ' + header[2] + ':' + (max_header + header_gap - len(header[2]))*' ' + new_ticket['t_zone2'] + (max_input - len(new_ticket['t_zone2']) - pad)*' ' + '#' + '\n'
    display += '#' + header_gap*' ' + fill_header*' ' + '#' + '\n'
    display += '#' + header_gap*' ' + header[3] + ':' + (max_header + header_gap - len(header[3]))*' ' + new_ticket['t_amount'] + (max_input - len(new_ticket['t_amount']) - pad)*' ' + '#' + '\n'
    display += '#' + header_gap*' ' + fill_header*' ' + '#' + '\n'
    display += '#' + header_gap*' ' + header[4] + ':' + (max_header + header_gap - len(header[4]))*' ' + new_ticket['t_price'] + (max_input - len(new_ticket['t_price']) - pad)*' ' + '#' + '\n'
    display += '#' + header_gap*' ' + fill_header*' ' + '#' + '\n'
    display += pad*' ' + header_gap*'#' + fill_header*'#' + '\n'
    print(display)

def printCardInfo(card):
    header = [
        'Email',
        'First',
        'Last',
        'Contract',
        'Zone1',
        'Zone2',
        'Price',
        'Expiration date',
        'Valid until',
        'Validated zone',
        'Validated date',
        'Ticket',
        'Zone1',
        'Zone2',
        'Amount',
        'Validated zone',
        'Validated date',
    ]
    pad = 1
    header_gap = 2
    fill_gap = 2
    max_input = 32
    max_header = 0
    for h in header:
        if len(h) > max_header:
            max_header = len(h)
    fill_header = header_gap + max_header + max_input
    display = '\n'
    display += pad*' ' + header_gap*'#' + fill_header*'#' + '\n'
    display += '#' + header_gap*' ' + fill_header*' ' + '#' + '\n'
    #display += '#' + header_gap*' ' + header[0] + ':' + (max_header + header_gap - len(header[0]))*' ' + card['email'] + (max_input - len(card['email']) - pad)*' ' + '#' + '\n'
    #display += '#' + header_gap*' ' + fill_header*' ' + '#' + '\n'
    display += '#' + header_gap*' ' + header[1] + ':' + (max_header + header_gap - len(header[1]))*' ' + card['first_name'] + (max_input - len(card['first_name']) - pad)*' ' + '#' + '\n'
    display += '#' + header_gap*' ' + fill_header*' ' + '#' + '\n'
    display += '#' + header_gap*' ' + header[2] + ':' + (max_header + header_gap - len(header[2]))*' ' + card['last_name'] + (max_input - len(card['last_name']) - pad)*' ' + '#' + '\n'
    display += '#' + header_gap*' ' + fill_header*' ' + '#' + '\n'
    display += '#' + header_gap*' ' + header[3] + ':' + (max_header + header_gap - len(header[3]))*' ' + card['contract'] + (max_input - len(card['contract']) - pad)*' ' + '#' + '\n'
    display += '#' + header_gap*' ' + fill_header*' ' + '#' + '\n'
    display += '#' + header_gap*' ' + header[4] + ':' + (max_header + header_gap - len(header[4]))*' ' + card['c_zone1'] + (max_input - len(card['c_zone1']) - pad)*' ' + '#' + '\n'
    display += '#' + header_gap*' ' + fill_header*' ' + '#' + '\n'
    display += '#' + header_gap*' ' + header[5] + ':' + (max_header + header_gap - len(header[5]))*' ' + card['c_zone2'] + (max_input - len(card['c_zone2']) - pad)*' ' + '#' + '\n'
    display += '#' + header_gap*' ' + fill_header*' ' + '#' + '\n'
    display += '#' + header_gap*' ' + header[6] + ':' + (max_header + header_gap - len(header[6]))*' ' + card['c_price'] + (max_input - len(card['c_price']) - pad)*' ' + '#' + '\n'
    display += '#' + header_gap*' ' + fill_header*' ' + '#' + '\n'
    display += '#' + header_gap*' ' + header[7] + ':' + (max_header + header_gap - len(header[7]))*' ' + card['c_expire'] + (max_input - len(card['c_expire']) - pad)*' ' + '#' + '\n'
    display += '#' + header_gap*' ' + fill_header*' ' + '#' + '\n'
    display += '#' + header_gap*' ' + header[8] + ':' + (max_header + header_gap - len(header[8]))*' ' + card['c_until'] + (max_input - len(card['c_until']) - pad)*' ' + '#' + '\n'
    display += '#' + header_gap*' ' + fill_header*' ' + '#' + '\n'
    display += '#' + header_gap*' ' + header[9] + ':' + (max_header + header_gap - len(header[9]))*' ' + card['c_zone'] + (max_input - len(card['c_zone']) - pad)*' ' + '#' + '\n'
    display += '#' + header_gap*' ' + fill_header*' ' + '#' + '\n'
    display += '#' + header_gap*' ' + header[10] + ':' + (max_header + header_gap - len(header[10]))*' ' + card['c_date'] + (max_input - len(card['c_date']) - pad)*' ' + '#' + '\n'
    display += '#' + header_gap*' ' + fill_header*' ' + '#' + '\n'
    display += '#' + header_gap*' ' + header[11] + ':' + (max_header + header_gap - len(header[11]))*' ' + card['ticket'] + (max_input - len(card['ticket']) - pad)*' ' + '#' + '\n'
    display += '#' + header_gap*' ' + fill_header*' ' + '#' + '\n'
    display += '#' + header_gap*' ' + header[12] + ':' + (max_header + header_gap - len(header[12]))*' ' + card['t_zone1'] + (max_input - len(card['t_zone1']) - pad)*' ' + '#' + '\n'
    display += '#' + header_gap*' ' + fill_header*' ' + '#' + '\n'
    display += '#' + header_gap*' ' + header[13] + ':' + (max_header + header_gap - len(header[13]))*' ' + card['t_zone2'] + (max_input - len(card['t_zone2']) - pad)*' ' + '#' + '\n'
    display += '#' + header_gap*' ' + fill_header*' ' + '#' + '\n'
    display += '#' + header_gap*' ' + header[14] + ':' + (max_header + header_gap - len(header[14]))*' ' + card['t_amount'] + (max_input - len(card['t_amount']) - pad)*' ' + '#' + '\n'
    display += '#' + header_gap*' ' + fill_header*' ' + '#' + '\n'
    display += '#' + header_gap*' ' + header[15] + ':' + (max_header + header_gap - len(header[15]))*' ' + card['t_zone'] + (max_input - len(card['t_zone']) - pad)*' ' + '#' + '\n'
    display += '#' + header_gap*' ' + fill_header*' ' + '#' + '\n'
    display += '#' + header_gap*' ' + header[16] + ':' + (max_header + header_gap - len(header[16]))*' ' + card['t_date'] + (max_input - len(card['t_date']) - pad)*' ' + '#' + '\n'
    display += '#' + header_gap*' ' + fill_header*' ' + '#' + '\n'
    display += pad*' ' + header_gap*'#' + fill_header*'#' + '\n'
    print(display)
