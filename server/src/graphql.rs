use crate::loan::*;
use async_graphql::{Context, FieldResult, SimpleBroker, ID};
use futures::Stream;
use sqlx::sqlite::SqlitePool;
use tokio::stream::StreamExt;

#[async_graphql::Object]
impl Loan {
    async fn id(&self) -> &i32 {
        &self.id
    }

    async fn amount(&self) -> &f32 {
        &self.amount
    }

    async fn interest_rate(&self) -> &f32 {
        &self.interest_rate
    }

    async fn loan_length_months(&self) -> &i32 {
        &self.loan_length_months
    }

    async fn monthly_payment_amount(&self) -> &f32 {
        &self.monthly_payment_amount
    }
}

pub struct QueryRoot;

#[async_graphql::Object]
impl QueryRoot {
    async fn loans(&self, ctx: &Context<'_>) -> FieldResult<Vec<Loan>> {
        let pool = ctx.data::<SqlitePool>();
        let items = Loan::list(&pool).await?;
        Ok(items)
    }
}

pub struct MutationRoot;

#[async_graphql::Object]
impl MutationRoot {
    async fn create_loan(
        &self,
        ctx: &Context<'_>,
        amount: f32,
        interest_rate: f32,
        loan_length_months: i32,
        monthly_payment_amount: f32,
    ) -> FieldResult<Loan> {
        let pool = ctx.data::<SqlitePool>();
        let item = Loan::insert(
            &pool,
            amount,
            interest_rate,
            loan_length_months,
            monthly_payment_amount,
        )
        .await?;

        SimpleBroker::publish(LoanChanged {
            mutation_type: MutationType::Created,
            id: item.clone().id.into(),
            item: Some(item.clone()),
        });

        Ok(item)
    }

    async fn delete_loan(&self, ctx: &Context<'_>, id: ID) -> FieldResult<bool> {
        let pool = ctx.data::<SqlitePool>();
        let id = id.parse::<i32>()?;

        Loan::delete(&pool, &id).await?;

        SimpleBroker::publish(LoanChanged {
            mutation_type: MutationType::Deleted,
            id: id.into(),
            item: None,
        });

        Ok(true)
    }

    async fn update_loan(
        &self,
        ctx: &Context<'_>,
        id: ID,
        amount: f32,
        interest_rate: f32,
        loan_length_months: i32,
        monthly_payment_amount: f32,
    ) -> FieldResult<Option<Loan>> {
        let pool = ctx.data::<SqlitePool>();
        let id = id.parse::<i32>()?;

        let item = Loan::update(
            &pool,
            &id,
            &amount,
            &interest_rate,
            &loan_length_months,
            &monthly_payment_amount,
        )
        .await?;

        SimpleBroker::publish(LoanChanged {
            mutation_type: MutationType::Updated,
            id: id.into(),
            item: item.clone(),
        });

        Ok(item)
    }

    // async fn toggle_complete(&self, ctx: &Context<'_>, id: ID) -> FieldResult<Option<Loan>> {
    //     let pool = ctx.data::<SqlitePool>();
    //     let id = id.parse::<String>()?;

    //     let item = Loan::toggle_complete(&pool, &id).await?;

    //     SimpleBroker::publish(LoanChanged {
    //         mutation_type: MutationType::Updated,
    //         id: id.into(),
    //         item: item.clone(),
    //     });

    //     Ok(item)
    // }
}

#[async_graphql::Enum]
#[derive(Copy, Clone)]
enum MutationType {
    Created,
    Updated,
    Deleted,
}

#[async_graphql::SimpleObject]
#[derive(Clone)]
struct LoanChanged {
    mutation_type: MutationType,
    id: ID,
    item: Option<Loan>,
}

pub struct SubscriptionRoot;

#[async_graphql::Subscription]
impl SubscriptionRoot {
    async fn loans(&self, mutation_type: Option<MutationType>) -> impl Stream<Item = LoanChanged> {
        SimpleBroker::<LoanChanged>::subscribe().filter(move |event| {
            if let Some(mutation_type) = mutation_type {
                event.mutation_type == mutation_type
            } else {
                true
            }
        })
    }
}
