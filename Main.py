# -------------------------------------------------------------------------------------------------------------------- #
# Title: Main running file of OTV rev.02
# Description: OTV takes user input on asset#, company, vendor,
# quantity, price. Searches established db using asset# to fill item specific
# info. Uses input to establish customer company, vendor, quant/price
# uses dictionary key/value to obtain customer company shipping number, and
# vendor mailing address.
# -------------------------------------------------------------------------------------------------------------------- #
# Imports
# -------------------------------------------------------------------------------------------------------------------- #
from IOclasses import IO
from ExcelWrite import XL as xl
from Data import *
from GIMSSQL_Query import fetch
from prettytable import PrettyTable
from shipping_accs import shipping_acx
from Email_MRF import *
import win32com.client as win32
# -------------------------------------------------------------------------------------------------------------------- #
# Constants
# -------------------------------------------------------------------------------------------------------------------- #
items = []
xliste = []
mrf_dir = r"\\ces24\Metrology\Purchasing\Material Request Forms\2020"   # change this path when the year changes
index = 1
VENDOR = IO.get_vendor()
MRN = IO.get_material_request_number()
RMA = IO.get_rma()
mail_to = 'abbas@cascade-eng.com'
# -------------------------------------------------------------------------------------------------------------------- #
# MAIN
# -------------------------------------------------------------------------------------------------------------------- #
while True:

    IO.print_menu_items()

    # Menu of Options
    # 1) ENTER ITEM
    # 2) SHOW LIST OF ITEMS
    # 3) DELETE ITEM FROM LIST
    # 4) WRITE MRF AND SAVE
    # 5) EMAIL MRF TO ABBAS
    # 6) QUIT

    choice = IO.input_menu_choice()
    # if 1 then allow user to enter gage_id, quantity and price
    if choice == '1':
        # instantiate new item
        new_item = Item(index, *fetch(IO.get_gage_id()), IO.get_price(), IO.get_quantity())
        # add item to list of items to print for user
        items.append(new_item)
        # add item in stupid MRF formatting to xliste
        xliste.append(new_item.rev_mrf_format())
        # increment the index
        index += 1
        continue

    # if choice = 2 then show list of current items being sent out
    elif choice == '2':
        t = PrettyTable(['Index', 'GageID', 'Model#', 'Serial Number', 'MFG', 'Description',
                         'Client Company', 'Certificate Type', 'Price', 'Quantity'])
        for item in items:
            t.add_row(item.to_list())
        print(t)
        continue

    # if choice = 3 then delete user choice from list
    elif choice == '3':
        # remove the item
        print('Functionality not added yet. :) lol')
        continue

    # if choice = 4 write the info obtained to the excel sheet
    elif choice == '4':
        xl.write_mrf_details(MRN, items[0].company, shipping_acx(items[0].company), RMA, index,
                             items[0].gage_id, items[0].cert_template, VENDOR)      # item[0].company()??

        xl.write_item(xliste)
        xl.save_sheet(MRN, mrf_dir, VENDOR)
        xld = win32.Dispatch('Excel.Application')
        xld.Visible = True
        xld.Workbooks.Open('r"' + newest_path(mrf_dir + '\\' + r'*.xlsx') + '"')
        continue

    # if choice = 5 email the latest saved sheet to abbas
    elif choice == '5':
        outlook_email(MRN, newest_path(mrf_dir + '\\' + r'*.xlsx'), mail_to, "")
        print("~~~~~~~EMAIL SENT~~~~~~~")
        continue
    # if choice = 6 quit the program
    elif choice == '6':
        break
    else:
        print("The command was not recognized, please enter a number [1-5]")
        continue

