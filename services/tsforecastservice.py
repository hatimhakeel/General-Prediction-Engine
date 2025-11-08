import pandas as pd
import numpy as np

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

    return {"status": "success"}
