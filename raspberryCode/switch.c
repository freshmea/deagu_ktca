// gpio_input_test.c 파일

#include <stdio.h>
#include <wiringPi.h>
#define KEY   3                                        // 해당 핀에 SWITCH 연결

int main(void)
{
    printf("Raspberry Pi – Key Input Test\n");
    wiringPiSetupGpio();                              // 핀 번호를 BCM모드로 설정
    pinMode(KEY, INPUT);                            // SWITCH 핀을 입력모드로 설정
    while(1)                                              // 무한 루프
    {
        int val = digitalRead(KEY);                  // SWITCH 핀의 상태를 확인
        if(val == LOW)                                 // 상태가 LOW 이면
        {
            printf("Button is pressed”\n");         // “Button is Pressed” 출력
        }
        delay(1000);                                    // 1000msec 지연
     }
     return 0;
 }
