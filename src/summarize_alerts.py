import pandas as pd

# Use path relative to project root
df = pd.read_csv('data/processed/final_alerts.csv')

summary = df.groupby('src_ip').agg({
    'alerts': lambda x: "; ".join(set(x)),
    'anomaly_label': lambda x: "; ".join(set(x)),
    'anomaly_score': 'max',
    'explanation': lambda x: "; ".join(set(x))
}).reset_index()

summary.to_csv('data/processed/final_alerts_summary.csv', index=False)
print(summary)
print("\nFinal alerts summary saved: data/processed/final_alerts_summary.csv\n")