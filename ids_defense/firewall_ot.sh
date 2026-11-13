#!/bin/bash
echo "[*] Aplicando Segmentação de Rede IT/OT na Subestação..."

# Remove regras antigas do script caso seja executado mais de uma vez
iptables -D INPUT -p tcp -s 127.0.0.1 --dport 502 -j ACCEPT 2>/dev/null
iptables -D INPUT -p tcp --dport 502 -j DROP 2>/dev/null

# Posição 1: permite que o próprio painel HMI local (127.0.0.1) converse com o PLC
iptables -I INPUT 1 -p tcp -s 127.0.0.1 --dport 502 -j ACCEPT

# MISSÃO BLUE TEAM (Segmentação):
# Descomente a linha abaixo para bloquear qualquer IP não autorizado (como o 172.28.0.99 da VPN comprometida) de acessar a porta 502:
# iptables -I INPUT 2 -p tcp --dport 502 -j DROP

echo "[+] Regras de Firewall atualizadas!"
