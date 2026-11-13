#!/bin/bash
echo "[*] Aplicando Segmentação de Rede IT/OT na Subestação..."

# permite que o próprio painel HMI local (127.0.0.1) converse com o PLC
iptables -A INPUT -p tcp -s 127.0.0.1 --dport 502 -j ACCEPT

# MISSÃO BLUE TEAM (Segmentação):
# Descomente a linha abaixo para bloquear qualquer IP não autorizado (como o 172.28.0.99 da VPN comprometida) de acessar a porta 502:
# iptables -A INPUT -p tcp --dport 502 -j DROP

echo "[+] Regras de Firewall atualizadas!"
