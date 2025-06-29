#!/usr/bin/python3

import platform
import socket
import subprocess
import time

sysinfo = "=" * 20 + "System Information" + "=" * 20 + '\n'
uname = platform.uname()
sysinfo += f"System: {uname.system}\n"
sysinfo += f"Node Name: {uname.node}\n"
sysinfo += f"Release: {uname.release}\n"
sysinfo += f"Version: {uname.version}\n"
sysinfo += f"Machine: {uname.machine}\n"
sysinfo += f"Processor: {uname.processor}\n"

sysinfo += "=" * 20 + "CPU Information" + "=" * 20 + '\n'
lscpu = subprocess.check_output(["lscpu"]).decode("utf-8")
sysinfo += lscpu

sysinfo += "=" * 20 + "Memory Information" + "=" * 20 + '\n'
free = subprocess.check_output(["cat", "/proc/meminfo"]).decode("utf-8")
sysinfo += free

sysinfo += "=" * 20 + "Storage Information" + "=" * 20 + '\n'
lsblk = subprocess.check_output(["lsblk"]).decode("utf-8")
sysinfo += lsblk

sysinfo += "=" * 20 + "PCI Device Information" + "=" * 20 + '\n'
try:
    lspci = subprocess.check_output(["lspci"]).decode("utf-8")
    sysinfo += lspci
except:
    sysinfo += "PCI information unavailable\n"


sysinfo += "=" * 20 + "USB Device Information" + "=" * 20 + '\n'
try:
    lsusb = subprocess.check_output(["lsusb"]).decode("utf-8")
    sysinfo += lsusb
except:
    sysinfo += "USB information unavailable\n"

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
ip = s.getsockname()[0]
s.close()
currtime = time.time()
host = f"{uname.node}-{ip}-{currtime}"
out = open(f"{host}.txt", 'w')
out.write(sysinfo)
out.close()
