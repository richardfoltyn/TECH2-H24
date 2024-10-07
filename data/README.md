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
- `FRED_monthly.csv`: Contains the same columns as `FRED.csv` but as monthly frequency.