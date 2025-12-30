"""
Configuration file for Goyal & Welch (2008) replication
"""
from pathlib import Path

# Data paths
DATA_DIR = Path(__file__).parent / "data"
MONTHLY_DATA_FILE = DATA_DIR / "GW05_original_monthly.csv"
ANNUAL_DATA_FILE = DATA_DIR / "GW05_original_annual.csv"
UPDATED_DATA_FILE = DATA_DIR / "Goyal_Welch_2008updated.csv"

# Analysis parameters - Annual data
ANNUAL_CONFIG = {
    'start_year': 1927,
    'end_year': 2005,
    'est_periods_oos': 20,
    'dep_var': 'equity_premium',
    'indep_vars': ['dp', 'dy', 'eqis', 'b/m', 'ntis', 'de']
}

# Analysis parameters - Monthly data
MONTHLY_CONFIG = {
    'start_date': '1927-12-01',
    'end_date': '2005-12-01',
    'est_periods_oos': 240,  # 20 years
    'dep_var': 'equity_premium',
    'indep_vars': ['de', 'svar', 'lty', 'ltr', 'infl', 'tms', 'tbl',
                   'dfy', 'dp', 'dy', 'ep', 'b/m', 'e10p', 'csp', 'ntis']
}

# Special treatment variables
SPECIAL_VARS = {
    'infl': {'lag': 2, 'reason': 'Wait 1 month to get inflation data (monthly only)'},
    'csp': {'start_date': '1937-05-01', 'end_date': '2002-12-01'}
}

# Output configuration
OUTPUT_DIR = Path(__file__).parent / "output"
SAVE_PLOTS = True
PLOT_FORMAT = 'png'
PLOT_DPI = 300
