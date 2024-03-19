from mac_vendor_lookup import MacLookup

def is_unicast(mac_address):
    try:
        #  Extracting the first hex value
        first_hex = mac_address.split(":")[0][:2]
        second_half = int(first_hex[1], 16)
        #  Converting the second half to binary and checking LSB
        second_half_binary = bin(second_half)[2:].zfill(4)  #  Ensure it's 4 bits long
        if (second_half_binary[-1] == '0'):
            return mac_address
    except ValueError:
        return False


def get_mac_addresss(mac_address):
    try:
        if is_unicast(mac_address):
            return MacLookup().lookup(mac_address)
        else:
            return None
    except Exception as e:
        return f"Error: {e}"
    

def main():
    mac_addres = input("ENter the mac address")
    company_name = get_mac_addresss(mac_addres)
    mac_address_to_company = {}
    if company_name:
        mac_address_to_company[mac_addres] = company_name
        print(mac_address_to_company)
    else:
        print("No company name found")

if __name__ == "__main__":
    main()  