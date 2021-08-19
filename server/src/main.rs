mod graphql;
mod loan;
mod result;
mod web;

use dotenv::dotenv;
use result::Result;
use sqlx::sqlite::SqlitePool;

#[tokio::main]
async fn main() -> Result<()> {
    dotenv().ok();

    let pool = SqlitePool::builder()
        .max_size(1)
        .build("sqlite://./loanstreet.sqlite3")
        .await
        .unwrap();

    sqlx::query!(
        "CREATE TABLE IF NOT EXISTS loan (
                    id                      INTEGER PRIMARY KEY NOT NULL,
                    amount                  REAL NOT NULL,
                    interest_rate           REAL NOT NULL,
                    loan_length_months      INTEGER NOT NULL,
                    monthly_payment_amount  REAL NOT NULL) "
    )
    .execute(&pool)
    .await?;

    // let loan1 = loan::Loan {
    //     id: 0,
    //     amount: 5_032.45,
    //     interest_rate: 2.01,
    //     loan_length_months: 102,
    //     monthly_payment_amount: 12.1,
    // };

    // let loan2 = Loan {
    //     id: 1,
    //     amount: 6_234.87,
    //     interest_rate: 1.23,
    //     loan_length_months: 405,
    //     monthly_payment_amount: 50.2,
    // };

    // insert ID as null here to allow sqlite to autoincrement
    // sqlx::query!(
    //     "INSERT INTO loan (id, amount, interest_rate, loan_length_months, monthly_payment_amount)
    //               VALUES (NULL, {amount}, {interest_rate}, {loan_length_months}, {monthly_payment_amount})",
    //     &[
    //         amount = &loan1.amount,
    //         &loan1.interest_rate,
    //         &loan1.loan_length_months,
    //         &loan1.monthly_payment_amount,
    //     ]
    // )
    // .unwrap();

    sqlx::query!(
        "INSERT INTO loan (id, amount, interest_rate, loan_length_months, monthly_payment_amount)
                  VALUES (NULL, 5032.45, 2.01, 102, 12.1)"
    )
    .execute(&pool)
    .await?;
    // .unwrap();

    web::start(pool).await;
    Ok(())
}
