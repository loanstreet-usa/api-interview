# from dotenv import load_dotenv

from loan_schema import LoanSchema

from gql import Client, gql
from gql.transport.requests import RequestsHTTPTransport
import pprint as pp

# transport = RequestsHTTPTransport(
#     url="https://countries.trevorblades.com/", verify=True, retries=3,
# )

transport = RequestsHTTPTransport(
    url="http://127.0.0.1:8080", verify=True, retries=3,
)

client = Client(transport=transport, schema=LoanSchema)

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

result = client.execute(query)
pp.pprint(result)
