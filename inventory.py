IP_list_file_path = r".\IP_list.txt"
device_inventory = []

with open(IP_list_file_path, 'r') as file:
    # Use list comprehension to create a list of items from each line
    switch_list = file.read().splitlines()
    
for ip in switch_list:
    device = {
        "device_type": "cisco_ios",
        "host": ip,
        "username": "komsak.w",
        "password": "P@ssw0rd",
        "secret": "P@ssw0rd",  # Enable password
        "timeout": 120
        
    }
    device_inventory.append(device)
    