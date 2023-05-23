#include <stdio.h>
#include <wiringPi.h>                           // wiringPi 헤더파일 참조
#define LED 21                                   // 해당 핀에 LED 연결

int main(void)
{
    printf("Raspberry Pi – LED Blink\n");
    wiringPiSetupGpio();                          // 핀 번호를 BCM모드로 설정
    pinMode(LED, OUTPUT);                     // LED 핀을 출력모드로 설정 

    while(1)                                          // 무한 루프
    {
        digitalWrite(LED, HIGH);                  // LED 핀의 상태를 HIGH로 변경
        delay(500);                                  // 500msec 지연
        digitalWrite(LED, LOW);                  // LED 핀의 상태를 LOW로 변경
        delay(500);
    }
    return 0;
}
