<svg viewBox="0 0 1280 640" xmlns="http://www.w3.org/2000/svg">
  <!-- Background with gradient -->
  <defs>
    <linearGradient id="bgGradient" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#0d1117;stop-opacity:1" />
      <stop offset="50%" style="stop-color:#161b22;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#0d1117;stop-opacity:1" />
    </linearGradient>
    
    <linearGradient id="shieldGradient" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" style="stop-color:#58a6ff;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#1f6feb;stop-opacity:1" />
    </linearGradient>
    
    <linearGradient id="accentGradient" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#1f6feb;stop-opacity:0.8" />
      <stop offset="100%" style="stop-color:#58a6ff;stop-opacity:0.8" />
    </linearGradient>
    
    <filter id="glow">
      <feGaussianBlur stdDeviation="3" result="coloredBlur"/>
      <feMerge>
        <feMergeNode in="coloredBlur"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>
  
  <!-- Background -->
  <rect width="1280" height="640" fill="url(#bgGradient)"/>
  
  <!-- Decorative grid pattern -->
  <g opacity="0.03" stroke="#58a6ff" stroke-width="1">
    <line x1="0" y1="160" x2="1280" y2="160"/>
    <line x1="0" y1="320" x2="1280" y2="320"/>
    <line x1="0" y1="480" x2="1280" y2="480"/>
    <line x1="320" y1="0" x2="320" y2="640"/>
    <line x1="640" y1="0" x2="640" y2="640"/>
    <line x1="960" y1="0" x2="960" y2="640"/>
  </g>
  
  <!-- Decorative circuit patterns -->
  <g opacity="0.15" stroke="#58a6ff" stroke-width="2" fill="none">
    <circle cx="120" cy="120" r="50"/>
    <circle cx="1160" cy="520" r="70"/>
    <line x1="120" y1="120" x2="250" y2="200"/>
    <line x1="1160" y1="520" x2="1000" y2="450"/>
    <circle cx="250" cy="200" r="6" fill="#58a6ff"/>
    <circle cx="1000" cy="450" r="6" fill="#58a6ff"/>
    
    <!-- Additional decorative nodes -->
    <circle cx="200" cy="500" r="30" opacity="0.5"/>
    <circle cx="1100" cy="150" r="40" opacity="0.5"/>
  </g>
  
  <!-- Main content group -->
  <g transform="translate(640, 320)">
    
    <!-- Shield icon (left side) -->
    <g transform="translate(-320, 0)">
      <path d="M 0,-100 L 70,-65 L 70,45 Q 70,80 0,110 Q -70,80 -70,45 L -70,-65 Z" 
            fill="url(#shieldGradient)" 
            stroke="#58a6ff" 
            stroke-width="3"
            filter="url(#glow)"/>
      
      <!-- Inner shield design -->
      <path d="M 0,-85 L 55,-55 L 55,40 Q 55,65 0,90 Q -55,65 -55,40 L -55,-55 Z" 
            fill="none" 
            stroke="#c9d1d9" 
            stroke-width="2"
            opacity="0.3"/>
      
      <!-- Checkmark -->
      <path d="M -30,-5 L -10,20 L 35,-35" 
            stroke="#ffffff" 
            stroke-width="10" 
            stroke-linecap="round" 
            stroke-linejoin="round"
            fill="none"/>
      
      <!-- AI Circuit nodes on shield -->
      <circle cx="-35" cy="-40" r="5" fill="#ffffff" opacity="0.9"/>
      <circle cx="35" cy="-40" r="5" fill="#ffffff" opacity="0.9"/>
      <circle cx="-45" cy="15" r="5" fill="#ffffff" opacity="0.9"/>
      <circle cx="45" cy="15" r="5" fill="#ffffff" opacity="0.9"/>
      <circle cx="0" cy="50" r="5" fill="#ffffff" opacity="0.9"/>
      
      <!-- Connecting lines -->
      <line x1="-35" y1="-40" x2="0" y2="-5" stroke="#ffffff" stroke-width="2" opacity="0.4"/>
      <line x1="35" y1="-40" x2="0" y2="-5" stroke="#ffffff" stroke-width="2" opacity="0.4"/>
      <line x1="-45" y1="15" x2="0" y2="20" stroke="#ffffff" stroke-width="2" opacity="0.4"/>
      <line x1="45" y1="15" x2="0" y2="20" stroke="#ffffff" stroke-width="2" opacity="0.4"/>
      <line x1="0" y1="20" x2="0" y2="50" stroke="#ffffff" stroke-width="2" opacity="0.4"/>
    </g>
    
    <!-- Title Text -->
    <text x="0" y="-40" font-family="'Segoe UI', Arial, sans-serif" font-size="72" font-weight="700" 
          fill="#c9d1d9" text-anchor="middle" letter-spacing="2">
      ELECTION GUARD
    </text>
    
    <!-- AI Text with gradient -->
    <text x="0" y="40" font-family="'Segoe UI', Arial, sans-serif" font-size="90" font-weight="800" 
          fill="url(#accentGradient)" text-anchor="middle" letter-spacing="8">
      AI
    </text>
    
    <!-- Tagline -->
    <text x="0" y="100" font-family="'Segoe UI', Arial, sans-serif" font-size="24" font-weight="300"
          fill="#8b949e" text-anchor="middle" letter-spacing="1">
      Securing Democracy with Artificial Intelligence
    </text>
    
    <!-- Feature badges -->
    <g transform="translate(-200, 140)">
      <rect x="0" y="0" width="120" height="32" rx="16" fill="#1f6feb" opacity="0.2"/>
      <text x="60" y="21" font-family="'Segoe UI', Arial, sans-serif" font-size="14" 
            fill="#58a6ff" text-anchor="middle" font-weight="600">
        🔒 Secure
      </text>
    </g>
    
    <g transform="translate(-60, 140)">
      <rect x="0" y="0" width="120" height="32" rx="16" fill="#1f6feb" opacity="0.2"/>
      <text x="60" y="21" font-family="'Segoe UI', Arial, sans-serif" font-size="14" 
            fill="#58a6ff" text-anchor="middle" font-weight="600">
        🤖 AI-Powered
      </text>
    </g>
    
    <g transform="translate(80, 140)">
      <rect x="0" y="0" width="120" height="32" rx="16" fill="#1f6feb" opacity="0.2"/>
      <text x="60" y="21" font-family="'Segoe UI', Arial, sans-serif" font-size="14" 
            fill="#58a6ff" text-anchor="middle" font-weight="600">
        ✓ Verified
      </text>
    </g>
  </g>
  
  <!-- Corner decorations -->
  <g opacity="0.6">
    <!-- Top left corner -->
    <line x1="30" y1="30" x2="80" y2="30" stroke="#1f6feb" stroke-width="3"/>
    <line x1="30" y1="30" x2="30" y2="80" stroke="#1f6feb" stroke-width="3"/>
    
    <!-- Top right corner -->
    <line x1="1200" y1="30" x2="1250" y2="30" stroke="#1f6feb" stroke-width="3"/>
    <line x1="1250" y1="30" x2="1250" y2="80" stroke="#1f6feb" stroke-width="3"/>
    
    <!-- Bottom left corner -->
    <line x1="30" y1="560" x2="30" y2="610" stroke="#1f6feb" stroke-width="3"/>
    <line x1="30" y1="610" x2="80" y2="610" stroke="#1f6feb" stroke-width="3"/>
    
    <!-- Bottom right corner -->
    <line x1="1250" y1="560" x2="1250" y2="610" stroke="#1f6feb" stroke-width="3"/>
    <line x1="1200" y1="610" x2="1250" y2="610" stroke="#1f6feb" stroke-width="3"/>
  </g>
</svg>


# election-guard-ai
An AI-assisted network anomaly detection system designed to monitor and protect election infrastructure by identifying abnormal traffic patterns and potential cyber threats in real time.

### REPOSITORY STRUCTURE
```bash
election-guard-ai/
│
├── data/
│   ├── raw/
│   │   └── sample_logs.csv
│   ├── processed/
│   │   └── features.csv
│
├── src/
│   ├── __init__.py
│   │
│   ├── data_loader.py        # Load & preprocess logs
│   ├── feature_engineering.py# Extract security features
│   ├── rules_engine.py       # Baseline rule-based detection
│   ├── model.py              # AI anomaly detection (Isolation Forest)
│   ├── explain.py            # Human-readable explanations
│   └── app.py                # CLI / minimal interface
│
├── tests/
│   └── test_cases.md         # Normal vs attack scenarios
│
├── docs/
│   ├── problem.md            # Day 1 output
│   ├── architecture.md       # System design
│   ├── lesson_outline.md     # Teaching plan
│   └── impact.md             # Impact statement
│
├── demo/
│   └── demo_script.md        # 40-minute presentation flow
│
├── requirements.txt
├── README.md
└── LICENSE
```
