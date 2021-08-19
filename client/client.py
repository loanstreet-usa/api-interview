from gql import Client, gql
from gql.transport.requests import RequestsHTTPTransport

class LoanStreetClient:
    """Client to use LoanStreet API"""

    def __init__(self):

        import pprint as pp

        transport = RequestsHTTPTransport(
            url="http://127.0.0.1:8080", verify=True, retries=3,
        )

        self.gql_client = Client(transport=transport, fetch_schema_from_transport=True)

    def get_all_loans(self):
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
        result = self.gql_client.execute(query)
        return result

    # TODO: Finish create_loan()
    def create_loan(self, params):
        query = gql(    """
            mutation ($amount: Float!, $interest_rate: Float!, $loan_length_months: Int!, $monthly_payment_amount: Float!) {
                createLoan (
                    amount: $amount,
                    interestRate: $interest_rate,
                    loanLengthMonths: $loan_length_months,
                    monthlyPaymentAmount: $monthly_payment_amount
                )
            {
                id
            }
            }
        """)

        result = self.gql_client.execute(query, variable_values=params)
        return result

    def update_loan(self, params):
        query = gql(    """
            mutation ($id: ID!, $amount: Float!, $interest_rate: Float!, $loan_length_months: Int!, $monthly_payment_amount: Float!) {
                updateLoan (
                    id: $id,
                    amount: $amount,
                    interestRate: $interest_rate,
                    loanLengthMonths: $loan_length_months,
                    monthlyPaymentAmount: $monthly_payment_amount
                )
            {
                id
            }
            }
        """)

        result = self.gql_client.execute(query, variable_values=params)
        return result