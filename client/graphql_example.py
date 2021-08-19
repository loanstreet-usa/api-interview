from extraction import Extractor

# TODO: Create loan
def create_loan(amount, interest_rate, loan_length_months, monthly_payment_amount):
    from .loan_schema import Loan

    next_ship = len(data["Ship"].keys()) + 1
    new_ship = Ship(id=str(next_ship), name=ship_name)
    data["Ship"][new_ship.id] = new_ship
    data["Faction"][faction_id].ships.append(new_ship.id)
    return new_ship

# TODO: Get loan
def get_loan(id):
    return data["Ship"][_id]


# TODO: Update loan






def get_faction(_id):
    return data["Faction"][_id]


def get_rebels():
    return get_faction("1")


def get_empire():
    return get_faction("2")