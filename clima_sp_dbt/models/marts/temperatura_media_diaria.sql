{{ config(
    materialized='incremental',
    unique_key='data'
) }}

select
    date(data_hora_coleta) as data,
    avg(temperatura) as temperatura_media,
    avg(umidade) as umidade_media,
    avg(pressao) as pressao_media
from clima_sp

{% if is_incremental() %}
where date(data_hora_coleta) NOT IN (select data from {{ this }})
{% endif %}

group by 1
order by 1