import asyncio
from bleak import BleakScanner

async def run():
    print("🔍 Сканируем Bluetooth-устройства...")
    devices = await BleakScanner.discover()
    for d in devices:
        print(f"📡 {d.name} | {d.address} | RSSI: {d.rssi} dBm")

asyncio.run(run())
