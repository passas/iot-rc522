import time
import serial

DBG = True
PAYLOAD_SIZE = 16
MESSAGE_SIZE = 22

def getAck(packet):
    return packet[0:2]
def getOp(packet):
    return packet[2:4]
def getField(packet):
    return packet[4:6]
def getPayload(packet):
    return packet[6:22]

def deserializeCardId():
    try:
        pipe = serial.Serial('/dev/ttyACM0', 9600)
    except Exception as e:
        raise Exception(e)
    while pipe.in_waiting < MESSAGE_SIZE:
        time.sleep(1)
    pckt = pipe.read(MESSAGE_SIZE).decode('utf-8')
    if DBG == True: #Debug
        print(pckt)
    card_id = pckt[6:22] #retrieve card id
    pckt = 'A' + pckt[1:] #acknowledge
    pipe.write(pckt.encode('utf-8'))
    pipe.close()
    return card_id

def truncatePayload(payload):
    s = ''
    for i in range(0,PAYLOAD_SIZE):
        if i<len(payload) and len(payload)<=PAYLOAD_SIZE:
            s += payload[i]
        else:
            s += '#'
    return s

def serializeNewClient(new_client):
    error = 0
    a, o, f, c = '::', '01', '::', '#'
    try:
        pipe = serial.Serial('/dev/ttyACM0', 9600)
    except Exception as e:
        raise Exception(e)
    #Request
    pckt = a + o + f + PAYLOAD_SIZE*c
    pipe.write(pckt.encode('utf-8'))
    while pipe.in_waiting < MESSAGE_SIZE:
        pass
    fdback = pipe.read(MESSAGE_SIZE).decode('utf-8')
    if DBG == True: #Debug
        print(fdback)
    #First name
    f = '01'
    pckt = a + o + f + truncatePayload(new_client['first_name'])
    pipe.write(pckt.encode('utf-8'))
    while pipe.in_waiting < MESSAGE_SIZE:
        pass
    fdback = pipe.read(MESSAGE_SIZE).decode('utf-8')
    if getAck(fdback) != 'A:':
        error = 1
    if DBG == True: #Debug
        print(fdback)
    #Last name
    f = '02'
    pckt = a + o + f + truncatePayload(new_client['last_name'])
    pipe.write(pckt.encode('utf-8'))
    while pipe.in_waiting < MESSAGE_SIZE:
        pass
    fdback = pipe.read(MESSAGE_SIZE).decode('utf-8')
    if getAck(fdback) != 'A:':
        error = 2
    if DBG == True: #Debug
        print(fdback)
    #Close
    pipe.close()
    return error

def serializeNewContract(new_contract):
    error = 0
    a, o, f, c = '::', '02', '::', '#'
    try:
        pipe = serial.Serial('/dev/ttyACM0', 9600)
    except Exception as e:
        raise Exception(e)
    #Request
    pckt = a + o + f + PAYLOAD_SIZE*c
    pipe.write(pckt.encode('utf-8'))
    while pipe.in_waiting < MESSAGE_SIZE:
        pass
    fdback = pipe.read(MESSAGE_SIZE).decode('utf-8')
    if DBG == True: #Debug
        print(fdback)
    #Type
    f = '03'
    pckt = a + o + f + truncatePayload(new_contract['contract'])
    pipe.write(pckt.encode('utf-8'))
    while pipe.in_waiting < MESSAGE_SIZE:
        pass
    fdback = pipe.read(MESSAGE_SIZE).decode('utf-8')
    if getAck(fdback) != 'A:':
        error = 3
    if DBG == True: #Debug
        print(fdback)
    #Zone1
    f = '04'
    pckt = a + o + f + truncatePayload(new_contract['c_zone1'])
    pipe.write(pckt.encode('utf-8'))
    while pipe.in_waiting < MESSAGE_SIZE:
        pass
    fdback = pipe.read(MESSAGE_SIZE).decode('utf-8')
    if getAck(fdback) != 'A:':
        error = 4
    if DBG == True: #Debug
        print(fdback)
    #Zone2
    f = '05'
    pckt = a + o + f + truncatePayload(new_contract['c_zone2'])
    pipe.write(pckt.encode('utf-8'))
    while pipe.in_waiting < MESSAGE_SIZE:
        pass
    fdback = pipe.read(MESSAGE_SIZE).decode('utf-8')
    if getAck(fdback) != 'A:':
        error = 5
    if DBG == True: #Debug
        print(fdback)
    #Price
    f = '06'
    pckt = a + o + f + truncatePayload(new_contract['c_price'])
    pipe.write(pckt.encode('utf-8'))
    while pipe.in_waiting < MESSAGE_SIZE:
        pass
    fdback = pipe.read(MESSAGE_SIZE).decode('utf-8')
    if getAck(fdback) != 'A:':
        error = 6
    if DBG == True: #Debug
        print(fdback)
    #Expiration
    f = '07'
    pckt = a + o + f + truncatePayload(new_contract['c_expire'])
    pipe.write(pckt.encode('utf-8'))
    while pipe.in_waiting < MESSAGE_SIZE:
        pass
    fdback = pipe.read(MESSAGE_SIZE).decode('utf-8')
    if getAck(fdback) != 'A:':
        error = 7
    if DBG == True: #Debug
        print(fdback)
    #Close
    pipe.close()
    return error

def serializeNewTicket(new_ticket):
    error = 0
    a, o, f, c = '::', '04', '::', '#'
    try:
        pipe = serial.Serial('/dev/ttyACM0', 9600)
    except Exception as e:
        raise Exception(e)
    #Request
    pckt = a + o + f + PAYLOAD_SIZE*c
    pipe.write(pckt.encode('utf-8'))
    while pipe.in_waiting < MESSAGE_SIZE:
        pass
    fdback = pipe.read(MESSAGE_SIZE).decode('utf-8')
    if DBG == True: #Debug
        print(fdback)
    #Type
    f = '11'
    pckt = a + o + f + truncatePayload(new_ticket['ticket'])
    pipe.write(pckt.encode('utf-8'))
    while pipe.in_waiting < MESSAGE_SIZE:
        pass
    fdback = pipe.read(MESSAGE_SIZE).decode('utf-8')
    if getAck(fdback) != 'A:':
        error = 11
    if DBG == True: #Debug
        print(fdback)
    #Zone1
    f = '12'
    pckt = a + o + f + truncatePayload(new_ticket['t_zone1'])
    pipe.write(pckt.encode('utf-8'))
    while pipe.in_waiting < MESSAGE_SIZE:
        pass
    fdback = pipe.read(MESSAGE_SIZE).decode('utf-8')
    if getAck(fdback) != 'A:':
        error = 12
    if DBG == True: #Debug
        print(fdback)
    #Zone2
    f = '13'
    pckt = a + o + f + truncatePayload(new_ticket['t_zone2'])
    pipe.write(pckt.encode('utf-8'))
    while pipe.in_waiting < MESSAGE_SIZE:
        pass
    fdback = pipe.read(MESSAGE_SIZE).decode('utf-8')
    if getAck(fdback) != 'A:':
        error = 13
    if DBG == True: #Debug
        print(fdback)
    #Amount
    f = '14'
    pckt = a + o + f + truncatePayload(new_ticket['t_amount'])
    pipe.write(pckt.encode('utf-8'))
    while pipe.in_waiting < MESSAGE_SIZE:
        pass
    fdback = pipe.read(MESSAGE_SIZE).decode('utf-8')
    if getAck(fdback) != 'A:':
        error = 14
    if DBG == True: #Debug
        print(fdback)
    #Zone
    f = '15'
    pckt = a + o + f + truncatePayload(new_ticket['t_zone'])
    pipe.write(pckt.encode('utf-8'))
    while pipe.in_waiting < MESSAGE_SIZE:
        pass
    fdback = pipe.read(MESSAGE_SIZE).decode('utf-8')
    if getAck(fdback) != 'A:':
        error = 15
    if DBG == True: #Debug
        print(fdback)
    #Zone
    f = '16'
    pckt = a + o + f + truncatePayload(new_ticket['t_date'])
    pipe.write(pckt.encode('utf-8'))
    while pipe.in_waiting < MESSAGE_SIZE:
        pass
    fdback = pipe.read(MESSAGE_SIZE).decode('utf-8')
    if getAck(fdback) != 'A:':
        error = 16
    if DBG == True: #Debug
        print(fdback)
    #Close
    pipe.close()
    return error

def deserializeTicket():
    error = 0
    fields = [
        'ticket',
        't_zone1',
        't_zone2',
        't_amount',
        't_zone',
        't_date'
    ]
    card = {
        'ticket': '',
        't_zone1': '',
        't_zone2': '',
        't_amount': '',
        't_zone': '',
        't_date': ''
    }
    error = 0
    a, o, f, c = '::', '05', '::', '#'
    try:
        pipe = serial.Serial('/dev/ttyACM0', 9600)
    except Exception as e:
        raise Exception(e)
    #Request
    pckt = a + o + f + PAYLOAD_SIZE*c
    pipe.write(pckt.encode('utf-8'))
    while pipe.in_waiting < MESSAGE_SIZE:
        pass
    fdback = pipe.read(MESSAGE_SIZE).decode('utf-8')
    if DBG == True: #Debug
        print(fdback)
    #Receive
    for i in range(0,len(fields)):
        while pipe.in_waiting < MESSAGE_SIZE:
            pass
        try:
            packet = pipe.read(MESSAGE_SIZE)
            packet = packet.decode('utf-8')
        except UnicodeError:
            error = 0
        else:
            try:
                if getAck(packet)=='::':
                    #card[fields[int(getField(packet))]] = getPayload(packet)
                    card[fields[i]] = getPayload(packet).replace('#','')
                else:
                    error = i
            except ValueError:
                pass
        if DBG == True: #Debug
            print(packet)
    return card, error

def deserializeCard():
    fields = [
        'email',
        'first_name',
        'last_name',
        'contract',
        'c_zone1',
        'c_zone2',
        'c_price',
        'c_expire',
        'c_until',
        'c_zone',
        'c_date',
        'ticket',
        't_zone1',
        't_zone2',
        't_amount',
        't_zone',
        't_date'
    ]
    card = {
        'email': '',
        'first_name': '',
        'last_name': '',
        'contract': '',
        'c_zone1': '',
        'c_zone2': '',
        'c_price': '',
        'c_expire': '',
        'c_until': '',
        'c_zone': '',
        'c_date': '',
        'ticket': '',
        't_zone1': '',
        't_zone2': '',
        't_amount': '',
        't_zone': '',
        't_date': ''
    }
    error = 0
    a, o, f, c = '::', '06', '::', '#'
    try:
        pipe = serial.Serial('/dev/ttyACM0', 9600)
    except Exception as e:
        raise Exception(e)
    #Request
    pckt = a + o + f + PAYLOAD_SIZE*c
    pipe.write(pckt.encode('utf-8'))
    while pipe.in_waiting < MESSAGE_SIZE:
        pass
    fdback = pipe.read(MESSAGE_SIZE).decode('utf-8')
    if DBG == True: #Debug
        print(fdback)
    #Receive
    for i in range(0,len(fields)):
        while pipe.in_waiting < MESSAGE_SIZE:
            pass
        try:
            packet = pipe.read(MESSAGE_SIZE)
            packet = packet.decode('utf-8')
        except UnicodeError:
            pass
        else:
            try:
                if getAck(packet)=='::':
                    card[fields[int(getField(packet))]] = getPayload(packet)
                else:
                    card[i] = 16*' '
            except ValueError:
                pass
        if DBG == True: #Debug
            if i != 0:
                print(packet)
    return card
