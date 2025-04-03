import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

from scipy.stats import normaltest, kstest, anderson
def detect_outliers_iqr(series: pd.Series, multiplier: float = 1.5) -> pd.Series:
    """
    Detects outliers in a pandas Series using the IQR method.
    
    Args:
        series (pd.Series): The numeric Series to analyze.
        multiplier (float): The IQR multiplier to flag outliers (default: 1.5).
    
    Returns:
        pd.Series: A boolean Series where True indicates an outlier.
    """
    # Calculate Q1, Q3, and IQR
    Q1 = series.quantile(0.25)
    Q3 = series.quantile(0.75)
    IQR = Q3 - Q1
    
    # Define bounds
    lower_bound = Q1 - multiplier * IQR
    upper_bound = Q3 + multiplier * IQR
    
    # Return boolean series indicating which entries are outliers
    return (series < lower_bound) | (series > upper_bound)


def plot_boxplot_with_outliers(series: pd.Series, title: str = "Box Plot with IQR Outliers"):
    """
    Displays a box plot with outliers highlighted based on IQR.
    """
    plt.figure(figsize=(8, 5))
    sns.boxplot(x=series)
    plt.title(title)
    plt.xlabel(series.name)
    plt.show()

def check_normality(series):
    """
    Check normality of a data series.
    """
    series = series.dropna()  

    # D’Agostino’s K-squared Test
    normaltest_result = normaltest(series)
    print(f"D’Agostino’s K-squared Test: Statistic = {normaltest_result.statistic:.4f}, p-value = {normaltest_result.pvalue:.4f}")
    
    # Kolmogorov-Smirnov Test (Compares distribution with a standard normal distribution)
    ks_result = kstest((series - series.mean()) / series.std(), 'norm')
    print(f"Kolmogorov-Smirnov Test: Statistic = {ks_result.statistic:.4f}, p-value = {ks_result.pvalue:.4f}")
    
    # Anderson-Darling Test (Gives critical values instead of p-value)
    anderson_result = anderson(series)
    print(f"Anderson-Darling Test: Statistic = {anderson_result.statistic:.4f}")
    for i, (cv, sig_level) in enumerate(zip(anderson_result.critical_values, anderson_result.significance_level)):
        print(f"  Significance level: {sig_level}% | Critical value: {cv}")
    
    if normaltest_result.pvalue < 0.05 or ks_result.pvalue < 0.05:
        print("\n❌ Data is likely NOT normally distributed.")
    else:
        print("\n✅ Data is likely normally distributed.")


