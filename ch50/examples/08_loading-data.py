from pathlib import Path

sales_csv = """order_id,city,product,units,price
1,London,Widget,5,9.99
2,Tokyo,Gadget,2,19.99
3,London,Gadget,1,19.99
4,Nairobi,Widget,8,9.99
5,Tokyo,Widget,3,9.99
6,Nairobi,Gadget,4,19.99
7,London,Widget,6,9.99
8,Tokyo,Gadget,,19.99
"""
Path("sales.csv").write_text(sales_csv)
print("sales.csv written")
