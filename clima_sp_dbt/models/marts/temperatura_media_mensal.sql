{{ config(
    materialized='table',
) }}

select
    strftime('%Y-%m', data) || '-01' AS safra,
    avg(temperatura_media) AS temperatura_media,
    avg(umidade_media) AS umidade_media,
    avg(pressao_media) AS pressao_media
from {{ ref('temperatura_media_diaria') }}