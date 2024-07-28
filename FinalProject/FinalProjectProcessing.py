# Saleh Razavi 2069661

import csv
from datetime import datetime

class InventoryProcessor:
    def __init__(self, manufacturer_data, price_data, service_date_data):
        self.manufacturer_data = manufacturer_data
        self.price_data = price_data
        self.service_date_data = service_date_data
        self.inventory = []

    def merge_data(self):
        for item_id, data in self.manufacturer_data.items():
            price = self.price_data.get(item_id, "")
            service_date = self.service_date_data.get(item_id, "")
            self.inventory.append({
                "item_id": item_id,
                "manufacturer": data["manufacturer"],
                "item_type": data["item_type"],
                "price": price,
                "service_date": service_date,
                "damaged": data["damaged"]
            })

    def write_full_inventory(self, file_path='FullInventory.csv'):
        sorted_inventory = sorted(self.inventory, key=lambda x: x["manufacturer"])
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            for item in sorted_inventory:
                writer.writerow([
                    item["item_id"],
                    item["manufacturer"],
                    item["item_type"],
                    item["price"],
                    item["service_date"],
                    item["damaged"]
                ])

    def write_item_type_inventory(self):
        item_types = {}
        for item in self.inventory:
            item_type = item["item_type"]
            if item_type not in item_types:
                item_types[item_type] = []
            item_types[item_type].append(item)

        for item_type, items in item_types.items():
            sorted_items = sorted(items, key=lambda x: x["item_id"])
            file_name = f"{item_type.capitalize()}Inventory.csv"
            with open(file_name, mode='w', newline='') as file:
                writer = csv.writer(file)
                for item in sorted_items:
                    writer.writerow([
                        item["item_id"],
                        item["manufacturer"],
                        item["price"],
                        item["service_date"],
                        item["damaged"]
                    ])

    def write_past_service_date_inventory(self, file_path='PastServiceDateInventory.csv'):
        current_date = datetime.now()
        past_service_items = [
            item for item in self.inventory
            if datetime.strptime(item["service_date"], '%m/%d/%Y') < current_date
        ]
        sorted_items = sorted(past_service_items, key=lambda x: datetime.strptime(x["service_date"], '%m/%d/%Y'))
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            for item in sorted_items:
                writer.writerow([
                    item["item_id"],
                    item["manufacturer"],
                    item["item_type"],
                    item["price"],
                    item["service_date"],
                    item["damaged"]
                ])

    def write_damaged_inventory(self, file_path='DamagedInventory.csv'):
        damaged_items = [item for item in self.inventory if item["damaged"]]
        sorted_items = sorted(damaged_items, key=lambda x: float(x["price"]), reverse=True)
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            for item in sorted_items:
                writer.writerow([
                    item["item_id"],
                    item["manufacturer"],
                    item["item_type"],
                    item["price"],
                    item["service_date"]
                ])

    def process_and_write_all(self):
        self.merge_data()
        self.write_full_inventory()
        self.write_item_type_inventory()
        self.write_past_service_date_inventory()
        self.write_damaged_inventory()
