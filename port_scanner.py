import socket

print("== Simple Port Scanner ==")
target = input("Target IP/domain: ")
start_port = int(input("Start port: "))
end_port = int(input("End port: "))

print(f"\nScanning {target} from port {start_port} to {end_port}...\n")
for port in range(start_port, end_port + 1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    try:
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port}: OPEN")
    except Exception as e:
        print(f"Port {port}: Error - {e}")
    s.close()
print("\nScan complete.")
