#usr/bin/env python3
#coding:utf8                                            import netifaces,nmap,socket

print('''
 ____       _       _
|  _ \ __ _(_)_ __ (_)_ __   __ _
| |_) / _` | | '_ \| | '_ \ / _` |
|  _ < (_| | | | | | | | | | (_| |
|_| \_\__,_|_|_| |_|_|_| |_|\__, |
                 ____       |___/
                / ___|  ___ __ _ _ __
                \___ \ / __/ _` | '_ \\
                 ___) | (_| (_| | | | |
                |____/ \___\__,_|_| |_|
                                   
[1] 启用自动扫描
[2] 自定义扫描
[3] 手动端口扫描

    感谢使用雨扫
''')

def get_gateways():
    return netifaces.gateways()['default'][netifaces.AF_INET][0]                                                
def get_ip_lists(ip):
    ip_lists = []
    for i in range(1, 256):
        ip_lists.append('{}{}'.format(ip[:-1], i))
    return ip_lists

def main_RS1(ip=None):
    ip=get_gateways()
    ip_lists=get_ip_lists(ip)
    nmScan,temp_ip_lists,hosts = nmap.PortScanner(),[],ip[:-1]+'0/24'
    ret = nmScan.scan(hosts=hosts, arguments='-sP')
    print('扫描时间：'+ret['nmap']['scanstats']['timestr']+'\n命令参数:'+ret['nmap']['command_line'])
    for ip in ip_lists:
        print('ip地址：'+ip+'：')
        if ip not in ret['scan']:
            temp_ip_lists.append(ip)
            print('扫描超时')
        else:print('已扫描到主机，主机名：'+ret['scan'][ip]['hostnames'][0]['name'])
    print(str(hosts) +' 网络中的存活主机:')
    for ip in temp_ip_lists:ip_lists.remove(ip)
    for ip in ip_lists:print(ip)

def main_RS2(ip=None):                                      ip=input("请输入ip网段:")
    ip_lists=get_ip_lists(ip)
    nmScan,temp_ip_lists,hosts = nmap.PortScanner(),[],ip[:-1]+'0/24'
    ret = nmScan.scan(hosts=hosts, arguments='-sP')
    print('扫描时间：'+ret['nmap']['scanstats']['timestr']+'\n命令参数:'+ret['nmap']['command_line'])               for ip in ip_lists:                                         print('ip地址：'+ip+'：')
        if ip not in ret['scan']:
            temp_ip_lists.append(ip)
            print('扫描超时')
        else:print('已扫描到主机，主机名：'+ret['scan'][ip]['hostnames'][0]['name'])
    print(str(hosts) +' 网络中的存活主机:')
    for ip in temp_ip_lists:ip_lists.remove(ip)
    for ip in ip_lists:print(ip)

def main_RS3():
    ip = raw_input("请输入IP:")
    port = input("请输入端口:")
    sock = socket.socket(socket.AF_INET,socket.SOCK_SYREAM)
    if sock.connect_ex((ip,port)):
        print ("端口",port,"未打开")
    else:
        print ("端口",port,"已打开")

if __name__ == '__main__':
    RSn=input("输入要选择的模式:")
    RSmode=int(RSn)
    if RSmode==1:
        print("欢迎使用Raining-scan默认扫描模式")
        main_RS1
    if RSmode==2:
        print('''
欢迎使用Raining-scan自定义扫描模式
帮助:这个脚本用于扫描局域网内的存活主机,通常局域>网网段分为以下三种:
C类:192.168.0.0-192.168.255.255
B类：172.16.0.0-172.31.255.255
A类：10.0.0.0-10.255.255.255
''')
        main_RS2
    if RSmode==3:
        print("欢迎使用手动端口扫描,只要输入ip和对应端口就可以扫描端口是否开放.")
        main_RS3
