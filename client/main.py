# from dotenv import load_dotenv

from gql import Client, gql
from gql.transport.requests import RequestsHTTPTransport
import pprint as pp

transport = RequestsHTTPTransport(
    url="http://127.0.0.1:8080", verify=True, retries=3,
)

client = Client(transport=transport, fetch_schema_from_transport=True)

query = gql(
    """
    query {
      loans {
        id
        amount
        interestRate
        loanLengthMonths
        monthlyPaymentAmount
      }
    }
"""
)

# TODO: Create loan

create_loan_query = gql(
    """
    query getContinentName ($code: ID!) {
      continent (code: $code) {
        name
      }
    }
"""
)
)


# TODO: Get loan

# TODO: Update loan

# TODO: Get all loans - optional

result = client.execute(query)
pp.pprint(result)



if __name__ == "__main__":
    result = client.execute(query)
    pp.pprint(result)