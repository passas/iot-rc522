#ifndef PROTOCOL_H
#define PROTOCOL_H

#define PROTOCOL_LENGTH  22
#define PAYLOAD_LENGTH   16
#define PAYLOAD_START     6
#define TOTAL_FIELDS     17

bool serializeCardId(MFRC522 mfrc522);
int deserializePacket(char buf[]);
void handleRequest01(MFRC522 mfrc522, MFRC522::MIFARE_Key key); //Write new client
void handleRequest02(MFRC522 mfrc522, MFRC522::MIFARE_Key key); //Write new contract
void handleRequest03(MFRC522 mfrc522, MFRC522::MIFARE_Key key); //Read contract
void handleRequest04(MFRC522 mfrc522, MFRC522::MIFARE_Key key); //Write new ticket
void handleRequest05(MFRC522 mfrc522, MFRC522::MIFARE_Key key); //Read ticket
void handleRequest06(MFRC522 mfrc522, MFRC522::MIFARE_Key key); //Read all the card

#endif