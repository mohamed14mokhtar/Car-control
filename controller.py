def led(fingerUp, led_1, led_2, led_3, led_4, led_5):
    if fingerUp == [0, 0, 0, 0, 0]:
        led_1.write(0)
        led_2.write(0)
        led_3.write(0)
        led_4.write(0)
        led_5.write(0)
    elif fingerUp == [1, 0, 0, 0, 0]:
        led_1.write(1)
        led_2.write(0)
        led_3.write(0)
        led_4.write(0)
        led_5.write(0)
    elif fingerUp == [1, 1, 0, 0, 0]:
        led_1.write(1)
        led_2.write(1)
        led_3.write(0)
        led_4.write(0)
        led_5.write(0)
    elif fingerUp == [0, 1, 0, 0, 0]:
        led_1.write(0)
        led_2.write(1)
        led_3.write(0)
        led_4.write(0)
        led_5.write(0)
    elif fingerUp == [0, 1, 1, 1, 0]:
        led_1.write(0)
        led_2.write(0)
        led_3.write(1)
        led_4.write(0)
        led_5.write(0)
    elif fingerUp == [0, 1, 1, 1, 1]:
        led_1.write(0)
        led_2.write(0)
        led_3.write(1)
        led_4.write(1)
        led_5.write(0)
    elif fingerUp == [0, 0, 0, 0, 1]:
        led_1.write(0)
        led_2.write(0)
        led_3.write(0)
        led_4.write(1)
        led_5.write(0)