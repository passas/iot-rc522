#include <SPI.h>
#include <MFRC522.h>

#include "Protocol.h"

int readFromCard (MFRC522 mfrc522, MFRC522::MIFARE_Key key, byte trailer_block, byte block_addr, byte data[], byte size);
void paylaodPacket (byte b[], char packet[]);

int writeToCard (MFRC522, MFRC522::MIFARE_Key, byte trailer_block, byte block_addr, byte data[], byte size);
void charsToBytes (byte b[], char packet[]);

bool serializeCardId(MFRC522 mfrc522)
{
  size_t r;
  char packet[PROTOCOL_LENGTH];

  //Retrieve card id
  String card_id = "";
  for (byte i = 0; i < mfrc522.uid.size; i++)
  {
    //Convert byte into char
    char b[3];
    sprintf(b, "%02X", mfrc522.uid.uidByte[i]);
    //Add the converted char into a string
    card_id += b;
  }
  
  //Build header
  packet[0] = ':';
  packet[1] = ':';
  packet[2] = 'i';
  packet[3] = 'd';
  packet[4] = ':';
  packet[5] = ':';
  //Build payload
  for(int j=0; j<PAYLOAD_LENGTH; j++)
    if (j<card_id.length())
      packet[PAYLOAD_START + j] = card_id[j];
    else
      packet[PAYLOAD_START + j] = '#';
    
  //Serialize packet w/ the card id
  Serial.write(packet, PROTOCOL_LENGTH);

  //Waiting for acknowledgment
  while(Serial.available() != PROTOCOL_LENGTH);
  r = Serial.readBytes(packet, PROTOCOL_LENGTH);
  if (r == PROTOCOL_LENGTH && packet[0]=='A')
    return true;

  return false;
}

int deserializePacket(char buf[])
{
  size_t r;

  while(Serial.available() != PROTOCOL_LENGTH);
  r = Serial.readBytes(buf, PROTOCOL_LENGTH);
  if (r != PROTOCOL_LENGTH)
    return -1;

  // Return option
  return 10*(buf[2] - '0') + (buf[3] - '0');
}

void handleRequest01(MFRC522 mfrc522, MFRC522::MIFARE_Key key)
{
  size_t r;
  char packet[PROTOCOL_LENGTH];

  int e;
  byte b[PROTOCOL_LENGTH];

  //Receive first and last name
  for(int i=0; i<2; i++)
  {
    while(Serial.available() != PROTOCOL_LENGTH);
    r = Serial.readBytes(packet, PROTOCOL_LENGTH);
    if (r != PROTOCOL_LENGTH)
      packet[0] = 'X';
    else
    {
      packet[0] = 'A';
      charsToBytes (b, packet);
      int field = 10*(packet[4] - '0') + (packet[5] - '0');
      if(field == 1)
        e = writeToCard(mfrc522, key, 7, 4, b, PAYLOAD_LENGTH);
      else if (field == 2)
        e = writeToCard(mfrc522, key, 7, 5, b, PAYLOAD_LENGTH);
      else
        e = -1;
      
      if (e == -1)
        packet[0] = 'X';
      else if (e == 100)
        packet[0] = 'R';
      else if (e == 101)
        packet[0] = 'W';
      else if (e == 1)
        packet[0] = '!';
    }
    Serial.write(packet, PROTOCOL_LENGTH);
  }
}

void handleRequest02(MFRC522 mfrc522, MFRC522::MIFARE_Key key)
{
  size_t r;
  char packet[PROTOCOL_LENGTH];

  int e;
  byte b[PROTOCOL_LENGTH];

  //Receive type, zone1, zone2, price, and expiration date
  for(int i=0; i<5; i++)
  {
    while(Serial.available() != PROTOCOL_LENGTH);
    r = Serial.readBytes(packet, PROTOCOL_LENGTH);
    if (r != PROTOCOL_LENGTH)
      packet[0] = 'X';
    else
    {
      packet[0] = 'A';
      charsToBytes (b, packet);
      int field = 10*(packet[4] - '0') + (packet[5] - '0');
      if(field == 3) //c_type
        e = writeToCard(mfrc522, key, 11, 8, b, PAYLOAD_LENGTH);
      else if (field == 4) //c_zone1
        e = writeToCard(mfrc522, key, 11, 9, b, PAYLOAD_LENGTH);
      else if (field == 5) //c_zone2
        e = writeToCard(mfrc522, key, 11, 10, b, PAYLOAD_LENGTH);
      else if (field == 6) //c_price
        e = writeToCard(mfrc522, key, 15, 12, b, PAYLOAD_LENGTH);
      else if (field == 7) //c_expire
        e = writeToCard(mfrc522, key, 15, 13, b, PAYLOAD_LENGTH);
      else
        e = -1;
      
      if (e == -1)
        packet[0] = 'X';
      else if (e == 100)
        packet[0] = 'R';
      else if (e == 101)
        packet[0] = 'W';
      else if (e == 1)
        packet[0] = '!';
    }
    Serial.write(packet, PROTOCOL_LENGTH);
  }
}

void handleRequest03(MFRC522 mfrc522, MFRC522::MIFARE_Key key)
{}

void handleRequest04(MFRC522 mfrc522, MFRC522::MIFARE_Key key)
{
  size_t r;
  char packet[PROTOCOL_LENGTH];

  int e;
  byte b[PROTOCOL_LENGTH];

  //Receive ticket type, zone1, zone2, and amount of tickets
  for(int i=11; i<17; i++)
  {
    while(Serial.available() != PROTOCOL_LENGTH);
    r = Serial.readBytes(packet, PROTOCOL_LENGTH);
    if (r != PROTOCOL_LENGTH)
      packet[0] = 'X';
    else
    {
      packet[0] = 'A';
      charsToBytes (b, packet);
      int field = 10*(packet[4] - '0') + (packet[5] - '0');
      if(field == 11) //ticket
        e = writeToCard(mfrc522, key, 27, 24, b, PAYLOAD_LENGTH);
      else if (field == 12) //t_zone1
        e = writeToCard(mfrc522, key, 27, 25, b, PAYLOAD_LENGTH);
      else if (field == 13) //t_zone2
        e = writeToCard(mfrc522, key, 27, 26, b, PAYLOAD_LENGTH);
      else if (field == 14) //t_amount
        e = writeToCard(mfrc522, key, 31, 28, b, PAYLOAD_LENGTH);
      else if (field == 15) //t_zone
        e = writeToCard(mfrc522, key, 31, 29, b, PAYLOAD_LENGTH);
      else if (field == 16) //t_date
        e = writeToCard(mfrc522, key, 31, 30, b, PAYLOAD_LENGTH);
      else
        e = -1;
      
      if (e == -1)
        packet[0] = 'X';
      else if (e == 100)
        packet[0] = 'R';
      else if (e == 101)
        packet[0] = 'W';
      else if (e == 1)
        packet[0] = '!';
    }
    Serial.write(packet, PROTOCOL_LENGTH);
  }  
}

void handleRequest05(MFRC522 mfrc522, MFRC522::MIFARE_Key key)
{
  size_t r;
  char packet[PROTOCOL_LENGTH];

  byte b[PAYLOAD_LENGTH + 2]; // \r\n
  byte b_size = sizeof(b);

  int e;
  char buf[PAYLOAD_LENGTH]; 
  
  //Send ticket type, zone1, zone2, and amount of tickets
  for(int i=11; i<17; i++)
  {
    packet[0] = ':'; packet[1] = ':';
    packet[2] = '0'; packet[3] = '4';
    if(i == 11) // ticket
    {
      packet[4] = '1'; packet[5] = '1';
      e = readFromCard(mfrc522, key, 27, 24, b, b_size);
    }
    else if (i == 12) // t_zone1
    {
      packet[4] = '1'; packet[5] = '2';
      e = readFromCard(mfrc522, key, 27, 25, b, b_size);
    }
    else if (i == 13) // t_zone2
    {
      packet[4] = '1'; packet[5] = '3';
      e = readFromCard(mfrc522, key, 27, 26, b, b_size);
    }
    else if (i == 14) // t_amount
    {
      packet[4] = '1'; packet[5] = '4';
      e = readFromCard(mfrc522, key, 31, 28, b, b_size);
    }
    else if (i == 15) // t_zone
    {
      packet[4] = '1'; packet[5] = '5';
      e = readFromCard(mfrc522, key, 31, 29, b, b_size);
    }
    else if (i == 16) // t_date
    {
      packet[4] = '1'; packet[5] = '6';
      e = readFromCard(mfrc522, key, 31, 30, b, b_size);
    }
    else
      e = -1;

    if (e == -1)
      packet[0] = 'X';
    else if (e == 100)
      packet[0] = 'R';
    else if (e == 101)
      packet[0] = 'W';
    else if (e == 1)
      packet[0] = '!';
    else
      paylaodPacket(b, packet);

    Serial.write(packet, PROTOCOL_LENGTH);
  }
}

void handleRequest06(MFRC522 mfrc522, MFRC522::MIFARE_Key key)
{
  size_t r;
  char packet[PROTOCOL_LENGTH];

  byte b[PAYLOAD_LENGTH + 2]; // \r\n
  byte b_size = sizeof(b);

  int e;
  char buf[PAYLOAD_LENGTH]; 
  
  //Send first and last name
  for(int i=0; i<TOTAL_FIELDS; i++)
  {
    packet[0] = ':'; packet[1] = ':';
    packet[2] = '0'; packet[3] = '6';
    if(i == 0) // email
    {
      packet[4] = '0'; packet[5] = '0';
      e = readFromCard(mfrc522, key, 3, 1, b, b_size);
    }
    else if (i == 1) // first_name
    {
      packet[4] = '0'; packet[5] = '1';
      e = readFromCard(mfrc522, key, 7, 4, b, b_size);
    }
    else if (i == 2) // last_name
    {
      packet[4] = '0'; packet[5] = '2';
      e = readFromCard(mfrc522, key, 7, 5, b, b_size);
    }
    else if (i == 3) // contract
    {
      packet[4] = '0'; packet[5] = '3';
      e = readFromCard(mfrc522, key, 11, 8, b, b_size);
    }
    else if (i == 4) // c_zone1
    {
      packet[4] = '0'; packet[5] = '4';
      e = readFromCard(mfrc522, key, 11, 9, b, b_size);
    }
    else if (i == 5) // c_zone2
    {
      packet[4] = '0'; packet[5] = '5';
      e = readFromCard(mfrc522, key, 11, 10, b, b_size);
    }
    else if (i == 6) // c_price
    {
      packet[4] = '0'; packet[5] = '6';
      e = readFromCard(mfrc522, key, 15, 12, b, b_size);
    }
    else if (i == 7) // c_expire
    {
      packet[4] = '0'; packet[5] = '7';
      e = readFromCard(mfrc522, key, 15, 13, b, b_size);
    }
    else if (i == 8) // c_until
    {
      packet[4] = '0'; packet[5] = '8';
      e = readFromCard(mfrc522, key, 15, 14, b, b_size);
    }
    else if (i == 9) // c_zone
    {
      packet[4] = '0'; packet[5] = '9';
      e = readFromCard(mfrc522, key, 19, 16, b, b_size);
    }
    else if (i == 10) // c_date
    {
      packet[4] = '1'; packet[5] = '0';
      e = readFromCard(mfrc522, key, 19, 17, b, b_size);
    }
    else if (i == 11) // ticket
    {
      packet[4] = '1'; packet[5] = '1';
      e = readFromCard(mfrc522, key, 27, 24, b, b_size);
    }
    else if (i == 12) // t_zone1
    {
      packet[4] = '1'; packet[5] = '2';
      e = readFromCard(mfrc522, key, 27, 25, b, b_size);
    }
    else if (i == 13) // t_zone2
    {
      packet[4] = '1'; packet[5] = '3';
      e = readFromCard(mfrc522, key, 27, 26, b, b_size);
    }
    else if (i == 14) // t_amount
    {
      packet[4] = '1'; packet[5] = '4';
      e = readFromCard(mfrc522, key, 31, 28, b, b_size);
    }
    else if (i == 15) // t_zone
    {
      packet[4] = '1'; packet[5] = '5';
      e = readFromCard(mfrc522, key, 31, 29, b, b_size);
    }
    else if (i == 16) // t_date
    {
      packet[4] = '1'; packet[5] = '6';
      e = readFromCard(mfrc522, key, 31, 30, b, b_size);
    }
    else
      e = -1;

    if (e == -1)
      packet[0] = 'X';
    else if (e == 100)
      packet[0] = 'R';
    else if (e == 101)
      packet[0] = 'W';
    else if (e == 1)
      packet[0] = '!';
    else
      paylaodPacket(b, packet);

    Serial.write(packet, PROTOCOL_LENGTH);
  }
}

void charsToBytes (byte b[], char packet[])
{
  byte i; int j;
  for(i=j=0; j<PAYLOAD_LENGTH; i++, j++)
    b[i] = packet[PAYLOAD_START + j];
}
int writeToCard (MFRC522 mfrc522, MFRC522::MIFARE_Key key, byte trailer_block, byte block_addr, byte data[], byte size)
{
  for (byte i = 0; i < 6; i++)
      key.keyByte[i] = 0xFF;
  MFRC522::StatusCode status;
  //status = (MFRC522::StatusCode) mfrc522.PCD_Authenticate(MFRC522::PICC_CMD_MF_AUTH_KEY_A, trailer_block, &key, &(mfrc522.uid));
  //if (status != MFRC522::STATUS_OK)
  //      return 100;
  status = (MFRC522::StatusCode) mfrc522.PCD_Authenticate(MFRC522::PICC_CMD_MF_AUTH_KEY_B, trailer_block, &key, &(mfrc522.uid));
  while (status != MFRC522::STATUS_OK)
      return 101;
  status = (MFRC522::StatusCode) mfrc522.MIFARE_Write(block_addr, data, size);
  if (status != MFRC522::STATUS_OK)
        return 1;
  return 0;
}

void paylaodPacket (byte b[], char packet[])
{
  for(int j=0; j<PAYLOAD_LENGTH; j++)
    packet[PAYLOAD_START + j] = b[j];
}
int readFromCard (MFRC522 mfrc522, MFRC522::MIFARE_Key key, byte trailer_block, byte block_addr, byte data[], byte size)
{
  for (byte i = 0; i < 6; i++)
      key.keyByte[i] = 0xFF;
  MFRC522::StatusCode status;
  status = (MFRC522::StatusCode) mfrc522.PCD_Authenticate(MFRC522::PICC_CMD_MF_AUTH_KEY_A, trailer_block, &key, &(mfrc522.uid));
  if (status != MFRC522::STATUS_OK)
        return 100;
  //status = (MFRC522::StatusCode) mfrc522.PCD_Authenticate(MFRC522::PICC_CMD_MF_AUTH_KEY_B, trailer_block, &key, &(mfrc522.uid));
  //while (status != MFRC522::STATUS_OK)
  //    return 101;
  status = (MFRC522::StatusCode) mfrc522.MIFARE_Read(block_addr, data, &size);
  if (status != MFRC522::STATUS_OK)
        return 1;
  return 0;
}