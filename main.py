"""
Main executable script for Goyal & Welch (2008) replication

This script provides a command-line interface to replicate the results from:
Goyal, A., & Welch, I. (2008). A comprehensive look at the empirical performance
of equity premium prediction. The Review of Financial Studies, 21(4), 1455-1508.

Usage:
    python main.py --mode annual --plot
    python main.py --mode monthly --variable dp --plot
    python main.py --mode all
"""

import argparse
import sys
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

from data_loader import load_annual_data, load_monthly_data, get_data_summary
from helper import get_statistics, get_monthly_statistics
from config import (
    ANNUAL_CONFIG, MONTHLY_CONFIG, SPECIAL_VARS,
    OUTPUT_DIR, SAVE_PLOTS, PLOT_FORMAT, PLOT_DPI
)


def setup_output_directory():
    """Create output directory if it doesn't exist"""
    OUTPUT_DIR.mkdir(exist_ok=True)


def run_annual_analysis(variables=None, plot=False):
    """
    Run analysis on annual data

    Parameters:
    -----------
    variables : list, optional
        List of independent variables to analyze
    plot : bool
        Whether to generate plots
    """
    print("\n" + "="*60)
    print("Annual Data Analysis")
    print("="*60)

    # Load data
    data_annual = load_annual_data()
    print(f"\nData loaded: {len(data_annual)} observations")
    print(f"Period: {data_annual.index.min()} - {data_annual.index.max()}")

    # Summary statistics
    summary = get_data_summary(data_annual, 'annual')
    print(f"\nEquity Premium Statistics:")
    print(f"  Mean: {summary['equity_premium_mean']:.4f}")
    print(f"  Std:  {summary['equity_premium_std']:.4f}")
    print(f"  Min:  {summary['equity_premium_min']:.4f}")
    print(f"  Max:  {summary['equity_premium_max']:.4f}")

    # Use default variables if none specified
    if variables is None:
        variables = ANNUAL_CONFIG['indep_vars']

    # Run analysis for each variable
    results = {}
    plot_mode = 'yes' if plot else 'no'

    for var in variables:
        if var not in data_annual.columns:
            print(f"\nWarning: Variable '{var}' not found in data, skipping...")
            continue

        print(f"\n--- Analyzing variable: {var} ---")
        try:
            result = get_statistics(
                data_annual,
                indep=var,
                dep=ANNUAL_CONFIG['dep_var'],
                start=ANNUAL_CONFIG['start_year'],
                end=ANNUAL_CONFIG['end_year'],
                est_periods_OOS=ANNUAL_CONFIG['est_periods_oos'],
                plot=plot_mode
            )
            results[var] = result
            print(f"  IS R² (1927-2005): {result['IS_R2_head_1927']}%")
            print(f"  IS R² (OOS period): {result['IS_R2_head_OOS']}%")
            print(f"  IS R² (1965-2005): {result['IS_R2_head_1965']}%")
            print(f"  OOS R²: {result['OOS_oR2']}%")
            print(f"  dRMSE: {result['dRMSE']}%")
            print(f"  MSE-F: {result['MSEf']}")

            if plot and SAVE_PLOTS:
                plt.savefig(
                    OUTPUT_DIR / f'annual_{var}.{PLOT_FORMAT}',
                    dpi=PLOT_DPI,
                    bbox_inches='tight'
                )
        except Exception as e:
            print(f"  Error analyzing {var}: {str(e)}")

    # Save results to CSV
    if results:
        df_results = pd.DataFrame.from_dict(results, orient='index')
        output_file = OUTPUT_DIR / 'annual_results.csv'
        df_results.to_csv(output_file)
        print(f"\nResults saved to: {output_file}")

    if plot:
        plt.show()

    return results


def run_monthly_analysis(variables=None, plot=False):
    """
    Run analysis on monthly data

    Parameters:
    -----------
    variables : list, optional
        List of independent variables to analyze
    plot : bool
        Whether to generate plots
    """
    print("\n" + "="*60)
    print("Monthly Data Analysis")
    print("="*60)

    # Load data
    data_monthly = load_monthly_data()
    print(f"\nData loaded: {len(data_monthly)} observations")
    print(f"Period: {data_monthly.index.min()} - {data_monthly.index.max()}")

    # Summary statistics
    summary = get_data_summary(data_monthly, 'monthly')
    print(f"\nEquity Premium Statistics:")
    print(f"  Mean: {summary['equity_premium_mean']:.4f}")
    print(f"  Std:  {summary['equity_premium_std']:.4f}")
    print(f"  Min:  {summary['equity_premium_min']:.4f}")
    print(f"  Max:  {summary['equity_premium_max']:.4f}")

    # Use default variables if none specified
    if variables is None:
        variables = MONTHLY_CONFIG['indep_vars']

    # Run analysis for each variable
    results = {}
    plot_mode = 'yes' if plot else 'no'

    for var in variables:
        if var not in data_monthly.columns:
            print(f"\nWarning: Variable '{var}' not found in data, skipping...")
            continue

        print(f"\n--- Analyzing variable: {var} ---")

        # Handle special cases
        if var in SPECIAL_VARS:
            if 'start_date' in SPECIAL_VARS[var]:
                start_date = SPECIAL_VARS[var]['start_date']
                end_date = SPECIAL_VARS[var]['end_date']
            else:
                start_date = MONTHLY_CONFIG['start_date']
                end_date = MONTHLY_CONFIG['end_date']
        else:
            start_date = MONTHLY_CONFIG['start_date']
            end_date = MONTHLY_CONFIG['end_date']

        try:
            result = get_monthly_statistics(
                data_monthly,
                indep=var,
                start=start_date,
                end=end_date,
                est_periods_OOS=MONTHLY_CONFIG['est_periods_oos'],
                plot=plot_mode
            )
            results[var] = result
            print(f"  IS R² (log): {result['IS_R2_head_log']}%")
            print(f"  IS R²: {result['IS_R2_head']}%")
            print(f"  IS R² (trunc): {result['IS_R2_head_trunc']}%")
            print(f"  OOS R²: {result['OOS_R2_head']}%")
            print(f"  Share truncated: {result['share_T']}%")
            print(f"  Share slope=0: {result['share_U']}%")
            print(f"  OOS R² (trunc): {result['OOS_R2_head_trunc']}%")
            print(f"  dRMSE: {result['dRMSE']}%")

            if plot and SAVE_PLOTS:
                plt.savefig(
                    OUTPUT_DIR / f'monthly_{var}.{PLOT_FORMAT}',
                    dpi=PLOT_DPI,
                    bbox_inches='tight'
                )
        except Exception as e:
            print(f"  Error analyzing {var}: {str(e)}")

    # Save results to CSV
    if results:
        df_results = pd.DataFrame.from_dict(results, orient='index')
        output_file = OUTPUT_DIR / 'monthly_results.csv'
        df_results.to_csv(output_file)
        print(f"\nResults saved to: {output_file}")

    if plot:
        plt.show()

    return results


def main():
    """Main function to handle command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Replicate Goyal & Welch (2008) equity premium prediction analysis'
    )
    parser.add_argument(
        '--mode',
        choices=['annual', 'monthly', 'all'],
        default='all',
        help='Analysis mode: annual, monthly, or all (default: all)'
    )
    parser.add_argument(
        '--variable',
        type=str,
        help='Specific variable to analyze (optional, analyzes all if not specified)'
    )
    parser.add_argument(
        '--plot',
        action='store_true',
        help='Generate plots for the analysis'
    )
    parser.add_argument(
        '--list-vars',
        action='store_true',
        help='List available variables and exit'
    )

    args = parser.parse_args()

    # List variables
    if args.list_vars:
        print("\nAvailable variables for annual data:")
        for var in ANNUAL_CONFIG['indep_vars']:
            print(f"  - {var}")
        print("\nAvailable variables for monthly data:")
        for var in MONTHLY_CONFIG['indep_vars']:
            print(f"  - {var}")
        sys.exit(0)

    # Setup
    setup_output_directory()

    # Determine variables to analyze
    variables = [args.variable] if args.variable else None

    # Run analysis
    try:
        if args.mode == 'annual':
            run_annual_analysis(variables=variables, plot=args.plot)
        elif args.mode == 'monthly':
            run_monthly_analysis(variables=variables, plot=args.plot)
        elif args.mode == 'all':
            run_annual_analysis(variables=variables, plot=args.plot)
            run_monthly_analysis(variables=variables, plot=args.plot)

        print("\n" + "="*60)
        print("Analysis completed successfully!")
        print("="*60)

    except Exception as e:
        print(f"\nError during analysis: {str(e)}", file=sys.stderr)
        sys.exit(1)


if __name__ == '__main__':
    main()
