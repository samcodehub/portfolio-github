import subprocess
result = subprocess.check_output(["netsh","wlan","show","network"])
result = result.decode("ascii")
result = result.replace("\r","")
ls = result.split("\n")
ls = ls[4:]
ssids = []
x = 0
while x < len(ls):
    if x%5==0:
        ssids.append(ls[x])
    x+=1
print(ssids)