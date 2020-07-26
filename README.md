# Extract, Transform, Load - Bolsa Família

> :warning: __To be clear__: *this repository has nothing to do with the federal government. Data collection and manipulation were done manually from the informations provided by the brazilian government's [transparency portal](http://www.transparencia.gov.br/).*

## Presentation
The act of execute the __ETL__ steps basicaly refers to the process of transferring data from one location to another. In addition to migrating data from one database to another, it also converts databases into a single format that can be utilized in the final destination. These main steps are:
+ __Extract__: collecting data from a database or any other source. At this point, the data is often from multiple and different types of sources.
+ __Transform__: converting recently extracted data into the correct form, so that it can be placed into another database. This process is crucial to ensuring data from one database or application can be utilized by other applications and databases. Some key functions here include:
  - Standardization to a consistent set of lookup values;
  - Cleansing through validity checks to remove or modify problematic data;
  - Transposing, usually via deformalizing and reorganizing into a dimensional model to optimize reporting;
  - Creating surrogate keys that are new values applied to similar data from different source systems.
+ __Load__: when the data is finnaly written into the target database or ETL data warehouse.

![etl_process](https://miro.medium.com/max/700/1*8GR7mLvaVulyvAiwXTM_3w.png)

In this repository, I intend to demonstrate how the ETL process and multidimensional data modeling works for data warehouse, by making use of the [__Bolsa Família__](http://www.caixa.gov.br/programas-sociais/bolsa-familia/Paginas/default.aspx) program data, provided by its [REST API](http://www.transparencia.gov.br/swagger-ui.html), our datasource, to handle the data and populate a simple SQL Server database.

## Motivation
As an objective, informations about the __number of beneficiaries__, as well the __amount__ (in R$) and __reference date__, used by the program, will be consolidated in our _fate_ dimension.

The modeling need in this scenario is to allow these metrics to be observed in two aspects:
+ __Time Dimension__: monthly, bimonthly, quarterly and half-yearly
+ __City Dimension__: city, state and region

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
> The illustrated JSON above represents the response we get. The displayed information is about the city of Brasília, from 01/01/2019.

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
> Using the `pip` package installer.
---
Repository created and maintained by me, [@rodolfobrandao_](https://twitter.com/rodolfobrandao_)
