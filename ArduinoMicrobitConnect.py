import serial
import time
import atexit
import sqltest
# serial port on raspberry pi will probably be /dev/ttyACM0

def microbit():
        mPort = "COM4"
        mBAUD = 115200
        try:
                microS = serial.Serial(mPort)
                microS.baudrate = mBAUD
                microS.parity   = serial.PARITY_NONE
                microS.databits = serial.EIGHTBITS
                microS.stopbits = serial.STOPBITS_ONE
                microS.flushInput()
                microS.flushOutput()
                return microS
        except serial.serialutil.SerialException:
                print("No Microbit")
                return None

def serial_write(s, toggle):
        if toggle:
                s.write('1'.encode('utf-8'))
                #print("on")
        else:
                s.write('0'.encode('utf-8'))
                #print("off")
        
def serial_read(s, name):
        bytesToRead = s.in_waiting
        if bytesToRead > 0:
                data = s.read(bytesToRead).decode()
                #print(name, end = '')
                print(data, end = '')
                return data
        return None

def exit_handler(mS, aS):
        if mS is not None:
                mS.close()
        if aS is not None:
                aS.close()

def arduino():
        aPort = "COM5"
        aBAUD = 115200
        try:        
                arduinoS = serial.Serial(aPort)
                arduinoS.baudrate = aBAUD
                arduinoS.parity   = serial.PARITY_NONE
                arduinoS.databits = serial.EIGHTBITS
                arduinoS.stopbits = serial.STOPBITS_ONE
                return arduinoS
        except serial.serialutil.SerialException:
                print("No Arduino")
                return None

mS = microbit()
aS = arduino()
atexit.register(exit_handler)
toggle = False
data = None

while True:
        if mS is not None:
                #serial_write(mS)
                data = serial_read(mS, "ms")
                if data is not None:
                        if ":" in data:
                                customer_id, light_level = data.split(":")
                                try:
                                        sqltest.execute(sqltest.db, "INSERT INTO %s%s VALUES%s" % (sqltest.Tables.LampLog, sqltest.TablesColumn.LampLog, sqltest.LampLogMapper(customer_id, int(light_level) > 50)))
                                except ValueError:
                                        print("woopsie")

        if aS is not None:
                if data is not None:
                        if '1' in data or '0' in data or ":" in data:
                                try:
                                        if ":" in data:
                                                toggle = not bool(int(data.split(":")[1]))
                                        else:
                                                toggle = bool(int(data))
                                        serial_write(aS, toggle)
                                        data = None
                                except ValueError:
                                        print("woopsie")
                serial_read(aS, "as")
        
        #toggle = not toggle
        time.sleep(0.001)
        # arduino()
