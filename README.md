# SecureFIM — File Integrity Monitoring Tool

SecureFIM is a Python-based **File Integrity Monitoring (FIM)** tool that uses SHA-256 cryptographic hashing to detect unauthorized or unexpected changes to files.

It creates a trusted baseline of a directory and continuously compares the current file state against that baseline to identify modified, newly created, or deleted files.

## Features

* 🔐 SHA-256 file hashing
* 📋 File integrity baseline creation
* 🔎 Modified file detection
* 🆕 New file detection
* 🗑️ Deleted file detection
* 📝 Security event logging
* 📊 JSON security reports
* 👁️ Continuous directory monitoring
* 🛡️ CLI input validation
* 🧪 Automated tests with pytest

## How It Works

```text
Target Directory
       │
       ▼
Create SHA-256 Baseline
       │
       ▼
Monitor / Scan Directory
       │
       ▼
Compare File Hashes
       │
       ├── Modified
       ├── New
       └── Deleted
              │
              ▼
       Security Event Log
              │
              ▼
          JSON Report
```

## Technologies

* **Python 3**
* **SHA-256**
* **JSON**
* **Python Logging**
* **pytest**
* **Git / GitHub**

## Installation

Clone the repository:

```bash
git clone https://github.com/Mwamtindi/secure-fim.git
cd secure-fim
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```
Note: For testing, create a directory containing files before creating a baseline.

## Usage

### 1. Create a baseline

Create a trusted baseline for a directory:

```bash
python main.py baseline --directory test_data
```

Example:

```text
[+] Baseline created for 2 files.
[+] Saved to: baseline.json
```

The baseline stores SHA-256 hashes for the files being monitored.

### 2. Scan for changes

Run a one-time integrity scan:

```bash
python main.py scan --directory test_data
```

Example:

```text
=== SecureFIM Scan Results ===

[MODIFIED] 1
  - important.txt

[NEW] 1
  - suspicious.txt

[DELETED] 1
  - config.txt

[+] Report saved to: report.json
```

### 3. Continuous monitoring

Monitor a directory continuously:

```bash
python main.py monitor --directory test_data --interval 5
```

Example:

```text
[+] Monitoring: test_data
[+] Scan interval: 5 seconds
[+] Press Ctrl+C to stop.

[!] File integrity changes detected!
[MODIFIED] important.txt

[!] File integrity changes detected!
[NEW] suspicious.exe

[!] File integrity changes detected!
[DELETED] suspicious.exe
```

The monitoring interval must be at least 1 second.

## Security Logging

SecureFIM records detected integrity events in:

```text
logs/securefim.log
```

Example:

```text
2026-10-04 09:07:43,211 | WARNING | FILE_MODIFIED | important.txt
```

Supported security events include:

* `FILE_MODIFIED`
* `FILE_CREATED`
* `FILE_DELETED`

## JSON Reports

Scan results are also saved as:

```text
report.json
```

Example:

```json
{
    "scan_time": "2026-09-30T10:42:40",
    "directory": "test_data",
    "summary": {
        "modified": 1,
        "new": 1,
        "deleted": 1
    },
    "changes": {
        "modified": [
            "important.txt"
        ],
        "new": [
            "suspicious.txt"
        ],
        "deleted": [
            "config.txt"
        ]
    }
}
```

## Testing

SecureFIM includes automated tests covering its core integrity-monitoring functionality.

Run the test suite with:

```bash
python -m pytest
```

Current test coverage includes:

* SHA-256 hashing
* Baseline creation
* Modified file detection
* New file detection
* Deleted file detection

Example:

```text
======================= 5 passed =======================
```

## Project Structure

```text
secure-fim/
│
├── securefim/
│   ├── __init__.py
│   ├── baseline.py
│   ├── hasher.py
│   ├── monitor.py
│   └── reporter.py
│
├── tests/
│   └── test_securefim.py
│
├── logs/
├── .gitignore
├── main.py
├── README.md
└── requirements.txt
```

Generated files such as the baseline, logs, and reports are excluded from version control where appropriate.

## Security Concepts Demonstrated

SecureFIM demonstrates practical cybersecurity and defensive security concepts including:

* File Integrity Monitoring
* Cryptographic hashing
* SHA-256
* Change detection
* Security event logging
* Continuous monitoring
* Security reporting
* Defensive security automation
* Command-line security tooling
* Automated security testing

## Future Improvements

Potential future enhancements include:

* Email or webhook alerts
* Configurable monitoring rules
* File exclusion patterns
* Hash database support
* Windows Event Log integration
* Dashboard visualization
* SIEM integration

## Author

**Shabani Athuman Mwamtindi**

Cybersecurity & Computer Security and Forensics graduate focused on defensive security, security tooling, and practical cybersecurity automation.
