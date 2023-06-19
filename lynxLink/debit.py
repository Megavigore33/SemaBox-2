import subprocess

subprocess.run(["rm ./debit.txt"], shell=True)

dl = subprocess.check_output("speedtest | grep Download | awk '{print $3 $4}'", shell=True)
up = subprocess.check_output("speedtest | grep Upload | awk '{print $3 $4}'", shell=True)

open("./ping.txt", "w").truncate(0)
filename = "./debit.txt"

with open(filename, 'a') as f:
    f.write(f'dl : {dl.decode()}up : {up.decode()}')
