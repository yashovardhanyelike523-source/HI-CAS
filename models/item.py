class Item:
    def __init__(self, name, qty, price, category, expiry):
        self.name = name
        self.qty = qty
        self.price = price
        self.category = category
        self.expiry = expiry

    def to_dict(self):
        return {
            "name": self.name,
            "qty": self.qty,
            "price": self.price,
            "category": self.category,
            "expiry": self.expiry
        }