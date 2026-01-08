# Feature Engineering Documentation
## AI-Driven Election Network Anomaly Detection System

### 1. request_rate
**Definition:** Number of requests per source IP per minute.  
**Purpose:** Detects traffic surges that may indicate DoS or automated attacks.

### 2. port_diversity
**Definition:** Number of distinct destination ports accessed by a source IP.  
**Purpose:** High port diversity can indicate network scanning or probing attempts.

### 3. traffic_spike
**Definition:** Ratio of current packet_count to average packet_count per IP.  
**Purpose:** Highlights unusual spikes in activity relative to baseline behavior.

### 4. byte_spike
**Definition:** Ratio of current byte_count to average byte_count per IP.  
**Purpose:** Detects abnormal data transfers or sudden large payloads.

### Notes:
- Features are calculated per source IP per time window (1 minute).  
- These features are designed to be explainable and suitable for both **rule-based alerts** and **unsupervised AI detection**.  
- The `event_type` column in raw logs is only for testing; the AI model itself does **not use labels**.
