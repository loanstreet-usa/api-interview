import pprint as pp

from client import LoanStreetClient

if __name__ == "__main__":

  client = LoanStreetClient()

  result = client.get_all_loans()

  pp.pprint(result)