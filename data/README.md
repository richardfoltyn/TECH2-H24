# Data 

This folder contains various data sets used during the lectures and workshops.

- `missing.csv`: 3 columns of randomly generated data with missing values.
- `titanic.csv`: Passenger list of the Titanic's maiden voyage, taken
    from [pandas' data collection]([https://github.com/pandas-dev/pandas/blob/main/doc/data/titanic.csv]).

    Variables:

    1.  `PassengerId`
    2.  `Survived`: indicator whether the person survived
    3.  `Pclass`: accommodation class (first, second, third)
    4.  `Name`: Name of passenger (last name, first name)
    5.  `Sex`: `male` or `female`
    6.  `Age`
    7.  `Ticket`: Ticket number
    8.  `Fare`: Fare in pounds
    9.  `Cabin`: Deck + cabin number
    10. `Embarked`: Port at which passenger embarked:
        `C` - Cherbourg, `Q` - Queenstown, `S` - Southampton
- `FRED.csv`:
    Contains annual data from [FRED](https://fred.stlouisfed.org/),
    a standard data source for macroeconomic time series.

    Variables:

    1.  `GDP`: Real gross domestic product in billions of chained
        2017 US dollars ([GDPC1](https://fred.stlouisfed.org/series/GDPC1))
    2.  `CPI`: Consumer Price Index for All Urban Consumers: All Items in U.S. City Average
        ([CPIAUCSL](https://fred.stlouisfed.org/series/CPIAUCSL)).
        Price level is normalised so that the average in 1982-1984 is 100.
    3.  `UNRATE`: Unemployment rate in percent ([UNRATE](https://fred.stlouisfed.org/series/UNRATE))
    4.  `FEDFUNDS`: Effective Federal Funds Rate in percent ([FEDFUNDS](https://fred.stlouisfed.org/series/FEDFUNDS))

- `FRED.xlsx`: Same contents as `FRED.csv`, stored in Excel format.
- `FRED_monthly.csv`: 
    Contains _monthly_ data from [FRED](https://fred.stlouisfed.org/),
    a standard data source for macroeconomic time series.

    Variables:

    1.  `CPI`: Consumer Price Index for All Urban Consumers: All Items in U.S. City Average
        ([CPIAUCSL](https://fred.stlouisfed.org/series/CPIAUCSL)).
        Price level is normalised so that the average in 1982-1984 is 100.
    2.  `UNRATE`: Unemployment rate in percent ([UNRATE](https://fred.stlouisfed.org/series/UNRATE))
    3.  `FEDFUNDS`: Effective Federal Funds Rate in percent ([FEDFUNDS](https://fred.stlouisfed.org/series/FEDFUNDS))
    4.  `REALRATE`: 1-Year Real Interest Rate in percent ([REAINTRATREARAT1YE](https://fred.stlouisfed.org/series/REAINTRATREARAT1YE))
    5.  `LFPART`: Labor Force Participation Rate in percent ([CIVPART](https://fred.stlouisfed.org/series/CIVPART))

- `ames_houses.csv`: Housing data from Ames, Iowa. 

    Based on the data provided by Kuhn (2020) on [CRAN](https://cran.r-project.org/web/packages/AmesHousing/index.html)

   The data was originally published in
   _De Cock (2011): "Ames, Iowa: Alternative to the Boston Housing Data as an End of Semester Regression Project",
   Journal of Statistics Education, 19(3). DOI: [https://doi.org/10.1080/10691898.2011.11889627](https://doi.org/10.1080/10691898.2011.11889627)_ 

   Variables:
   
    1.  `SalePrice`: House price in US dollars (float)
    2.  `LotArea`: Size of the lot in m² (float)
    3.  `Neighborhood`: Name of the neighborhood (string)
    4.  `BuildingType`: Type of building (categorical stored as string)
    5.  `OverallQuality`: Rates the overall condition of the house from (1) "very poor" to (10) "excellent" (integer)
    6.  `OverallCondition`: Rates the overall material and finish of the house from (1) "very poor" to (10) "excellent" (integer)
    7.  `YearBuilt`: Original construction date (integer)
    8.  `CentralAir`: Central air conditioning: Yes/No (categorical string)
    9.  `LivingArea`: Above-ground living area in m² (float)
    10. `Bathrooms`: Number of bathrooms (integer)
    11. `Bedrooms`: Number of bedrooms (integer)
    12. `Fireplaces`: Number of fireplaces (integer)
    13. `HasGarage`: Indicator whether house has a garage (integer)

- `DJIA.csv`: Daily closing price of the Dow Jones Industrial Average since 2020-01-02, obtained from Yahoo! Finance
- `SP500.csv`: Daily closing price of the S&P 500 since 2020-01-02, obtained from Yahoo! Finance
- `NASDAQ.csv`: Daily closing price of the NASDAQ composite since 2020-01-02, obtained from Yahoo! Finance

- `population_norway.csv`: Population by municipality (kommune) as of January 1, 2024.

    Source: SSB, [https://www.ssb.no/statbank/sq/10102933](https://www.ssb.no/statbank/sq/10102933)
    
