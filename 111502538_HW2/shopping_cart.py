from abc import ABC, abstractmethod
from functools import reduce


# 商品基類
class Product(ABC):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @abstractmethod
    def accept(self, visitor):
        pass


# 食品類
class Food(Product):
    def accept(self, visitor):
        return visitor.visit_food(self)


# 電子產品類
class Electronics(Product):
    def accept(self, visitor):
        return visitor.visit_electronics(self)


# 訪問者模式實作
class TaxVisitor:
    def visit_food(self, product):
        return 0  # 食品免稅

    def visit_electronics(self, product):
        return product.price * 0.1  # 電子產品稅率為 10%


# 購物車類
class ShoppingCart:
    def __init__(self, products):
        self.products = products

    # 計算總價格
    def calculate_total(self):
        return sum(map(lambda p: p.price, self.products))  # Functional Programming

    # 計算總稅收
    def calculate_tax(self, visitor):
        return sum(map(lambda p: p.accept(visitor), self.products))  # Functional Programming

    # 生成報表
    def generate_report(self, visitor):
        total = self.calculate_total()
        tax = self.calculate_tax(visitor)
        grand_total = total + tax
        return f"Total: ${total:.2f}, Tax: ${tax:.2f}, Grand Total: ${grand_total:.2f}"


# 測試程式
if __name__ == "__main__":
    # 建立商品
    apple = Food("Apple", 2.5)
    laptop = Electronics("Laptop", 1200.0)
    bread = Food("Bread", 1.5)
    phone = Electronics("Phone", 800.0)

    # 建立購物車
    cart = ShoppingCart([apple, laptop, bread, phone])

    # 訪問者
    tax_visitor = TaxVisitor()

    # 輸出報表
    #print(cart.generate_report(tax_visitor))

    # 測試案例
    print("Test Case: 空購物車")
    print(ShoppingCart([]).generate_report(tax_visitor))
    print()

    print("Test Case: 僅食品")
    print(ShoppingCart([apple, bread]).generate_report(tax_visitor))
    print()

    print("Test Case: 僅電子產品")
    print(ShoppingCart([laptop, phone]).generate_report(tax_visitor))
    print()

    print("Test Case: 混合商品")
    print(ShoppingCart([apple, laptop, bread]).generate_report(tax_visitor))
    print()