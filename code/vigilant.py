import socket
import time
import threading 

#config
PORTS = [21, 22, 80, 445]
IP = "0.0.0.0"

def watch_port(port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((IP, port))
        server.listen(5)
        print(f"[*] Vigilant starting at port: {port}")

        while True:
            client, direction = server.accept()
            # capture time of the attack
            hour = time.strftime("%H:%M:%S")
            attacker_ip = direction[0]

            print(f"[{hour}] ALERT: Attempt of connection at port {port} detected. IP: {attacker_ip} from {direction[0]}!")
            client.close()
    except Exception as e:
        print(f"[!] Error at port {port}: {e}")


print("--- STARTING MULTI PORT SYSTEM ---")
for p in PORTS:
    # create a thread for each port in the list above
    thread = threading.Thread(target=watch_port, args=(p,))
    thread.start() #starts vigilant without blocking the rest
