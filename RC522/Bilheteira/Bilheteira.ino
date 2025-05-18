#include <SPI.h>
#include <MFRC522.h>

#include "Protocol.h"

#define RST_PIN           9  
#define SS_PIN           10 

MFRC522 mfrc522(SS_PIN, RST_PIN);
MFRC522::MIFARE_Key key;

char buf[PROTOCOL_LENGTH+2];
size_t r;

void setup() {
  Serial.begin(9600);
  SPI.begin();        // Init SPI bus
  mfrc522.PCD_Init(); // Init MFRC522 card
  for (byte i = 0; i < 6; i++)
      key.keyByte[i] = 0xFF;
}

void loop() {
  
  // Waiting until card is present
  delay(1000);
  while ((!mfrc522.PICC_IsNewCardPresent()) or (!mfrc522.PICC_ReadCardSerial()))
    return;

  // Send the card id
  if (serializeCardId(mfrc522)==false)
    return;

  // Attend request
  switch (deserializePacket(buf))
  {
    case 0:
      break;
    case 1:
      // Acknowledge request
      buf[0] = 'A';
      Serial.write(buf, PROTOCOL_LENGTH);
      handleRequest01(mfrc522, key);
      break;
    case 2:
      // Acknowledge request
      buf[0] = 'A';
      Serial.write(buf, PROTOCOL_LENGTH);
      handleRequest02(mfrc522, key);
      break;
    case 3:
      // Acknowledge request
      buf[0] = 'A';
      Serial.write(buf, PROTOCOL_LENGTH);
      handleRequest03(mfrc522, key);
      break;
    case 4:
      // Acknowledge request
      buf[0] = 'A';
      Serial.write(buf, PROTOCOL_LENGTH);
      handleRequest04(mfrc522, key);
      break;
    case 5:
      // Acknowledge request
      buf[0] = 'A';
      Serial.write(buf, PROTOCOL_LENGTH);
      handleRequest05(mfrc522, key);
      break;
    case 6:
      // Acknowledge request
      buf[0] = 'A';
      Serial.write(buf, PROTOCOL_LENGTH);
      handleRequest06(mfrc522, key);
      break;
    default:
      buf[0] = 'X';
      Serial.write(buf, PROTOCOL_LENGTH);
      break;
  }
  delay(1000);
  mfrc522.PICC_HaltA();
  mfrc522.PCD_StopCrypto1();
}

