#测试
#Ghos9527

import asyncio
from bleak import BleakScanner

async def run():
    print(" 正在扫描蓝牙设备...")
    devices = await BleakScanner.discover()
    for d in devices:
        print(f" {d.name} | {d.address} | RSSI: {d.rssi} dBm")

asyncio.run(run())
