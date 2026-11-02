# stock_tool.py
# Author: David Leatherman


class StockLookup:
    """A tool that tracks product inventory counts."""

    def __init__(self, stock):
        self.stock = stock

    def find_product(self, text):
        """Return the first known product or None."""
        text_lower = text.lower()
        for product in self.stock:
            if product.lower() in text_lower:
                return product
        return None

    def count_for(self, product):
        """Return inventory count for product or None."""
        return self.stock.get(product, None)