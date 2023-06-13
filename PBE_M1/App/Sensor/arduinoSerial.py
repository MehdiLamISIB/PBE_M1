import pyfirmata
from time import sleep
def getArduino_board():
    try:
        board=pyfirmata.Arduino('/dev/ttyACM0')
        return board
    except:
        board=pyfirmata.Arduino('/dev/ttyACM1')
        return board
board=getArduino_board()#pyfirmata.Arduino('/dev/ttyACM0')

led=8
board.digital[led].mode=pyfirmata.OUTPUT
## création d'un thread pour les entrées & sorties analogues
it=pyfirmata.util.Iterator(board)
it.start()
analog_input=board.get_pin('a:0:i')
while True:


    ###
    ### Resistance de 10k ohm
    ## avec potentiometre
    #board.digital[led].write(1)
    """
    sleep(1)
    board.digital[led].write(0)
    sleep(1)

    """

    #DigitalRead
    value=analog_input.read()
    print(value)
    sleep(0.1)