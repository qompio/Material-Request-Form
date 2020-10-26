# ------------------------------------------------------------------------ #
# Title: Shipping Accounts
# Description: Matches customer name to their shipping information, if they have any. If
# they don't have any, then it will default to ship ground.
# called inside of main module, sending the information to the excel write module
# ------------------------------------------------------------------------ #
if __name__ == "__main__":
    raise Exception("This file is not meant to ran by itself")
# Imports ---------------------------------------------------------------- #

# Dictionary ------------------------------------------------------------- #
shipping_acc = {'PHILIPS ULTRASOUND': ['666666', 'UPS'],
                'SAFRAN CABIN': ['66666', 'UPS'],
                'SAGEMAX BOIOCERAMICS': ['666666', 'UPS'],
                'SEAMETRICS': ['66666', 'UPS'],
                'SGL': ['666666', 'UPS'],
                'SPECTRUM CONTROLS': ['6666666', 'UPS'],
                'TEK MACHINING': ['666666', 'UPS'],
                "TERRY'S MACHINE": ['66666', 'UPS'],
                'TETHERS': ['666666', 'FEDEX'],
                'UNILODE - HEBRON, KY': ['6666666', 'FEDEX'],
                'UNILODE AVIATION SOL': ['6666666', 'UPS'],
                'US ELECTRODYNAMICS': ['6666666', 'UPS'],
                'VARIAN': ['66666', 'UPS'],
                'WOODSTONE': ['6666666', 'UPS']
                }


# [value for key, value in programs.items() if new_item.company() in key.upper()]
# if shipping_acc contains new_item.company()
# ship_acc_num = shipping_acc[new_item.company()]


def shipping_acx(searchterm):
    ground_ship = 'Return ship Ground; Prepay & Add'
    for k, v in shipping_acc.items():  # .items() returns key and value
        if str(searchterm) in "SAFRAN CABIN":
            choice = input("Enter [1] or [2]\n"
                           "[1] : FEDEX\n"
                           "[2] : UPS\n")
            if choice == 1:
                return ['6007 76843', 'FEDEX']
            elif choice == 2:
                return ['05487X', 'UPS']
        elif str(searchterm) in k:
            return v
        else:
            return ground_ship

# print(search(shipping_acc, other_test.upper()))
