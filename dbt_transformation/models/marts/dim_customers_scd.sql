with snapshot as (
    select *
    from {{ ref("customers_snapshot") }}
)

select
    customer_id,
    email,
    gender,
    city,
    country,
    dbt_valid_from,
    dbt_valid_to,
    case when dbt_valid_to is null then true else false end as is_current
from snapshot
