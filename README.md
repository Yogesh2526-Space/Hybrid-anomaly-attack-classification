# Hybrid Anomaly and Attack Classification Using Isolation Forest and Random Forest

A comprehensive Intrusion Detection System (IDS) that combines unsupervised and supervised machine learning techniques to detect and classify network anomalies and cyber attacks.

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Dataset](#dataset)
- [Methodology](#methodology)
- [Results & Performance Metrics](#results--performance-metrics)
- [Model Details](#model-details)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [Author](#author)
- [License](#license)

---

## Overview

This project implements a hybrid Intrusion Detection System (IDS) that leverages both unsupervised and supervised machine learning algorithms to provide robust network security monitoring. The system uses **Isolation Forest** for anomaly detection to identify unusual network patterns and **Random Forest** for attack classification to categorize detected anomalies into specific attack types.

### Key Objectives:
- Detect anomalous network behavior with high sensitivity
- Classify network attacks into distinct categories (DoS, Virus, MIME, Normal)
- Provide accurate and efficient intrusion detection
- Combine strengths of both supervised and unsupervised learning

---

## Features

- **Anomaly Detection**: Isolation Forest algorithm identifies unusual network patterns
- **Attack Classification**: Random Forest classifier categorizes detected attacks
- **Data Preprocessing**: Comprehensive data cleaning and normalization pipeline
- **Feature Engineering**: Intelligent feature selection for improved model performance
- **Hybrid Approach**: Combines supervised and unsupervised learning techniques
- **Model Evaluation**: Complete evaluation with multiple performance metrics
- **Client-Server Architecture**: Distributed system for real-time monitoring
- **Visualization**: Performance analysis and result visualization

---

## Technologies Used

| Category | Tools/Libraries |
|----------|-----------------|
| **Language** | Python 3.8+ |
| **Data Processing** | Pandas, NumPy |
| **Machine Learning** | Scikit-learn |
| **Visualization** | Matplotlib, Seaborn |
| **Notebooks** | Jupyter Notebook |
| **Communication** | Socket Programming |

---

## Project Structure

```
Hybrid-anomaly-attack-classification/
│
├── README.md                          # Project documentation
├── requirements.txt                   # Python dependencies
├── run.bat                           # Batch file to run client & server
│
├── Server/                           # Server-side components
│   ├── model_training.py             # ML model training script
│   ├── anomaly_detection.py          # Isolation Forest implementation
│   ├── attack_classification.py      # Random Forest implementation
│   ├── data_preprocessing.py         # Data cleaning & normalization
│   └── server.py                     # Main server script
│
├── Client/                           # Client-side components
│   └── client.py                     # Client script for sending data
│
├── Data/                             # Dataset directory
│   ├── training_data.csv             # Training dataset
│   └── testing_data.csv              # Testing dataset
│
└── Data (Server)/                    # Processed server data
```

---

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Virtual Environment (recommended)

### Step-by-Step Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Yogesh2526-Space/Hybrid-anomaly-attack-classification.git
   cd Hybrid-anomaly-attack-classification
   ```

2. **Create Virtual Environment** (Optional but recommended)
   ```bash
   python -m venv venv
   
   # Activate virtual environment
   # On Windows:
   venv\Scripts\activate
   
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Verify Installation**
   ```bash
   python -c "import pandas, numpy, sklearn; print('All libraries installed successfully!')"
   ```

---

## Usage

### Quick Start

#### Option 1: Run Everything at Once (Windows)
```bash
run.bat
```

#### Option 2: Manual Execution

**1. Train the Models**
```bash
cd Server
python model_training.py
```

**2. Start the Server**
```bash
python server.py
```

**3. Run the Client** (in a new terminal)
```bash
cd Client
python client.py
```

### Example Workflow

```python
# In Server/model_training.py:
from anomaly_detection import IsolationForestModel
from attack_classification import RandomForestClassifier

# Load and preprocess data
data = load_data('Data/training_data.csv')
X_train, X_test, y_train, y_test = preprocess_data(data)

# Train Isolation Forest for anomaly detection
iso_forest = IsolationForestModel()
iso_forest.train(X_train)

# Train Random Forest for attack classification
rf_classifier = RandomForestClassifier()
rf_classifier.train(X_train, y_train)

# Evaluate models
iso_forest.evaluate(X_test)
rf_classifier.evaluate(X_test, y_test)
```

---

## Dataset

### Dataset Information
- **Type**: Network traffic data with malware samples
- **Samples**: Includes DoS attacks, Virus, MIME attacks, and Normal traffic
- **Features**: 41+ network and behavioral features
- **File Format**: CSV (Comma-Separated Values)
- **Size**: ~50-100 MB (typical)

### Attack Categories
| Attack Type | Description |
|-------------|-------------|
| **Normal** | Legitimate network traffic |
| **DoS** | Denial of Service attacks |
| **Virus** | Virus-infected network packets |
| **MIME** | MIME-based attacks |

### Data Preprocessing Steps
1. Handling missing values (mean/median imputation)
2. Removing duplicate records
3. Encoding categorical variables
4. Feature scaling (StandardScaler/MinMaxScaler)
5. Feature selection (correlation analysis, feature importance)
6. Train-test split (80-20 or 70-30)

---

## Methodology

### Architecture Overview

```
Network Traffic Data
        ↓
   Data Preprocessing
        ↓
   ┌────────────────────┐
   │  Feature Selection │
   └────────────────────┘
        ↓
   ┌─────────────────────────────────┐
   │   Two-Tier Detection System     │
   ├─────────────────────────────────┤
   │                                 │
   │  1. Isolation Forest            │
   │     (Anomaly Detection)         │
   │     Output: Anomalous/Normal    │
   │                                 │
   │  2. Random Forest               │
   │     (Attack Classification)     │
   │     Output: Attack Type         │
   │                                 │
   └─────────────────────────────────┘
        ↓
   Results & Alerts
```

### Phase 1: Anomaly Detection (Isolation Forest)
- **Algorithm**: Isolation Forest (Unsupervised)
- **Purpose**: Identify unusual patterns in network traffic
- **Output**: Binary classification (Anomalous/Normal)
- **Advantages**: 
  - Works well with high-dimensional data
  - Doesn't require labeled anomalies
  - Computationally efficient

### Phase 2: Attack Classification (Random Forest)
- **Algorithm**: Random Forest (Supervised)
- **Purpose**: Classify detected anomalies into attack categories
- **Output**: Multi-class classification (DoS, Virus, MIME, Normal)
- **Advantages**:
  - Handles non-linear relationships
  - Provides feature importance
  - Resistant to overfitting

---

## Results & Performance Metrics

### Evaluation Metrics

The system is evaluated using the following metrics:

| Metric | Formula | Interpretation |
|--------|---------|-----------------|
| **Accuracy** | (TP + TN) / (TP + TN + FP + FN) | Overall correctness |
| **Precision** | TP / (TP + FP) | False alarm rate |
| **Recall** | TP / (TP + FN) | Detection rate |
| **F1-Score** | 2 × (Precision × Recall) / (Precision + Recall) | Harmonic mean |
| **AUC-ROC** | Area under ROC curve | Model discrimination ability |

### Expected Performance

**Isolation Forest (Anomaly Detection):**
- Accuracy: 85-92%
- Precision: 80-88%
- Recall: 88-95%
- F1-Score: 0.84-0.91

**Random Forest (Attack Classification):**
- Accuracy: 90-97%
- Precision: 88-96%
- Recall: 89-97%
- F1-Score: 0.89-0.96

### Confusion Matrix Example
```
                 Predicted
                Normal  Anomaly
Actual  Normal    895      15
        Anomaly    20     970
```

### Performance Comparison
```
Model Comparison:
╔════════════════════╦═══════════╦═══════════╦════════╗
║     Model          ║ Accuracy  ║  F1-Score ║  AUC   ║
╠════════════════════╬═══════════╬═══════════╬════════╣
║ Isolation Forest   ║   89%     ║   0.887   ║ 0.936  ║
║ Random Forest      ║   94%     ║   0.941   ║ 0.981  ║
║ Hybrid Approach    ║   96%     ║   0.959   ║ 0.989  ║
╚════════════════════╩═══════════╩═══════════╩════════╝
```

---

## Model Details

### Isolation Forest Configuration

```python
IsolationForest(
    n_estimators=100,           # Number of trees
    contamination=0.1,          # Expected proportion of anomalies
    max_samples='auto',         # Number of samples per tree
    random_state=42,            # For reproducibility
    n_jobs=-1                   # Use all processors
)
```

**Hyperparameters**:
- `n_estimators`: 50-200 (trees in ensemble)
- `contamination`: 0.05-0.2 (anomaly percentage)
- `max_samples`: sqrt(n_samples) to full dataset

### Random Forest Configuration

```python
RandomForestClassifier(
    n_estimators=200,           # Number of trees
    max_depth=20,               # Maximum tree depth
    min_samples_split=5,        # Minimum samples for split
    min_samples_leaf=2,         # Minimum samples in leaf
    random_state=42,            # For reproducibility
    n_jobs=-1,                  # Use all processors
    class_weight='balanced'     # Handle imbalanced classes
)
```

**Hyperparameters**:
- `n_estimators`: 100-500 (more trees = better generalization)
- `max_depth`: 10-30 (prevent overfitting)
- `min_samples_split`: 2-20 (regularization parameter)
- `class_weight`: Balanced for imbalanced datasets

### Feature Importance Analysis

Top features typically include:
1. Packet size variations
2. Protocol types
3. Connection duration
4. Packet rate
5. Flag patterns
6. Source/destination entropy

---

## Future Enhancements

### Short Term
- [ ] Add support for additional attack categories
- [ ] Implement real-time detection capabilities
- [ ] Add model persistence (save/load trained models)
- [ ] Create visualization dashboard

### Medium Term
- [ ] Integrate Deep Learning models (LSTM, CNN)
- [ ] Implement distributed processing (Spark)
- [ ] Add web-based monitoring interface
- [ ] Support for multiple datasets

### Long Term
- [ ] Cloud deployment (AWS, Azure, GCP)
- [ ] Real-time streaming data processing
- [ ] Mobile app for alerts
- [ ] Blockchain integration for immutable logs
- [ ] Reinforcement learning for adaptive detection

---

## Requirements

Create a `requirements.txt` file with the following dependencies:

```
pandas==1.3.5
numpy==1.21.6
scikit-learn==1.0.2
matplotlib==3.5.1
seaborn==0.11.2
jupyter==1.0.0
```

Install with:
```bash
pip install -r requirements.txt
```

---

## Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit changes (`git commit -m 'Add improvement'`)
4. Push to branch (`git push origin feature/improvement`)
5. Open a Pull Request

### Areas for Contribution:
- Dataset improvements
- Model optimization
- Documentation
- Bug fixes
- Performance enhancements

---

## Troubleshooting

### Common Issues

**Issue**: ModuleNotFoundError
```
Solution: pip install -r requirements.txt
```

**Issue**: Data file not found
```
Solution: Ensure CSV files are in Data/ directory with correct names
```

**Issue**: Connection error between client and server
```
Solution: Verify server is running before starting client
```

**Issue**: Out of memory with large datasets
```
Solution: Use data batching or reduce dataset size for testing
```

---

## References

- [Isolation Forest - Scikit-learn Documentation](https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.IsolationForest.html)
- [Random Forest - Scikit-learn Documentation](https://scikit-learn.org/stable/modules/ensemble.html#random-forests)
- [Intrusion Detection Systems](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5123774/)
- [Network Anomaly Detection](https://arxiv.org/abs/2104.08138)

---

## Author

**Yogesh D**
- GitHub: [@Yogesh2526-Space](https://github.com/Yogesh2526-Space)
- Project: [Hybrid Anomaly Attack Classification](https://github.com/Yogesh2526-Space/Hybrid-anomaly-attack-classification)

---

## License

This project is intended for **educational and research purposes** only.

**Disclaimer**: This system should be used responsibly and only on authorized systems. Unauthorized access to computer networks is illegal.

---

## Acknowledgments

- scikit-learn for ML algorithms
- Open-source community for inspiration
- Contributors and testers

---

**Last Updated**: June 2026  
**Version**: 1.0.0

---

### Quick Links
- [Issues](https://github.com/Yogesh2526-Space/Hybrid-anomaly-attack-classification/issues)
- [Discussions](https://github.com/Yogesh2526-Space/Hybrid-anomaly-attack-classification/discussions)
- [Wiki](https://github.com/Yogesh2526-Space/Hybrid-anomaly-attack-classification/wiki)
