# Rule-Based Detection Documentation
## AI-Driven Election Network Anomaly Detection System

### Rules:

1. **request_rate > 20** → High alert (possible DoS or automated traffic)
2. **port_diversity > 5** → Medium alert (possible network scanning)
3. **traffic_spike > 3** → High alert (unusual surge in packets)
4. **byte_spike > 3** → Medium alert (abnormal data transfer)

### Teaching Notes:

- Rules are interpretable and easy to understand for students
- Shows **threshold-based anomaly detection**
- Alerts are **human-readable** and directly map to features
- Serves as a foundation before introducing **AI-based detection**
- Explains **limitations**: static thresholds cannot detect unknown patterns
