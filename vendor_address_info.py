# ------------------------------------------------------------------------ #
# Title: Shipping Accounts
# Description: Matches vendor name to their shipping address information, if they have any. If
# they don't have any, then it will default to ship ground.
# called inside of main module, sending the information to the excel write module
# ------------------------------------------------------------------------ #
if __name__ == "__main__":
    raise Exception("This file is not meant to ran by itself")

shipping_address = {'LEDFORD': ['LEDFORD GAGE', '227 INDUSTRIAL DR', 'MULVANE, KS 67110', '800-237-4243'],
                    'KEYSIGHT': ['KEYSIGHT', '10090 FOOTHILLS BLVD #1276', 'ROSEVILLE, CA 95747', '800-829-4444'],
                    'OMEGA ENGINEERING OMEGA': ['Omega Engineering Inc', 'One Omega Circle', 'Bridgeport NJ 08014',
                                                '888-773-4019'],
                    'FLUKE (IL)': ['FLUKE ELECTRONICS', '2 SCIENCE RD., BLDG 4', 'GLENWOOD, IL 60425', '833.296.9240'],
                    'FLUKE (WA)': ['FLUKE ELECTRONICS', '1420 75th Street SW', 'Bldg 4', 'Everett, WA 98203',
                                   '888.993.5853'],
                    'KONICA MINOLTA': ['KONICA MINOLTA', '101 Williams Drive', 'Ramsey, NJ 07446', '201-785-2449'],
                    'MITUTOYO': ['MITUTOYO', '16925 E. GALE AVE', 'CITY OF INDUSTRY CA, 91745'],
                    'NDC TECHNOLOGIES': ['NDC TECHNOLOGIES', '454 Smith Street', 'Middletown, CT  06457',
                                         '1-800-284-7975'],
                    'DIGIVAC': ['DIGIVAC', '1020 Campus Dr W', 'Morganville, NJ 07751', '732-765-0900'],
                    'APPLIED TECHNICAL SERVICES (ATS)': ['Applied Technical Services, Inc', 'Attn: Cal Lab',
                                                         '1049 Triad Court', 'Marietta, GA 30062', '770-423-1400'],
                    'TEKTRONIX (WA)': ['TEKTRONIX INC', '18939 120th Ave', 'Ste 111', 'Bothell WA 98011',
                                       '800-438-8165'],
                    'TEKTRONIX (OR)': ['TEKTRONIX INC', '13725 SW KARL BRAUN DR', 'BLDG. 19', 'BEAVERTON, OR 97077',
                                       '503-627-6031'],
                    'RIEKER INC': ['RIEKER INC', '34 MOUNT PLEASANT RD', 'ASTON, PA 19014', '610-500-2000'],
                    'OCEAN OPTICS INC': ['OCEAN OPTICS, INC', '4301 METRIC DRIVE', 'WINTER PARK, FL  32792',
                                         '727-733-2447'],
                    'TELEDYNE LECROY': ['LECROY Corp.', '700 CHESTNUT RIDGE RD', 'CHESTNUT RIDGE, NY 10977',
                                        '800-553-2769'],
                    'IKONIX': ['IKONIX', '28105 N KEITH DR', 'LAKE FOREST, IL 60045', '847.367.4671'],
                    'STARRETT': ['Starrett Calibration Services', '321 Tucapau Road', 'Duncan, SC  29334',
                                 '864-433-8407'],
                    }


def enter_address():
    company = input("COMPANY: ")
    street_address = input('STREET ADDRESS: ')
    city = input('CITY: ')
    state = input('STATE: ')
    zip = input('ZIP: ')
    phone = input('PHONE#: ')
    return {company: [company, street_address, city + ',' + state + zip, phone]}


def vendor_address(vendor_search):
    for k, v in shipping_address.items():  # .items() returns key and value
        if str(vendor_search) in "FLUKE":
            choice = input("Enter [1] or [2]\n"
                           "[1] : FLUKE (IL)\n"
                           "[2] : FLUKE (WA)\n")
            if choice == 1:
                return {
                    'FLUKE (IL)': ['FLUKE ELECTRONICS', '2 SCIENCE RD., BLDG 4', 'GLENWOOD, IL 60425', '833.296.9240']}
            elif choice == 2:
                return {'FLUKE (WA)': ['FLUKE ELECTRONICS', '1420 75th Street SW', 'Bldg 4', 'Everett, WA 98203',
                                       '888.993.5853']}

        elif str(vendor_search) in "TEKTRONIX":
            choice = input("Enter [1] or [2]\n"
                           "[1] : TEKTRONIX (WA)\n"
                           "[2] : TEKTRONIX (OR)\n")
            if choice == 1:
                return {'TEKTRONIX (WA)': ['TEKTRONIX INC', '18939 120th Ave', 'Ste 111', 'Bothell WA 98011',
                                           '800-438-8165']}
            elif choice == 2:
                return {'TEKTRONIX (OR)': ['TEKTRONIX INC', '13725 SW KARL BRAUN DR', 'BLDG. 19', 'BEAVERTON, OR 97077',
                                           '503-627-6031']}
        elif str(vendor_search).upper().strip() in k:
            # if v[0] =
            return v
        else:
            return enter_address()
