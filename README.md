
# Log Classification System

## Overview

This project is a comprehensive log classification system that uses multiple techniques to categorize log messages from different sources. It combines regex pattern matching, BERT embeddings with a trained classifier, and LLM-based classification to accurately label log entries.

## Features

- **Multi-technique classification**: Uses different classification methods based on the log source  
- **Regex-based classification**: Fast pattern matching for well-structured logs  
- **BERT-based classification**: Machine learning approach for more complex logs  
- **LLM-based classification**: Uses Groq's API with LLaMA 70B for ambiguous or complex logs from LegacyCRM  
- **CSV processing**: Can process entire CSV files with log data  
- **REST API**: FastAPI endpoint for easy integration  

## Components

### 1. Classification Pipeline (`classify.py`)

The main classification logic that routes logs to appropriate classifiers:
- LegacyCRM logs go to LLM classifier
- Other logs first try regex, then fall back to BERT if no match found

### 2. Classifiers

#### Regex Classifier (`processor_regex.py`)
- Uses predefined patterns to match common log formats  
- Fast and deterministic  
- Returns None if no pattern matches  

#### BERT Classifier (`processor_bert.py`)
- Uses SentenceTransformer embeddings  
- Pre-trained classifier loaded from joblib file  
- Returns "Unclassified" if confidence is low (<0.5)  

#### LLM Classifier (`processor_llm.py`)
- Uses Groq API with DeepSeek R1 model  
- Strictly categorizes into 3 classes for LegacyCRM logs  
- Uses XML-style tags for structured output  

### 3. REST API (`server.py`)
- FastAPI endpoint for CSV processing  
- Validates input and returns classified CSV  
- Handles errors gracefully  

## Setup Instructions

### Prerequisites

- Python 3.8+  
- pip  

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   - Create a `.env` file in the root directory  
   - Add your Groq API key:
     ```
     GROQ_API_KEY=your_api_key_here
     ```

### Required Files

Ensure you have these files in place:
- `models/log_classifier.joblib` - Pre-trained classifier model  
- `resources/` directory for input/output files  

## Usage

### 1. Command Line

To classify a CSV file:
```bash
python classify.py resources/test.csv
```

### 2. Programmatic Usage

```python
from classify import classify

logs = [
    ("ModernCRM", "User User123 logged in."),
    ("LegacyCRM", "Case escalation failed for ticket ID 123")
]

classified_logs = classify(logs)
print(classified_logs)
```

### 3. REST API

Start the server:
```bash
uvicorn server:app --reload
```

Send a POST request with a CSV file:
```bash
curl -X POST -F "file=@path/to/your/file.csv" http://localhost:8000/classify/ --output output.csv
```

## File Structure

```
.
├── classify.py               # Main classification logic
├── processor_bert.py         # BERT-based classifier
├── processor_llm.py          # LLM-based classifier
├── processor_regex.py        # Regex-based classifier
├── server.py                 # FastAPI server
├── requirements.txt          # Dependencies
├── models/                   # Contains trained models
│   └── log_classifier.joblib
└── resources/                # Input/output files
    ├── input.csv
    └── output.csv
```

## Testing

The modules include test cases in their `__main__` blocks. You can run them directly to verify functionality:

```bash
python processor_regex.py
python processor_bert.py
python processor_llm.py
```

## Performance Considerations

- **Regex** is fastest - use for predictable log formats  
- **BERT** is medium speed - good fallback for unstructured logs  
- **LLM** is slowest - reserved for LegacyCRM logs only  

## Limitations

- LLM classifier requires API key and internet connection  
- BERT classifier needs pre-trained model file  
- Regex patterns need to be maintained as log formats change  

## Future Improvements

- Add more regex patterns for common log formats  
- Implement caching for LLM responses  
- Add batch processing for BERT embeddings  
- Support for other classifier models  

## License

[MIT License] - Feel free to use and modify for your needs.
