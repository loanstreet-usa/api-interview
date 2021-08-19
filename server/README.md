# GraphQL API for LoanStreet interview

This GraphQL API implements basic CRUD behavior and subscriptions.

## Running the server

Install [Rust](https://www.rust-lang.org/) so you can use `cargo`

Use the Rust nightly build:

```sh
rustup default nightly
```

Install [Sqlite3](https://sqlite.org/index.html)
If you are on Mac/Linux, you can do:

```sh
brew install sqlite3
```

Create a sqlite3 database called `loanstreet.sqlite3`:

```sh
sqlite3 loanstreet.sqlite3

Clone the repo and in the base `server` directory, run:

```sh
cargo run
```

Open `http://localhost:8080` in your browser to see the GraphQL playground.

## Example GraphQL queries

### Get all loans

```graphql
query {
  loans {
    id
    amount
    interestRate
    loanLengthMonths
    monthlyPaymentAmount
  }
}
```

### Get one loan by ID

```graphql
query {
  loan(id:1) {
    id
    amount
    interestRate
    loanLengthMonths
    monthlyPaymentAmount
  }
}
```

Note that the query is `loan` and not `loans`.

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
