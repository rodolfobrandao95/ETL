# Extract, Transform, Load - Bolsa Família

> :warning: __To be clear__: *this repository has nothing to do with the federal government. Data collection and manipulation were done manually from the informations provided by the brazilian government's [transparency portal](http://www.transparencia.gov.br/).*

## Presentation
In this repository, I intend to demonstrate how the ETL process and multidimensional data modeling works for data warehouse, by making use of the [__Bolsa Família__](http://www.caixa.gov.br/programas-sociais/bolsa-familia/Paginas/default.aspx) program data, provided by its [REST API](http://www.transparencia.gov.br/swagger-ui.html), our datasource, to handle the data and populate a simple SQL Server database.

## Motivation
As an objective, informations about the __number of beneficiaries__, as well the __amount__ (in R$) and the __reference date__, used by the program, will be consolidated in our __fate__ dimension.

The modeling need in this scenario is to allow these metrics to be observed in two aspects:
+ __Temporal__: monthly, bimonthly, quarterly and half-yearly
+ __Spatial__: cities, states and regions

## Data gathering
In order to collect information, the following endpoint, for example, will be used:\
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
> _The illustrated JSON above represents the response we get. The displayed information is about the city of Brasília, federal district of Brazil, from 01/01/2019._

The given endpoint enables requests by passing two paramameters: `mesAno` (YYYYMM) and `codigoIbge` (state code concatenated with city code), which can be obtained from the file _CSV/municipios_IBGE.csv_.

## Requirements
Apart of `csv` and `json`, the following python modules are required to run this project:
+ [multiprocessing](https://pypi.org/project/multiprocessing/)
+ [pyodbc](https://pypi.org/project/pyodbc/)
+ [requests](https://pypi.org/project/requests/)
```
$ pip install multiprocessing
$ pip install pyodbc
$ pip install requests
```
> _Using the `pip` package installer._
