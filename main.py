import os
import pandas as pd
import pprint

#### IDEAS ####
# Please comment any ideas
#~Which data fields are needed must be determined exactly
# Data that is scraped might be stored in a local database or remote database
# this way we are going to get retrieve the data faster and Only
# scraping this years' data would be enough.
# This module is scrapes only 'value investing algorithm's data
#~Multhreading can be implemented
#~This can be turned into an api and this api can be deployed on the cloud
#with multiple instances. maybe docker like system




def main():
    import Stock
    dummy_stock = Stock.Stock("apple")
    dummy_stock.run_spider('ticker')
    # yukarda facebook un company nameinden ticker sembolu olan FB yi scrape ettik ve
    # Bunu ticker_spider isimli class ile yaptik. Bulunan degeri stock classinin ilgili
    #fieldina yazdik
    run_all_spiders(dummy_stock)
    # geriye kalan 4 spider ile scrape etmeye devam ettik ama yeterli degil bazi fieldlar
    # eklememiz lazim
    print_stock(dummy_stock) # buldugumuz datalari yazdirdik.

def print_stock(stock):
    # stock.main_df.set_index('Year', inplace=True)

    print(stock.main_df.to_string(justify='Center'))
    print("#########################################")
    pprint.pprint(stock.balance_sheet_dict, sort_dicts=False)
    print("#########################################")
    pprint.pprint(stock.stats_dict)
    print("#########################################")






def run_all_spiders(stock):
    # Dividends goes first because it has more rows (since 1989)
    stock.run_spider('dividends')
    stock.run_spider('eps')
    stock.run_spider('balance_sheet')
    stock.run_spider('price_to_book')




if __name__ == '__main__':
    main()
