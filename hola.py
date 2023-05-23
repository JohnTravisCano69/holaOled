#jonathan lara segovia

import machine
import ssd1306

# Initialize I2C bus and SSD1306 display
i2c = machine.I2C(0, scl=machine.Pin(9), sda=machine.Pin(8), freq=400000)
display = ssd1306.SSD1306_I2C(128, 32, i2c)

# Clear the display buffer
display.fill(0)
display.show()

# Write some text to the display
display.text("Hello, world!", 0, 0)
display.show()
