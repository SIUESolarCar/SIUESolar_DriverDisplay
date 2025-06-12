import framebuf

# https://lvgl.github.io/lv_img_conv/
# CF_TRUE_COLOR
# Binary RGB 565 Swap

data = open('Cyan.bin', 'rb')
Cyan = bytearray(data.read())

data = open('Green.bin', 'rb')
Green = bytearray(data.read())

data = open('Yellow.bin', 'rb')
Yellow = bytearray(data.read())

data = open('Orange.bin', 'rb')
Orange = bytearray(data.read())

data = open('Red.bin', 'rb')
Red = bytearray(data.read())

data = open('Gray.bin', 'rb')
Gray = bytearray(data.read())

#fb = framebuf.FrameBuffer(Cyan, 62, 20, framebuf.RGB565)
#LCD.blit(fb, 3, 5)

#fb = framebuf.FrameBuffer(Green, 62, 20, framebuf.RGB565)
#LCD.blit(fb, 66, 5)

#fb = framebuf.FrameBuffer(Yellow, 62, 20, framebuf.RGB565)
#LCD.blit(fb, 129, 5)

#fb = framebuf.FrameBuffer(Orange, 62, 20, framebuf.RGB565)
#LCD.blit(fb, 192, 5)

#fb = framebuf.FrameBuffer(Red, 62, 20, framebuf.RGB565)
#LCD.blit(fb, 255, 5)

def intensity(LCD, level):
    if level == 0:
        fb = framebuf.FrameBuffer(Gray, 62, 20, framebuf.RGB565)
        LCD.blit(fb, 3, 5)
        LCD.blit(fb, 66, 5)
        LCD.blit(fb, 129, 5)
        LCD.blit(fb, 192, 5)
        LCD.blit(fb, 255, 5)

    elif level == 1:
        fb = framebuf.FrameBuffer(Cyan, 62, 20, framebuf.RGB565)
        LCD.blit(fb, 3, 5)

        fb = framebuf.FrameBuffer(Gray, 62, 20, framebuf.RGB565)
        LCD.blit(fb, 66, 5)
        LCD.blit(fb, 129, 5)
        LCD.blit(fb, 192, 5)
        LCD.blit(fb, 255, 5)

    elif level == 2:
        fb = framebuf.FrameBuffer(Cyan, 62, 20, framebuf.RGB565)
        LCD.blit(fb, 3, 5)
        fb = framebuf.FrameBuffer(Green, 62, 20, framebuf.RGB565)
        LCD.blit(fb, 66, 5)

        fb = framebuf.FrameBuffer(Gray, 62, 20, framebuf.RGB565)
        LCD.blit(fb, 129, 5)
        LCD.blit(fb, 192, 5)
        LCD.blit(fb, 255, 5)

    elif level == 3:
        fb = framebuf.FrameBuffer(Cyan, 62, 20, framebuf.RGB565)
        LCD.blit(fb, 3, 5)
        fb = framebuf.FrameBuffer(Green, 62, 20, framebuf.RGB565)
        LCD.blit(fb, 66, 5)
        fb = framebuf.FrameBuffer(Yellow, 62, 20, framebuf.RGB565)
        LCD.blit(fb, 129, 5)

        fb = framebuf.FrameBuffer(Gray, 62, 20, framebuf.RGB565)
        LCD.blit(fb, 192, 5)
        LCD.blit(fb, 255, 5)

    elif level == 4:
        fb = framebuf.FrameBuffer(Cyan, 62, 20, framebuf.RGB565)
        LCD.blit(fb, 3, 5)
        fb = framebuf.FrameBuffer(Green, 62, 20, framebuf.RGB565)
        LCD.blit(fb, 66, 5)
        fb = framebuf.FrameBuffer(Yellow, 62, 20, framebuf.RGB565)
        LCD.blit(fb, 129, 5)
        fb = framebuf.FrameBuffer(Orange, 62, 20, framebuf.RGB565)
        LCD.blit(fb, 192, 5)

        fb = framebuf.FrameBuffer(Gray, 62, 20, framebuf.RGB565)
        LCD.blit(fb, 255, 5)

    elif level == 5:
        fb = framebuf.FrameBuffer(Cyan, 62, 20, framebuf.RGB565)
        LCD.blit(fb, 3, 5)
        fb = framebuf.FrameBuffer(Green, 62, 20, framebuf.RGB565)
        LCD.blit(fb, 66, 5)
        fb = framebuf.FrameBuffer(Yellow, 62, 20, framebuf.RGB565)
        LCD.blit(fb, 129, 5)
        fb = framebuf.FrameBuffer(Orange, 62, 20, framebuf.RGB565)
        LCD.blit(fb, 192, 5)
        fb = framebuf.FrameBuffer(Red, 62, 20, framebuf.RGB565)
        LCD.blit(fb, 255, 5)