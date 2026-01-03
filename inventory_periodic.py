"""
Inventory Management - Periodic Review Policy (R, S)

This script implements periodic review inventory management policies
to calculate order-up-to levels for retail replenishment.
"""

import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt


def load_demand_data():
    """Load demand data from CSV."""
    df = pd.read_csv("data/df_periodic.csv", index_col=0)
    print(f"{len(df):,} items loaded")
    return df


def calculate_periodic_policy(demand_series, R=10, LD=2, k=1):
    """
    Calculate (R, S) periodic review policy parameters.

    Parameters:
    - demand_series: daily demand values
    - R: review period (days)
    - LD: lead time (days)
    - k: safety factor

    Returns:
    - S: order-up-to level
    """
    # Average daily demand
    D_day = math.ceil(demand_series.mean())

    # Standard deviation of daily demand
    sigma = demand_series.std()

    # Average demand during lead time + review period
    mu_ld = math.floor(D_day * (LD + R))

    # Standard deviation during lead time + review period
    sigma_ld = sigma * math.sqrt(LD + R)

    # Order-up-to level
    S = mu_ld + k * sigma_ld

    return {
        "daily_demand": D_day,
        "sigma": sigma,
        "mu_ld": mu_ld,
        "sigma_ld": sigma_ld,
        "S": S,
        "R": R,
        "LD": LD,
        "k": k,
    }


def calculate_continuous_policy(demand_series, LD=2, k=3):
    """
    Calculate (s, Q) continuous review policy parameters.

    Parameters:
    - demand_series: daily demand values
    - LD: lead time (days)
    - k: safety factor

    Returns:
    - s: reorder point
    - Q: order quantity
    """
    # Average daily demand
    D_day = math.ceil(demand_series.mean())

    # Standard deviation
    sigma = demand_series.std()

    # Order quantity (5 days of demand)
    Q = 5 * D_day

    # Average demand during lead time
    mu_ld = math.floor(D_day * LD)

    # Standard deviation during lead time
    sigma_ld = sigma * math.sqrt(LD)

    # Reorder point
    s = mu_ld + k * sigma_ld

    return {
        "daily_demand": D_day,
        "sigma": sigma,
        "mu_ld": mu_ld,
        "sigma_ld": sigma_ld,
        "s": s,
        "Q": Q,
        "LD": LD,
        "k": k,
    }


def analyze_sku(df, sku_index=4):
    """Analyze a specific SKU with both policies."""
    cols_date = [f"DAY {i}" for i in range(1, 366)]

    sku_id = df["ITEM ID"].unique()[sku_index]
    demand_values = df[df["ITEM ID"] == sku_id][cols_date].values.flatten()

    print("=" * 60)
    print(f"SKU ANALYSIS: {sku_id}")
    print("=" * 60)

    # Continuous policy (s, Q)
    continuous = calculate_continuous_policy(demand_values)
    print("\n--- Continuous Review Policy (s, Q) ---")
    print(f"Daily Demand: {continuous['daily_demand']} units")
    print(f"Standard Deviation: {continuous['sigma']:.2f}")
    print(f"Lead Time: {continuous['LD']} days")
    print(f"Safety Factor (k): {continuous['k']}")
    print(f"Average demand during LT: {continuous['mu_ld']} units")
    print(f"Std deviation during LT: {continuous['sigma_ld']:.2f} units")
    print(f"Reorder Point (s): {continuous['s']:.2f} units")
    print(f"Order Quantity (Q): {continuous['Q']} units")

    # Periodic policy (R, S)
    periodic = calculate_periodic_policy(demand_values)
    print("\n--- Periodic Review Policy (R, S) ---")
    print(f"Review Period (R): {periodic['R']} days")
    print(f"Lead Time: {periodic['LD']} days")
    print(f"Safety Factor (k): {periodic['k']}")
    print(f"Average demand during R+LT: {periodic['mu_ld']} units")
    print(f"Std deviation during R+LT: {periodic['sigma_ld']:.2f} units")
    print(f"Order-Up-To Level (S): {periodic['S']:.2f} units")

    return continuous, periodic


def compare_review_periods(demand_series, review_periods=[5, 7, 10, 14]):
    """Compare different review periods."""
    print("\n" + "=" * 60)
    print("REVIEW PERIOD COMPARISON")
    print("=" * 60)
    print(f"{'Review Period':<15} {'Order-Up-To (S)':<20}")
    print("-" * 35)

    for R in review_periods:
        result = calculate_periodic_policy(demand_series, R=R)
        print(f"{R} days{'':<9} {result['S']:.2f} units")


def main():
    """Main function for inventory policy analysis."""
    try:
        df = load_demand_data()

        # Analyze sample SKU
        continuous, periodic = analyze_sku(df, sku_index=4)

        # Compare review periods
        cols_date = [f"DAY {i}" for i in range(1, 366)]
        sku_id = df["ITEM ID"].unique()[4]
        demand_values = df[df["ITEM ID"] == sku_id][cols_date].values.flatten()
        compare_review_periods(demand_values)

    except FileNotFoundError:
        print("Data file not found. Running with sample data...")

        # Sample data for demonstration
        np.random.seed(42)
        sample_demand = np.random.poisson(lam=5, size=365)

        print("\n--- Sample Analysis with Generated Data ---")
        continuous = calculate_continuous_policy(sample_demand)
        periodic = calculate_periodic_policy(sample_demand)

        print(f"\nContinuous (s,Q): s={continuous['s']:.2f}, Q={continuous['Q']}")
        print(f"Periodic (R,S): R={periodic['R']}, S={periodic['S']:.2f}")


if __name__ == "__main__":
    main()
