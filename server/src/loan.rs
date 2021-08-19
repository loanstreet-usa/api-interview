use crate::result::Result;
use sqlx::sqlite::SqlitePool;
// use uuid::Uuid;

#[derive(Debug, Clone)]
pub struct Loan {
    pub id: i32,
    pub amount: f32,
    pub interest_rate: f32,
    pub loan_length_months: i32,
    pub monthly_payment_amount: f32,
}

impl Loan {
    pub async fn insert(
        pool: &SqlitePool,
        amount: f32,
        interest_rate: f32,
        loan_length_months: i32,
        monthly_payment_amount: f32,
    ) -> Result<Loan> {
        // do BEGIN so you get the correct rowid
        sqlx::query!(
            "INSERT INTO loan VALUES (NULL, $1, $2, $3, $4)",
            amount,
            interest_rate,
            loan_length_months,
            monthly_payment_amount,
        )
        .execute(pool)
        .await?;

        // TODO: get ID back from inserted record with last_insert_rowid()

        Ok(Loan {
            id: -1,
            amount: amount,
            interest_rate: interest_rate,
            loan_length_months: loan_length_months,
            monthly_payment_amount: monthly_payment_amount,
        })
    }

    pub async fn list(pool: &SqlitePool) -> Result<Vec<Loan>> {
        let loans = sqlx::query_as!(Loan, "SELECT * FROM loan")
            .fetch_all(pool)
            .await?;

        Ok(loans)
    }

    pub async fn get_loan(pool: &SqlitePool, id: &i32) -> Result<Option<Loan>> {
        let loan: Option<Loan> = sqlx::query_as!(Loan, "SELECT * FROM loan WHERE id=$1", id)
            .fetch_optional(pool)
            .await?;

        Ok(loan)
    }

    pub async fn update(
        pool: &SqlitePool,
        id: &i32,
        amount: &f32,
        interest_rate: &f32,
        loan_length_months: &i32,
        monthly_payment_amount: &f32,
    ) -> Result<Option<Loan>> {
        sqlx::query!(
            "UPDATE loan SET amount=$1, interest_rate=$2, loan_length_months=$3, monthly_payment_amount=$4 WHERE id=$5",
            amount,
            interest_rate,
            loan_length_months,
            monthly_payment_amount,
            id,
        )
        .execute(pool)
        .await?;

        let loan: Option<Loan> = sqlx::query_as!(Loan, "SELECT * FROM loan WHERE id=$1", id)
            .fetch_optional(pool)
            .await?;

        Ok(loan)
    }

    pub async fn delete(pool: &SqlitePool, id: &i32) -> Result<()> {
        sqlx::query!("DELETE FROM loan WHERE id=$1", id)
            .execute(pool)
            .await?;

        Ok(())
    }
}
