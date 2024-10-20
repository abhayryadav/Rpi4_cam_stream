import socket

# Function to control the drone (dummy function for illustration)
def control_drone(data):
    print(f"Controlling drone with data: {data}")
    # Add your drone control logic here

# Create a socket to listen for incoming connections
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind(('localhost', 65432))  # Bind to the address and port
    s.listen()  # Listen for incoming connections
    print("Listening for data from the earthquake detection script...")

    while True:
        conn, addr = s.accept()  # Accept a new connection
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)  # Buffer size of 1024 bytes
                if not data:
                    break  # Exit if no data
                control_drone(data.decode('utf-8'))  # Decode and process the received data
