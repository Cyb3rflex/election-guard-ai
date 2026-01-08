from pathlib import Path
import pandas as pd
from sklearn.ensemble import IsolationForest

def load_features(file_path):
    """Load features CSV"""
    return pd.read_csv(file_path)

def train_isolation_forest(df_features):
    """Train Isolation Forest on features"""
    # Use numerical columns only
    X = df_features[['request_rate', 'port_diversity', 'traffic_spike', 'byte_spike']]
    
    model = IsolationForest(n_estimators=100, contamination=0.1, random_state=42)
    model.fit(X)
    
    # Predict anomalies: -1 = anomaly, 1 = normal
    df_features['anomaly'] = model.predict(X)
    
    # Calculate anomaly score for teaching
    df_features['anomaly_score'] = model.decision_function(X) * -1  # higher = more anomalous
    
    return df_features, model

if __name__ == "__main__":
    # Resolve paths relative to this script
    repo_root = Path(__file__).parent.parent
    features_file = repo_root / 'data' / 'processed' / 'features.csv'
    ai_alerts_file = repo_root / 'data' / 'processed' / 'ai_alerts.csv'
    
    df_features = load_features(features_file)
    df_anomaly, model = train_isolation_forest(df_features)
    
    # Map anomaly labels to human-readable
    df_anomaly['anomaly_label'] = df_anomaly['anomaly'].apply(lambda x: 'anomaly' if x == -1 else 'normal')
    
    # Save results
    df_anomaly.to_csv(ai_alerts_file, index=False)
    print(f"AI-based alerts saved: {ai_alerts_file}")
    print(df_anomaly[['src_ip', 'request_rate', 'port_diversity', 'traffic_spike', 'byte_spike', 'anomaly_label']])
