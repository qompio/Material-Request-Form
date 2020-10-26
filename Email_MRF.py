# ------------------------------------------------------------------------ #
# Title: Email MRF
# Description: Email most recent MRF to abbas after completion

# ------------------------------------------------------------------------ #
import win32com.client as win32
import os
import glob
import time
# if __name__ == "__main__":
#     raise Exception("This file is not meant to ran by itself")


def newest_path(mrf_save_path):
    list_of_files = glob.glob(mrf_save_path)
    latest_file = max(list_of_files, key=os.path.getctime)
    return latest_file


def outlook_email(mrn, latest_file, recipient_address, cc_address):
    # list_of_files = glob.glob(prod_run_path)
    #
    # latest_file = max(list_of_files, key=os.path.getctime)

    outlook = win32.Dispatch('outlook.application')
    mail = outlook.CreateItem(0)
    mail.To = recipient_address
    mail.Subject = 'Request for PO: ' + mrn
    mail.Body = 'See Attached'
    mail.CC = cc_address
    mail.HTMLBody = '<b1>Please see attached.<br>' \
                    'Email back with any questions or concerns.<br><br>' \
                    'Thanks,<br>'\
                    'William Ang'\
                    '</b1>'
    # To attach a file to the email (optional):
    mail.Attachments.Add(latest_file)

    mail.Send()


# print(str(newest_path(r"\\ces24\Metrology\Purchasing\Material Request Forms\2020" + '\\' + r'*.xlsx')))
#
# xld = win32.gencache.EnsureDispatch('Excel.Application')
# xld.Visible = True
# # time.sleep(5)
# path = str(newest_path(r"\\ces24\Metrology\Purchasing\Material Request Forms\2020" + '\\' + r'*.xlsx'))
# xld.Workbooks.Open(r"\\ces24\Metrology\Purchasing\Material Request Forms\2020\my-stout.csv")
