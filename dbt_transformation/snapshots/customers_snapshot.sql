{% snapshot customers_snapshot %}

{{
    config(
        target_schema="snapshots",
        unique_key="customer_id",
        strategy="check",
        check_cols=["email", "gender", "city", "country"]
    )
}}

select
    customer_id,
    email,
    gender,
    city,
    country
from {{ source("raw_data", "customers") }}

{% endsnapshot %}
