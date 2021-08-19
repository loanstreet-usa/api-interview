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

    def get_loan(self, id):
        """Get loan by ID
        You must pass the id in a dictionary with key \'id\' """
        params = {'id': id}
        query = gql(
            """
            query ($id: Int!) {
                loan (id: $id) {
                    id
                    amount
                    interestRate
                    loanLengthMonths
                    monthlyPaymentAmount
                }
            }
        """
        )
        result = self.gql_client.execute(query, variable_values=params)
        return result


    def create_loan(self, params):
        """Create loan
        You must pass all parameters (amount, interest_rate, loan_length_months, monthly_payment_amount)
        as a dictionary with keys as indicated.
        """
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
        """Update loan
        You must pass all parameters (id, amount, interest_rate, loan_length_months, monthly_payment_amount)
        as a dictionary with keys as indicated.
        """
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