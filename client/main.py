from client import LoanStreetClient

if __name__ == "__main__":
  import pprint as pp

  client = LoanStreetClient()

  result = client.get_all_loans()

  pp.pprint(result)