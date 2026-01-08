from pathlib import Path
import pandas as pd

def load_raw_logs(file_path: Path) -> pd.DataFrame:
    """Load raw network logs CSV"""
    return pd.read_csv(file_path, parse_dates=['timestamp'])

def generate_features(df: pd.DataFrame) -> pd.DataFrame:
    """Generate numerical features for anomaly detection"""
    # Request rate per src_ip (requests per minute)
    df['minute'] = df['timestamp'].dt.floor('T')
    req_rate = df.groupby(['src_ip', 'minute']).size().reset_index(name='request_rate')
    df = df.merge(req_rate, on=['src_ip', 'minute'], how='left')
    
    # Port diversity per src_ip (number of distinct dest_ports)
    df['port_diversity'] = df.groupby('src_ip')['dest_port'].transform('nunique')
    
    # Traffic spike (current packet_count / average packet_count per IP)
    avg_packet = df.groupby('src_ip')['packet_count'].transform('mean')
    df['traffic_spike'] = df['packet_count'] / (avg_packet + 1e-5)
    
    # Byte count spike (current byte_count / average byte_count per IP)
    avg_bytes = df.groupby('src_ip')['byte_count'].transform('mean')
    df['byte_spike'] = df['byte_count'] / (avg_bytes + 1e-5)
    
    # Drop columns not needed for model
    df_features = df[['src_ip', 'request_rate', 'port_diversity', 'traffic_spike', 'byte_spike']]
    
    return df_features

if __name__ == "__main__":
    # Safe path resolution
    repo_root = Path(__file__).parent.parent
    file_path = repo_root / 'data' / 'raw' / 'sample_logs.csv'
    df_raw = load_raw_logs(file_path)
    df_features = generate_features(df_raw)
    
    # Save features
    processed_dir = repo_root / 'data' / 'processed'
    processed_dir.mkdir(exist_ok=True)
    df_features.to_csv(processed_dir / 'features.csv', index=False)
    
    print(f"Feature file saved: {processed_dir / 'features.csv'}")
