def order_summary(customer, *items, **extras):
    print("Customer:", customer)
    print("Items:", items)
    print("Extras:", extras)

order_summary("Amara", "bread", "milk", gift_wrap=True, note="Ring bell")
