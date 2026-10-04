def calculate_change(purchase_price: float, cash_given: float) -> str:
    currency = [
        ("ONE HUNDRED", 10000),
        ("FIFTY", 5000),
        ("TWENTY", 2000),
        ("TEN", 1000),
        ("FIVE", 500),
        ("TWO", 200),
        ("ONE", 100),
        ("HALF DOLLAR", 50),
        ("QUARTER", 25),
        ("DIME", 10),
        ("NICKEL", 5),
        ("PENNY", 1),
    ]

    pp_cents = round(purchase_price * 100)
    ch_cents = round(cash_given * 100)

    if ch_cents < pp_cents:
        return "ERROR"
    if ch_cents == pp_cents:
        return "ZERO"

    change_cents = ch_cents - pp_cents
    result = []

    for name, value in currency:
        while change_cents >= value:
            result.append(name)
            change_cents -= value

    result.sort()
    return ", ".join(result)


# Test cases
if __name__ == "__main__":
    print(calculate_change(15.94, 16.00))  # NICKEL, PENNY
    print(calculate_change(10.00, 50.00))  # TWENTY, TWENTY
    print(calculate_change(10.00, 10.00))  # ZERO
    print(calculate_change(20.00, 10.00))  # ERROR