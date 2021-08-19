# GraphQL API for LoanStreet interview

This GraphQL API implements basic CRUD behavior and subscriptions.

## Running

Clone the repo and run

```bash
cargo run
```

Open `http://localhost:8080` in your browser to see the GraphQL playground.

## GraphQL queries

### Get all loans

```graphql
query	{
  loans {
    id
    amount
    interestRate
    loanLengthMonths
    monthlyPaymentAmount
  }
}
```

### Subscribe to loans

Open two windows to the GraphQL playground.

In the first window, do:

```graphql
subscription {
  loans {
    id
    mutationType
    item
  }
}
```

In the second window, create a new loan by doing:

```graphql
mutation {
  createLoan(amount: 4023.32,
  interestRate: 1.05,
  loanLengthMonths: 104,
  monthlyPaymentAmount: 12.1
  ) {
    id
  }
}
```
