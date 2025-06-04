from machine import Pin,SPI,PWM
import framebuf
import time
import os

import MCP2512
import LCD2inch8
import DisElements as DE

if __name__ == '__main__':
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
    # while(1):
    #while(1):
    #    readbuf = can.Receive(id)
    #    print(readbuf)
    #    time.sleep(0.5)

    print("--------------------------------------------------------")

    # https://lvgl.github.io/lv_img_conv/
    # CF_TRUE_COLOR
    # Binary RGB 565 Swap
    

    LCD = LCD2inch8.LCD_2inch8()
    LCD.bl_ctrl(100)
    #LCD.fill(LCD.BLACK)
    #LCD.show_up()

    sleep = 1
    #color BRG     
    while True:
        #LCD.fill(LCD.BLACK)
        #LCD.fill_rect(60,5,200,30,LCD.RED)
        #LCD.text("SIUE Solar Racing Team",75,17,LCD.WHITE)

        #LCD.fill(0)
        #LCD.fill_rect(0, 0, 32, 32, 1)
        #LCD.fill_rect(2, 2, 28, 28, 0)
        #LCD.vline(9, 8, 22, 1)
        #LCD.vline(16, 2, 22, 1)
        #LCD.vline(23, 8, 22, 1)
        #LCD.fill_rect(26, 24, 2, 4, 1)
        #LCD.text('MicroPython', 40, 0, 1)
        #LCD.text('SSD1306', 40, 12, 1)
        #LCD.text('OLED 128x64', 40, 24, 1)
        #LCD.show_up() 
        #time.sleep(10)

        #LCD.fill(0)


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