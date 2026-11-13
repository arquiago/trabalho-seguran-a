import asyncio
from pymodbus.server import StartAsyncTcpServer
from pymodbus.datastore import ModbusSequentialDataBlock, ModbusSlaveContext, ModbusServerContext

async def main():
    # Coils 0, 1, 2 = Disjuntores das Subestações (True = Fechado/Com Energia)
    # Coil 3 = Status do Sistema / KillDisk (False = Normal, True = Sistema Destruído)
    store = ModbusSlaveContext(
        co=ModbusSequentialDataBlock(0, [True, True, True, False] + [False]*96)
    )
    context = ModbusServerContext(slaves=store, single=True)
    print("[PLC] Controlador Modbus TCP iniciado na porta 502...")
    await StartAsyncTcpServer(context=context, address=("0.0.0.0", 502))

if __name__ == "__main__":
    asyncio.run(main())
