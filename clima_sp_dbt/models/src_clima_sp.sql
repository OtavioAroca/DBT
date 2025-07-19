{{ config(materialized='table') }}

select * from clima_sp
