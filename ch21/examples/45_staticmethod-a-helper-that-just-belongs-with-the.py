class BankAccount:
    # ...(rest of the class as before)...

    @staticmethod
    def is_valid_amount(amount):
        return (type(amount) in (int, float)
                and amount > 0
                and (type(amount) is int or math.isfinite(amount)))
