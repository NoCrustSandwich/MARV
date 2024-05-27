from serial import Serial
import threading

# Function to continuously send data to the serial port
def send_to_serial(ser):
    while True:
        user_input = input("")
        ser.write(user_input.encode('utf-8') + b'\n')

# Open the serial port
ser = Serial('COM3', 19200, timeout=3)  # Set timeout to 1 second
# Replace 'COM3' with the appropriate COM port and baud rate

# Start a thread to continuously send data to the serial port
serial_thread = threading.Thread(target=send_to_serial, args=(ser,), daemon=True)
serial_thread.start()

# Main loop for continuously reading from the serial port
try:
    while True:
        if ser.in_waiting:
            try:
                data = ser.readline().decode('utf-8').strip()
                print(data)
            except UnicodeDecodeError:
                pass
except KeyboardInterrupt:
    pass

# Close the serial port
ser.close()
