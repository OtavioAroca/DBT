-- models/temperatura_media_diaria.sql
{{ config(materialized='table') }}
select
    date(data_hora_coleta) as data,
    avg(temperatura) as temperatura_media,
    avg(umidade) as umidade_media,
    avg(pressao) as pressao_media
from {{ ref('src_clima_sp') }}
group by 1
order by 1
