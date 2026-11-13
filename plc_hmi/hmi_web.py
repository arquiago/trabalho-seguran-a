from flask import Flask, jsonify, render_template_string
from pymodbus.client import ModbusTcpClient

app = Flask(__name__)
PLC_IP = "127.0.0.1"

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>SCADA HMI - Prykarpattyaoblenergo (Ucrânia 2015)</title>
    <style>
        body { background: #0f172a; color: #f8fafc; font-family: monospace; text-align: center; padding: 20px; }
        .grid { display: flex; justify-content: center; gap: 20px; margin-top: 30px; }
        .card { padding: 25px; border-radius: 8px; width: 220px; border: 2px solid #334155; background: #1e293b; }
        .online { border-color: #22c55e; box-shadow: 0 0 15px rgba(34,197,94,0.3); }
        .offline { border-color: #ef4444; background: #450a0a; box-shadow: 0 0 20px rgba(239,68,68,0.6); }
        .status { font-size: 20px; font-weight: bold; margin-top: 10px; }
        button { margin-top: 30px; padding: 12px 24px; font-size: 16px; cursor: pointer; background: #3b82f6; color: white; border: none; border-radius: 6px; font-weight: bold; }
    </style>
</head>
<body>
    <h1>⚡ SCADA HMI - Subestação Regional de Kiev</h1>
    <p>Monitoramento em Tempo Real via Modbus TCP (172.28.0.10:502)</p>
    <div id="killdisk-banner" style="display:none; background:#dc2626; padding:15px; font-size:22px; font-weight:bold;">
        ⚠️ ALERTA CRÍTICO: ASSINATURA MBR CORROMPIDA (KILLDISK DETECTADO) ⚠️
    </div>
    <div class="grid" id="painel"></div>
    <button onclick="resetar()">🔄 Religar Disjuntores Manualmente (Reset Lab)</button>

    <script>
        async function atualizar() {
            const res = await fetch('/status');
            const data = await res.json();
            const nomes = ["Subestação Kiev-01", "Subestação Ivano-02", "Subestação Chernivtsi-03"];
            let html = "";
            for(let i=0; i<3; i++) {
                const ligado = data.coils[i];
                html += `<div class="card ${ligado ? 'online' : 'offline'}">
                    <h3>${nomes[i]}</h3>
                    <div>Tensão: ${ligado ? '110 kV' : '0 kV'}</div>
                    <div class="status" style="color:${ligado ? '#4ade80' : '#f87171'}">
                        ${ligado ? 'FECHADO (ONLINE)' : 'ABERTO (APAGÃO)'}
                    </div>
                </div>`;
            }
            document.getElementById('painel').innerHTML = html;
            document.getElementById('killdisk-banner').style.display = data.coils[3] ? 'block' : 'none';
        }
        async function resetar() {
            await fetch('/reset', {method: 'POST'});
            atualizar();
        }
        setInterval(atualizar, 1000);
        atualizar();
    </script>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route("/status")
def status():
    client = ModbusTcpClient(PLC_IP, port=502)
    client.connect()
    res = client.read_coils(0, 4)
    client.close()
    return jsonify({"coils": res.bits[:4] if not res.isError() else [False, False, False, False]})

@app.route("/reset", methods=["POST"])
def reset():
    client = ModbusTcpClient(PLC_IP, port=502)
    client.connect()
    client.write_coils(0, [True, True, True, False])
    client.close()
    return jsonify({"ok": True})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
