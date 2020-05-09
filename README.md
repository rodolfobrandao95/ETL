# Extract, Transform, Load
#### In this repository, I intend to demonstrate how multi dimensional data modeling for Data Warehouse and ETL process works by applying it manually.

#### For this sample, it will be used the _Bolsa Família_ program data, provided by the brazilian government's transparency [REST API](http://www.transparencia.gov.br/swagger-ui.html).

___

As an objective, informations about the __number of beneficiaries__, as well as the __amount__ (in R$), used by the program, will be consolidated.

The modeling need in this scenario is to allow these metrics to be observed in two aspects:
* __Time Dimension__: monthly, bimonthly, quarterly and half-yearly
* __City Dimension__: city, state and region

___

In order to get the data from the _Bolsa Família_ program (per month), we'll use the following URI:\
http://www.transparencia.gov.br/api-de-dados/bolsa-familia-por-municipio/?mesAno=201901&codigoIbge=5300108&pagina=1

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
> The illustrated JSON above represents the response we get from the API. The information shown is about the city of Brasília, from 01/01/2019.

The given URI enables requests by passing two paramameters: __mesAno__ (YYYYMM) and __codigoIbge__ (state code concatenated with city code), which can be obtained from the provided file _municipios_IBGE.csv_.
