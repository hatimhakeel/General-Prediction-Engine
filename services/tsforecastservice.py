import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from skforecast.recursive import ForecasterRecursive
from sklearn.ensemble import RandomForestRegressor
from skforecast.model_selection import TimeSeriesFold, grid_search_forecaster
from skforecast.utils import save_forecaster, load_forecaster

sales_forecaster_model = 'salesforecaster.joblib'

def sales_forecasts(customerid, predictinterval):

    """
    A service function for sales forecasting.
    
    Parameters:
    customerid (int): Input data for customer whose sales are to be forecasted.
    predictinterval (int): Input data for sales prediction interval in days.
    
    Returns:
    dict: Forecasted sales results.
    """
def sales_forecasts_trainer(customerid):

    """
    A service function for sales forecast model training.
    
    Parameters:
    customerid (int): Input data for customer whose sales are to be forecasted.
    
    Returns:
    string: Forecast model training status.
    """
    # Simulate some processing
    forecasted_sales = {
        "January": 1200,
        "February": 1300,
        "March": 1250,
        "April": 1400,
        "May": 1500,
        "June": 1600,
    }
    
    fpath = 'data\WideWorldImporters_ToysAndMachines.csv'
    df = pd.read_csv(fpath, parse_dates=['TransactionDate'], date_format='%m/%d/%Y')

    print(df)
    print(df.dtypes)

    df[['TrxTotal']] = df.groupby('TransactionDate').agg({'TransactionAmount': 'cumsum'})
    df = df.drop_duplicates(subset=['TransactionDate'], keep='last', ignore_index=True)

    print(df)

    print("TrxTotal min:{} max:{} mean:{} median:{} std:{}".format(df['TrxTotal'].min(), df['TrxTotal'].max(), df['TrxTotal'].mean(), 
                                                              df['TrxTotal'].median(), df['TrxTotal'].std()))

    # Data exploration with histogram for distribution and scatterplot in JupyterLab project

    count, bins = np.histogram(df['TrxTotal'], bins=15)
    print("{} {}".format(count, bins))

    dfts = df.loc[:, ['TransactionDate', 'TrxTotal']]

    print(dfts.dtypes)

    dfts.set_index('TransactionDate', inplace=True)

    print(dfts)

    dftsintp = dfts.asfreq('D', fill_value=df['TrxTotal'].mean())
    dftsintp = dftsintp.sort_index()

    print(dftsintp)

    print(dftsintp.loc['2013-01-01': '2013-12-31'])
    print(dftsintp.loc['2014-01-01': '2014-12-31'])
    print(dftsintp.loc['2015-01-01': '2015-12-31'])
    print(dftsintp.loc['2016-01-01': '2016-12-31'])

    dftsintp_train = dftsintp.loc['2016-01-01': '2016-04-30']
    dftsintp_test = dftsintp.loc['2016-05-01': '2016-05-31']

    print(dftsintp_train)
    print(dftsintp_test)

    # Forecaster model training and parameter tuning with grid search

    forecaster = ForecasterRecursive(regressor=RandomForestRegressor(random_state=123, verbose=0, 
                                                                 max_depth=5, n_estimators=5), lags=30)
    forecaster.fit(y=dftsintp_train['TrxTotal'])
    print(forecaster)
    
    predictions = forecaster.predict(steps = 31)
    print(predictions.head(10))

    results = grid_search_forecaster(forecaster = forecaster, y = dftsintp_train['TrxTotal'], 
                                 cv = TimeSeriesFold(steps=31, initial_train_size=int(len(dftsintp_train) * 0.5),
                                                    refit=False, fixed_train_size=False),
                                lags_grid=[30], param_grid={'n_estimators': [5, 7, 12, 15, 50, 100, 150, 200, 250], 
                                                          'max_depth': [5, 6, 7, 8, 9, 10]},
                                metric='mean_squared_error', return_best=True, n_jobs='auto', verbose=False)

    print(results)

    save_forecaster(forecaster, file_name=f"models\{customerid}_{sales_forecaster_model}", verbose=False)


    return {"status": "success"}
