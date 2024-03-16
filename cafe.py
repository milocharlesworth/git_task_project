menu = ["Coffee", "Tea", "Water", "Biscuits"]  # Outlining items on the menu

# Taking stock
Stock_value = {
    "Coffee": 15,
    "Tea": 25,
    "Water": 40,
    "Biscuits": 70,
}

# Storing prices of items
Item_price = {"Coffee": 4,
            "Tea": 3,
            "Water": 1,
            "Biscuits": 1
}

# Calculating total stock revenue
total_stock_worth = sum(Stock_value[item] * Item_price[item] for item in menu)

# Printing total
print(total_stock_worth)
