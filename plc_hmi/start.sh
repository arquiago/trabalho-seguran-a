#!/bin/bash
# Envia pacotes TCP na porta 502 (Modbus) para o Suricata IPS avaliar (--queue-bypass garante que se o Suricata cair, a rede não trava)
iptables -I INPUT -p tcp --dport 502 -j NFQUEUE --queue-num 0 --queue-bypass
iptables -I OUTPUT -p tcp --sport 502 -j NFQUEUE --queue-num 0 --queue-bypass

python -u /app/plc_server.py &
python -u /app/hmi_web.py
