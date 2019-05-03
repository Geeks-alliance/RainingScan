#!/usr/bin/python
#coding:utf8
import netifaces,nmap

print("欢迎使用Raining-scan自定义扫描模式")
print("帮助:这个脚本用于扫描局域网内的存活主机,通常局域网网段分为以下三种:")
print("C类:192.168.0.0-192.168.255.255")
print("B类：172.16.0.0-172.31.255.255")
print("A类：10.0.0.0-10.255.255.255")

def get_ip_lists(ip):
    ip_lists = []
    for i in range(1, 256):
        ip_lists.append('{}{}'.format(ip[:-1], i))
    return ip_lists

def main(ip=None):
    ip=input("请输入ip网段（例:192.168.1.1）：")
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

if __name__ == '__main__':
    main()
