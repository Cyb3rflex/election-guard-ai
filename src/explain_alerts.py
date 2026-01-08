from pathlib import Path
import pandas as pd

def load_alerts(repo_root):
    """Load rule-based and AI-based alerts CSVs"""
    rule_alerts_file = repo_root / 'data' / 'processed' / 'rule_alerts.csv'
    ai_alerts_file = repo_root / 'data' / 'processed' / 'ai_alerts.csv'

    rule_alerts = pd.read_csv(rule_alerts_file)
    ai_alerts = pd.read_csv(ai_alerts_file)
    return rule_alerts, ai_alerts

def explain_row(row):
    """Generate human-readable explanation for a row"""
    reasons = []

    if row.get('high_request_rate', 0) == 1:
        reasons.append("Unusually high request rate detected")

    if row.get('high_port_diversity', 0) == 1:
        reasons.append("Access to multiple ports in short time window")

    if row.get('traffic_spike', 1) > 3:
        reasons.append("Sudden spike in network traffic")

    if row.get('byte_spike', 1) > 3:
        reasons.append("Abnormal increase in data volume")

    if row.get('anomaly_label') == 'anomaly':
        reasons.append("AI model identified unusual behavior pattern")

    if not reasons:
        reasons.append("Normal network behavior")

    return "; ".join(reasons)

def merge_and_explain(rule_df, ai_df):
    """Merge rule and AI alerts and generate explanations"""
    merged = pd.merge(
        rule_df,
        ai_df[['src_ip', 'anomaly_label', 'anomaly_score']],
        on='src_ip',
        how='left'
    )

    merged['explanation'] = merged.apply(explain_row, axis=1)
    return merged

if __name__ == "__main__":
    # Resolve repo root relative to this script
    repo_root = Path(__file__).parent.parent

    rule_df, ai_df = load_alerts(repo_root)
    final_alerts = merge_and_explain(rule_df, ai_df)

    final_file = repo_root / 'data' / 'processed' / 'final_alerts.csv'
    final_alerts.to_csv(final_file, index=False)

    print(f"\nFinal explained alerts saved: {final_file}\n")
    print("\n=== EXPLAINED SECURITY ALERTS ===\n")
    for _, row in final_alerts.iterrows():
        print(f"[{row['src_ip']}] → {row['explanation']}")
