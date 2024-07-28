# Saleh Razavi 2069661

from FinalProjectInput import InventoryInput
from FinalProjectProcessing import InventoryProcessor

def main():
    inventory_input = InventoryInput()
    inventory_input.read_all_files()

    inventory_processor = InventoryProcessor(
        inventory_input.manufacturer_data,
        inventory_input.price_data,
        inventory_input.service_date_data
    )
    inventory_processor.process_and_write_all()

if __name__ == "__main__":
    main()
