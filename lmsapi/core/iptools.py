import ipaddress


def validIP(address):
    try:
        # Njepve zjistime jestli se jedna o 123.123.123.123 nebo 123456789 format

        parts = address.split(".")
        if len(parts) != 4:
            # Tak neni to fomat iptext, tetneme jestli numericky parametr je ip adrese
            # test = ipaddress.ip_address(address)
            # print(test)
            # Pokud ne, tak to vyhodi chybu
            return address
        for item in parts:
            if not 0 <= int(item) <= 255:
                return None
        return int(ipaddress.ip_address(address))
    except:
        return None
