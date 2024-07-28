# Saleh Razavi 2069661

import csv

class InventoryInput:
    def __init__(self):
        self.manufacturer_data = {}
        self.price_data = {}
        self.service_date_data = {}

    def read_manufacturer_list(self, file_path='ManufacturerList.csv'):
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                item_id = row[0]
                manufacturer = row[1]
                item_type = row[2]
                damaged = row[3] if len(row) > 3 else ""
                self.manufacturer_data[item_id] = {
                    "manufacturer": manufacturer,
                    "item_type": item_type,
                    "damaged": damaged
                }

    def read_price_list(self, file_path='PriceList.csv'):
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                item_id = row[0]
                price = row[1]
                self.price_data[item_id] = price

    def read_service_dates_list(self, file_path='ServiceDatesList.csv'):
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                item_id = row[0]
                service_date = row[1]
                self.service_date_data[item_id] = service_date

    def read_all_files(self):
        self.read_manufacturer_list()
        self.read_price_list()
        self.read_service_dates_list()

