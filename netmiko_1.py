from netmiko import ConnectHandler
from pprint import pprint
import huawei_conf as cfg
h_type = cfg.d_type
u_name = cfg.u_name
h_password = cfg.pwd
h_port = cfg.h_port

huawei_1 = {'device_type': h_type, 'ip': '10.200.199.12', 'username': u_name, \
'password': h_password,'port': h_port }
huawei_2 = {'device_type': h_type, 'ip': '10.200.199.13', 'username': u_name, \
'password': h_password,'port': h_port }
huawei_3 = {'device_type': h_type, 'ip': '10.200.199.14', 'username': u_name, \
'password': h_password,'port': h_port }
huawei_4 = {'device_type': h_type, 'ip': '10.200.199.15', 'username': u_name, \
'password': h_password,'port': h_port }

huawei_acc_cores = [huawei_1, huawei_2, huawei_3, huawei_4]

def connection(h):
    net_connect = ConnectHandler(**h)
    sshConfirm = net_connect.find_prompt()
    print('login ' + sshConfirm)
    commands = ['display interface description']
    output = net_connect.send_config_set(commands)
    pprint(output, width=120)
    print("_"*100)
    net_connect.disconnect()

if __name__ == "__main__":
    for h in huawei_acc_cores:
        connection(h)
