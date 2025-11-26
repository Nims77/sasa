import platform
import subprocess
import socket
import datetime
import shutil
def system_info():
    info={}
    info["OS"]=platform.system()
    info["os version"]=platform.version()
    info["machine"]=platform.machine()
    info["processor"]=platform.processor()
    hostname=socket.gethostname()
    ip=socket.gethostbyname(hostname)
    info["hostname"]=hostname
    info["ip"]=ip
    return info
def system_health():
    health={}
    health["disk"]=shutil.disk_usage('/')
    return health
def port_scan(target_ip):
    open_port=[]
    print(f"sacnning ports on:{target_ip} ")
    for port in range(1,1000):
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.settimeout(0.02)
        result=s.connect_ex((target_ip,port))
        if result==0:
            open_port.append(port)
        s.close()
    return open_port
def save_report(system_info,system_health,open_ports):
    times=datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename="report"+times+".txt"
    with open(filename,"w") as f:
        f.write("system information:\n")
        for key,value in system_info.items():
            f.write(f"{key}:{value}\n")
        f.write("\nSystem Health:\n")
        for key,value in system_health.items():
            f.write(f"{key}:{value}\n")
        f.write("\nOpen Ports:\n")
        for port in open_ports:
            if open_ports:
                f.write(f"Port {port} is open\n")
            else:
                f.write("no open ports\n")
    print(f"Report saved as {filename}")
if __name__ == "__main__":

 info=system_info()
 health=system_health()
 print("enter the ip adress to be scanned: ")
 target_ip=input()
 ports=port_scan(target_ip)
 save_report(info,health,ports)
 print("scan complete")


