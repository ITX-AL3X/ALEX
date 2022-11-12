from platform import uname
bit=uname().machine.lower()
if 'aarch' in bit:
    import Alex
    Alex.menu()
else:
    exit(' 32bit Device not Supported ')
