from machine import Pin,SPI,PWM
import framebuf
import time
import os
import _thread

import MCP2512
import LCD2inch8
import DisElements as DE

sleep = 1

def LCDUpdate_thread():
    LCD = LCD2inch8.LCD_2inch8()
    LCD.bl_ctrl(100)
    #LCD.fill(LCD.BLACK)
    #LCD.show_up()

    while True:
        DE.intensity(LCD, 0)
        LCD.show_up()  
        time.sleep(sleep)

        #LCD.fill(0)
        DE.intensity(LCD, 1)
        LCD.show_up()  
        time.sleep(sleep)

        #LCD.fill(0)
        DE.intensity(LCD, 2)
        LCD.show_up()  
        time.sleep(sleep)

        #LCD.fill(0)
        DE.intensity(LCD, 3)
        LCD.show_up()  
        time.sleep(sleep)

        #LCD.fill(0)
        DE.intensity(LCD, 4)
        LCD.show_up()  
        time.sleep(sleep)

        #LCD.fill(0)
        DE.intensity(LCD, 5)
        LCD.show_up()  
        time.sleep(sleep)

        #LCD.fill(0)
        DE.intensity(LCD, 4)
        LCD.show_up()  
        time.sleep(sleep)

        #LCD.fill(0)
        DE.intensity(LCD, 3)
        LCD.show_up()  
        time.sleep(sleep)

        #LCD.fill(0)
        DE.intensity(LCD, 2)
        LCD.show_up()  
        time.sleep(sleep)

        #LCD.fill(0)
        DE.intensity(LCD, 1)
        LCD.show_up()  
        time.sleep(sleep)

if __name__ == '__main__':

    second_thread = _thread.start_new_thread(LCDUpdate_thread, ())

    print("--------------------------------------------------------")
    can = MCP2512.MCP2515()
    print("init...")
    can.Init()
    print("send data...")
    id = 0x123 #max 7ff
    data = [1, 2, 3, 4, 5, 6, 7, 8]
    dlc = 8
    can.Send(id, data, dlc)

    readbuf = []

    while(1):
        readbuf = can.Receive(id)
        print(readbuf)
        time.sleep(0.5)

    print("--------------------------------------------------------")