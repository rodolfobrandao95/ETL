# Extract, Transform, Load
#### In this repository, I intend to demonstrate how multi dimensional data modeling for Data Warehouse and ETL process works by applying it manually.

#### For this sample, it will be used the _Bolsa Família_ program data, provided by the brazilian government's transparency [REST API](http://www.transparencia.gov.br/swagger-ui.html).

___

As an objective, informations about the _number of beneficiaries_, as well as the _total amount_ (in R$), used by the program, will be consolidated.

The modeling need is to allow these metrics to be observed in two aspects:
* __Time Dimension__: monthly, bimonthly, quarterly and half-yearly
* __City Dimension__: city, state and region

The _Bolsa Família_ program information can be obtained by the following URI:\
http://www.transparencia.gov.br/api-de-dados/bolsa-familia-por-municipio/?mesAno=201901&codigoIbge=5300108&pagina=1

And as response, we get the following JSON:

```json
[
    {
        "id": 78300058,
        "dataReferencia": "01/01/2019",
        "municipio": {
            "codigoIBGE": "5300108",
            "nomeIBGE": "BRASÍLIA",
            "nomeIBGEsemAcento": "BRASILIA",
            "pais": "BRASIL",
            "uf": {
                "sigla": "DF",
                "nome": "DISTRITO FEDERAL"
            }
        },
        "tipo": {
            "id": 1,
            "descricao": "Bolsa Família",
            "descricaoDetalhada": "Bolsa Família"
        },
        "valor": 12013474.00,
        "quantidadeBeneficiados": 66650
    }
]
```
> The illustrated JSON above is about the city of Brasília, from 01/01/2019.

The given URI enables requests by two params: __date__ (YYYYMM) and __IBGE code__ (state code + city code), which can be obtained from the .csv file contained in this project.
