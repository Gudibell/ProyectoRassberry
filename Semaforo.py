from pyfirmata import Arduino
import time 
board = Arduino("COM7")
ledr = board.get_pin('d:1:o')
ledv = board.get_pin('d:2:o')
leda = board.get_pin('d:3:o')

ledr.write(0)
ledv.write(0)
leda.write(0)


