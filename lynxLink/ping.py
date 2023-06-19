import datetime
import subprocess

def main():
    open("./ping.txt", "w").truncate(0)
    ping = subprocess.check_output("ping -c 5 8.8.8.8 | tail -1 | awk '{print $4}' | cut -d '/' -f 2", shell=True)
    goodping = ping.decode()
    firstnow = datetime.datetime.now()
    now = (firstnow.strftime("%Y-%m-%d %H:%M:%S"))

    filename = "./ping.txt"

    with open(filename, 'a') as f:
        f.write(f'Date : {now}| Ping : {goodping} \n')
        
main()