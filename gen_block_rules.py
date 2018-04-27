# -*- coding: utf-8 -*-

# Please uncomment template for generate rule for appropriate format

# rules for iptables
# tmpl = """iptables -A INPUT -s {item} -j DROP"""

# rules for mictorik
# tmpl = """add address={item} list=MRG"""

# rules for ufw firewall
# tmpl = """ufw deny from {item}"""

# rules for firewalld
tmpl = """firewall-cmd --permanent --add-rich-rule="rule family='ipv4' source address='{item}' reject" """

block_list = [
    '5.61.16.0/21',
    '5.61.232.0/21',
    '79.137.157.0/24',
    '79.137.174.0/23',
    '79.137.183.0/24',
    '94.100.176.0/20',
    '95.163.32.0/19',
    '95.163.212.0/22',
    '95.163.216.0/22',
    '95.163.248.0/21',
    '128.140.168.0/21',
    '178.22.88.0/21',
    '178.237.16.0/20',
    '178.237.29.0/24',
    '185.5.136.0/22',
    '185.16.148.0/22',
    '185.16.244.0/23',
    '185.16.246.0/24',
    '185.16.247.0/24',
    '188.93.56.0/21',
    '194.186.63.0/24',
    '195.211.20.0/22',
    '195.218.168.0/24',
    '217.20.144.0/20',
    '217.69.128.0/20'
]

for item in block_list:
    print(tmpl.format(item=item))
