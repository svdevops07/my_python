nativeVLAN = input('The native VLAN is: ')
dataVLAN = input('The data VLAN is: ')
if nativeVLAN == dataVLAN:
    print('The native VLAN and the data VLAN are the same.')
else:
    print('The native VLAN and the data VLAN are different.')