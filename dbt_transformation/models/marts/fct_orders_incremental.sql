{{
    config(
        materialized="incremental",
        unique_key="order_id",
        on_schema_change="sync_all_columns"
    )
}}

with source as (
    select *
    from {{ ref("stg_orders") }}
)

select
    order_id,
    customer_id,
    order_status,
    order_approved_at,
    order_delivered_at
from source

{% if is_incremental() %}
where
    coalesce(order_approved_at, order_delivered_at) > (
        select
            coalesce(max(coalesce(order_approved_at, order_delivered_at)), cast('1900-01-01' as timestamp))
        from {{ this }}
    )
{% endif %}
