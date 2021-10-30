import os
import pandas as pd
from crochet import setup, wait_for
from scrapy.utils.log import configure_logging


class Stock:
    def __init__(self, name, ticker='', directory=None):
        self.name = name
        self.ticker = ticker
        self.dir = directory
        self.main_df = pd.DataFrame()
        self.calculations_df = pd.DataFrame()
        self.calculations_df['Criterion'] = []
        self.calculations_df['Value'] = []
        self.calculations_df['Passed'] = []
        self.calculations_df['Note(s)'] = []
        self.balance_sheet_dict = {}
        self.stats_dict = {'Trailing 12 Month EPS': 0,
                           'Current Price': 0,
                           'Book Value per Share': 0}

        setup()
        # configure_logging()

    @wait_for(20)
    def run_spider(self, spider_key_word: str):
        from importlib import import_module
        lower_key = spider_key_word.lower()
        module_name = "web_scraping.web_scraping.spiders.{}_spider".format(lower_key)
        imported_spider_class = import_module(module_name)  # can't seem to import using this
        arg_dict = {'name': self.name,
                    'ticker': self.ticker,
                    'filepath': self.dir,
                    'stock': self}
        my_class = getattr(imported_spider_class, "Spider")
        #spider = imported_spider_class.Spider(**arg_dict)
        from scrapy.crawler import CrawlerRunner
        crawler = CrawlerRunner()
        process = crawler.crawl(my_class, **arg_dict)
        return process

    def set_attr(self, attribute_name: str, attribute_value) -> None:
        setattr(self, attribute_name, attribute_value)

    def concatenate_df(self, df_to_concat):
        if self.main_df.empty:
            self.main_df = df_to_concat
        else:
            self.main_df = self.main_df.merge(df_to_concat, on='Year', how='outer')
            self.main_df = self.main_df.sort_values('Year', ascending=False).reset_index(drop=True)




