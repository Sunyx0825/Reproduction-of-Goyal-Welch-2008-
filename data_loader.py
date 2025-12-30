"""
Data loading and preprocessing module for Goyal & Welch (2008) replication
"""
import numpy as np
import pandas as pd
from pathlib import Path
from config import MONTHLY_DATA_FILE, ANNUAL_DATA_FILE


def load_annual_data(file_path=None):
    """
    Load and preprocess annual data

    Parameters:
    -----------
    file_path : str or Path, optional
        Path to the annual data file

    Returns:
    --------
    pd.DataFrame
        Preprocessed annual data
    """
    if file_path is None:
        file_path = ANNUAL_DATA_FILE

    # Read data
    data_annual = pd.read_csv(file_path, sep=';', decimal=',')
    data_annual.set_index('yyyy', inplace=True)

    # Create derived variables
    data_annual['dp'] = np.log(data_annual["D12"]) - np.log(data_annual["Index"])
    data_annual['dy'] = np.log(data_annual["D12"]) - np.log(data_annual["Index"].shift(1))
    data_annual['de'] = np.log(data_annual["D12"]) - np.log(data_annual["E12"])
    data_annual['equity_premium'] = np.log1p(data_annual['CRSP_SPvw']) - np.log1p(data_annual['Rfree'])

    return data_annual


def load_monthly_data(file_path=None, start_date='1927-11-01'):
    """
    Load and preprocess monthly data

    Parameters:
    -----------
    file_path : str or Path, optional
        Path to the monthly data file
    start_date : str, optional
        Start date for filtering data

    Returns:
    --------
    pd.DataFrame
        Preprocessed monthly data
    """
    if file_path is None:
        file_path = MONTHLY_DATA_FILE

    # Read data
    data_monthly = pd.read_csv(file_path, sep=';', decimal=',')
    data_monthly['yyyymm'] = pd.to_datetime(data_monthly['yyyymm'], format='%Y%m')
    data_monthly.rename(columns={'yyyymm': 'date'}, inplace=True)

    # Filter data
    if start_date:
        data_monthly = data_monthly[data_monthly['date'] >= start_date]

    # Create derived variables
    data_monthly['dp'] = np.log(data_monthly["D12"]) - np.log(data_monthly["Index"])
    data_monthly['dy'] = np.log(data_monthly["D12"]) - np.log(data_monthly["Index"].shift(1))
    data_monthly['ep'] = np.log(data_monthly["E12"]) - np.log(data_monthly["Index"])
    data_monthly['de'] = np.log(data_monthly["D12"]) - np.log(data_monthly["E12"])
    data_monthly['e10p'] = np.log(data_monthly['E12'].rolling(window=120).mean()) - np.log(data_monthly['Index'])
    data_monthly['tms'] = data_monthly['AAA'] - data_monthly['tbl']
    data_monthly['dfy'] = data_monthly['BAA'] - data_monthly['AAA']

    # Equity premium
    data_monthly['log_equity_premium'] = np.log1p(data_monthly['CRSP_SPvw']) - np.log1p(data_monthly['Rfree'])
    data_monthly['equity_premium'] = data_monthly['CRSP_SPvw'] - data_monthly['Rfree']
    data_monthly['equity_premium_lag'] = data_monthly['equity_premium'].shift(1)
    data_monthly['abs_ep_lag'] = data_monthly['equity_premium'].abs().shift(1)
    data_monthly['sign_lag'] = (data_monthly['equity_premium'] > 0).astype(int).shift(1)

    # Remove first row due to shifts
    data_monthly = data_monthly[1:]

    # Set date as index
    data_monthly.set_index('date', inplace=True)

    return data_monthly


def get_data_summary(data, data_type='monthly'):
    """
    Get summary statistics of the data

    Parameters:
    -----------
    data : pd.DataFrame
        Input data
    data_type : str
        Type of data ('monthly' or 'annual')

    Returns:
    --------
    dict
        Summary statistics
    """
    summary = {
        'data_type': data_type,
        'n_observations': len(data),
        'start_date': data.index.min(),
        'end_date': data.index.max(),
        'equity_premium_mean': data['equity_premium'].mean(),
        'equity_premium_std': data['equity_premium'].std(),
        'equity_premium_min': data['equity_premium'].min(),
        'equity_premium_max': data['equity_premium'].max(),
    }

    return summary
