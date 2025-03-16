from netmiko import ConnectHandler
import inventory

def ssh(device_info,ip_address):
    hostname = ""
    
    # try:
    with ConnectHandler(**device_info) as net_connect:
        # device> Enable
        net_connect.enable()
        prompt = net_connect.find_prompt()
        hostname = prompt[0:-1]
        
        # # print hostname and IP address
        # print("\n"+hostname+" : "+ device_info['host']+"")
        
        # config
        net_connect.send_config_set(["vlan 888","name TEST-VLAN"])
        
        # show information
        output = net_connect.send_command('show vlan br')
        print(output)
        
        net_connect.disconnect()
    # except:
    #     failed_reason = f"{ip_address} - TCP connection to device failed."
    #     print(failed_reason)
        
if __name__ == "__main__":

    ## Multi host ##
    
    # device = inventory.device_inventory
    # for device_info in device:
    #     ip_address = device_info["host"]
    #     ssh(device_info, ip_address)
    
    ## Single host ##
    
    device_info = {
        "device_type": "cisco_ios",
        "host": "192.168.159.5",
        "username": "admin",
        "password": "P@ssw0rd",
        "secret": "P@ssw0rd",  # Enable password
    }
    
    ip_address = device_info["host"]
    ssh(device_info, ip_address)