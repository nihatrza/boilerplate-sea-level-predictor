import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    # 2. Scatter plot yaradırıq (x: Year, y: CSIRO Adjusted Sea Level)
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', alpha=0.7)

    # 3. Birinci 'Line of Best Fit' (1880-dən 2050-yə qədər)
    res_all = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_pred1 = pd.Series(range(1880, 2051))
    y_pred1 = res_all.slope * x_pred1 + res_all.intercept
    ax.plot(x_pred1, y_pred1, color='red', label='1880-2050 Trend')

    # 4. İkinci 'Line of Best Fit' (2000-ci ildən 2050-yə qədər)
    df_recent = df[df['Year'] >= 2000]
    res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    x_pred2 = pd.Series(range(2000, 2051))
    y_pred2 = res_recent.slope * x_pred2 + res_recent.intercept
    ax.plot(x_pred2, y_pred2, color='green', label='2000-2050 Trend')

    # 5. Başlıq və oxların adlarını təyin edirik
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()