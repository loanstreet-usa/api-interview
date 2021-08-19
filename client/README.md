# LoanStreet API Client

## Installation

Install [Python](https://www.python.org/) 3.6 or later
Install [Poetry](https://python-poetry.org/)

## Using the API client

Before using the API client, you need to create a virtual environment in the base `client` folder:

```sh
poetry shell
```

and install the Python dependencies:

```sh
poetry install
```

You must also have the server running (see `client` folder for more information)

To use the API client, instantiate a client object from LoanStreetClient.

```python

from client import LoanStreetClient

result = client.get_all_loans()
```

### Examples

#### Get all loans

client = LoanStreetClient()

result = client.get_all_loans()

pp.pprint(result)

#### Create loan

```python

from client import LoanStreetClient

params = {
'amount': 5203.01,
'interest_rate': 1.01,
'loan_length_months': 30,
'monthly_payment_amount': 5.43
}

result = client.update_loan(params)
print(result)

```

## Supported behavior

- get_loan
- get_all_loans
- create_loan
- update_loan

See function docstrings for more information
