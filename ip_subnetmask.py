

def ip_subnet_calculator(ip, subnet):
    ip_split_list = list(map(int, ip.split('.')))
    subnet_split_list = list(map(int, subnet.split('.')))

    ip_bin_list = []
    subnet_bin_list = []
    for i in range(4):
        ip_bin_list.append(format(ip_split_list[i], '08b'))
        subnet_bin_list.append(format(subnet_split_list[i], '08b'))

    ip_bin_octets = ''.join(ip_bin_list)
    subnet_bin_octets = ''.join(subnet_bin_list)


    network_id_bin_list = []
    for i in range(32):
        if ip_bin_octets[i] == '1' and subnet_bin_octets[i] == '1':
            network_id_bin_list.append('1')
        else:
            network_id_bin_list.append('0')

    network_id_bin_list = [''.join(network_id_bin_list[0:8]), ''.join(network_id_bin_list[8:16]), ''.join(network_id_bin_list[16:24]), ''.join(network_id_bin_list[24:32])]

    network_id_list = []
    for i in network_id_bin_list:
        network_id_list.append(str(int(i, 2)))

    cidr = subnet_bin_octets.count('1')
    network_id = '.'.join(network_id_list)
    
    print('네트워크 ID :', network_id)
    print('CIDR        :', cidr)

