from pathlib import Path
import pandas as pd

def load_features(file_path):
    """Load processed features CSV"""
    return pd.read_csv(file_path)

def apply_rules(df):
    """Apply rule-based anomaly detection"""
    alerts = []

    for idx, row in df.iterrows():
        alert_msgs = []

        if row['request_rate'] > 2:
            alert_msgs.append(f"High request rate ({row['request_rate']})")

        if row['port_diversity'] > 1:
            alert_msgs.append(f"High port diversity ({row['port_diversity']})")

        if row['traffic_spike'] > 1.2:
            alert_msgs.append(f"Traffic spike ({row['traffic_spike']:.2f}×)")

        if row['byte_spike'] > 1.2:
            alert_msgs.append(f"Byte spike ({row['byte_spike']:.2f}×)")

        if alert_msgs:
            alerts.append({
                'src_ip': row['src_ip'],
                'alerts': "; ".join(alert_msgs)
            })

    return pd.DataFrame(alerts)

if __name__ == "__main__":
    # Correct paths relative to script location
    repo_root = Path(__file__).parent.parent
    features_file = repo_root / 'data' / 'processed' / 'features.csv'
    alerts_file = repo_root / 'data' / 'processed' / 'rule_alerts.csv'

    df_features = load_features(features_file)
    df_alerts = apply_rules(df_features)

    df_alerts.to_csv(alerts_file, index=False)
    print(f"Rule-based alerts saved: {alerts_file}")
    print(df_alerts)
