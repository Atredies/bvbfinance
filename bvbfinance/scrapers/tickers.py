import requests
import os

# Downloading the full file with all tickets on BVB
BVB_SHARE_DOWNLOAD_URL = 'https://bvb.ro/FinancialInstruments/Markets/SharesListForDownload.ashx'

def download_bvb_shares(file_name):
    url = BVB_SHARE_DOWNLOAD_URL
    url_results = requests.get(url)

    cwd = os.path.dirname(os.path.abspath(__file__))
    save_location = os.path.join(cwd, '../data', file_name)

    with open(save_location, 'wb') as downloaded_shares_csv:
         downloaded_shares_csv.write(url_results.content)

    return save_location