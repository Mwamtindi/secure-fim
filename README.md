# 🔐 SecureFIM — File Integrity Monitoring Tool

[![SecureFIM Tests](https://github.com/Mwamtindi/secure-fim/actions/workflows/tests.yml/badge.svg)](https://github.com/Mwamtindi/secure-fim/actions/workflows/tests.yml)

**SecureFIM** is a Python-based **File Integrity Monitoring (FIM)** tool designed to detect unauthorized or unexpected changes to files.

The tool creates a trusted baseline using **SHA-256 cryptographic hashes** and compares the current state of a monitored directory against that baseline. It can identify **modified, newly created, and deleted files**, while recording security events and generating structured JSON reports.

SecureFIM demonstrates practical **defensive cybersecurity, security monitoring, cryptographic hashing, event logging, and security automation**.

---

## 🎯 Project Purpose

File integrity monitoring is an important defensive security technique used to identify changes to critical files that may indicate:

* Unauthorized modification
* Malware activity
* Configuration tampering
* Suspicious file creation
* Accidental deletion
* Potential security incidents

SecureFIM provides a lightweight command-line implementation of these concepts using Python.

---

## ✨ Features

* 🔐 **SHA-256 file hashing**
* 📋 **File integrity baseline creation**
* 🔎 **Modified file detection**
* 🆕 **New file detection**
* 🗑️ **Deleted file detection**
* 📝 **Security event logging**
* 📊 **JSON security reports**
* 👁️ **Continuous directory monitoring**
* 🛡️ **CLI input validation**
* 🧪 **Automated testing with pytest**
* ⚙️ **GitHub Actions CI**
* 🚨 **Real-time detection during monitoring**

---

## ⚙️ How It Works

```text
                 Target Directory
                        │
                        ▼
              Create SHA-256 Baseline
                        │
                        ▼
                Scan / Monitor Files
                        │
                        ▼
                Compare File Hashes
                        │
            ┌───────────┼───────────┐
            ▼           ▼           ▼
        MODIFIED       NEW       DELETED
            │           │           │
            └───────────┼───────────┘
                        ▼
               Security Event Log
                        │
                        ▼
                  JSON Report
```

### Workflow

1. **Baseline** — SecureFIM calculates SHA-256 hashes for files in the target directory.
2. **Scan** — The current file state is compared against the stored baseline.
3. **Detection** — Changes are classified as modified, new, or deleted files.
4. **Logging** — Detected security events are recorded in the application log.
5. **Reporting** — Scan results are written to a structured JSON report.
6. **Monitoring** — The directory can be continuously monitored for new changes.

---

## 🛠️ Technologies

| Technology         | Purpose                        |
| ------------------ | ------------------------------ |
| **Python 3**       | Core application               |
| **SHA-256**        | Cryptographic file hashing     |
| **JSON**           | Baselines and security reports |
| **Python Logging** | Security event logging         |
| **pytest**         | Automated testing              |
| **Git & GitHub**   | Version control                |
| **GitHub Actions** | Continuous Integration         |

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/Mwamtindi/secure-fim.git
cd secure-fim
```

### 2. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 3. Verify the CLI

```bash
python main.py --help
```

You should see the available commands:

```text
baseline
scan
monitor
```

---

# 📖 Usage

## 1. Create a Baseline

Create a test directory containing files you want to monitor.

Example:

```text
test_data/
├── important.txt
└── config.txt
```

Create the baseline:

```bash
python main.py baseline --directory test_data
```

Example output:

```text
[+] Baseline created for 2 files.
[+] Saved to: baseline.json
```

The baseline stores the SHA-256 hash of each monitored file.

---

## 2. Scan for File Changes

Run a one-time integrity scan:

```bash
python main.py scan --directory test_data
```

If files have changed, SecureFIM reports the differences.

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

This allows an analyst to quickly identify changes that occurred after the trusted baseline was created.

---

## 3. Continuous Monitoring

SecureFIM can continuously monitor a directory.

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

The monitoring interval must be **at least 1 second**.

Press:

```text
Ctrl+C
```

to stop monitoring.

---

# 📝 Security Event Logging

SecureFIM records detected integrity events in:

```text
logs/securefim.log
```

Example:

```text
2026-10-04 09:07:43,211 | WARNING | FILE_MODIFIED | important.txt
```

Supported security events include:

```text
FILE_MODIFIED
FILE_CREATED
FILE_DELETED
```

These events provide a basic audit trail that can be useful when investigating suspicious file activity.

---

# 📊 JSON Security Reports

One-time scans generate a structured JSON report:

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

The report provides both a **summary of detected changes** and the specific files affected.

---

# 🧪 Testing

SecureFIM includes automated tests covering the core integrity-monitoring functionality.

Run the test suite:

```bash
python -m pytest
```

Current tests cover:

* SHA-256 hashing
* Baseline creation
* Modified file detection
* New file detection
* Deleted file detection

Example:

```text
============================= test session starts =============================
collected 5 items

tests/test_securefim.py .....                                             [100%]

============================== 5 passed =======================================
```

---

# 🔄 Continuous Integration

SecureFIM uses **GitHub Actions** to automatically run the test suite whenever code is pushed to the `main` branch or a pull request is opened.

The CI workflow:

1. Checks out the repository
2. Sets up Python 3.13
3. Installs project dependencies
4. Runs the automated test suite

This helps ensure that changes do not introduce regressions.

**CI Status:** ✅ Passing

---

# 📁 Project Structure

```text
secure-fim/
│
├── .github/
│   └── workflows/
│       └── tests.yml
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
│
├── .gitignore
├── main.py
├── README.md
└── requirements.txt
```

Generated files such as:

```text
baseline.json
report.json
logs/securefim.log
test_data/
```

are excluded from version control where appropriate.

---

# 🛡️ Security Use Case

SecureFIM can be used as a lightweight defensive security tool for monitoring files that should remain unchanged.

For example, an administrator could establish a trusted baseline for a directory containing:

```text
configuration files
system scripts
application files
security policies
critical documents
```

If a file is unexpectedly modified, created, or deleted, SecureFIM can detect the change and record the event.

In a larger security environment, these events could eventually be forwarded to a **SIEM platform** for centralized monitoring and alerting.

---

# 🧠 Security Concepts Demonstrated

This project demonstrates practical knowledge of:

* File Integrity Monitoring (FIM)
* Cryptographic hashing
* SHA-256
* Baseline security
* File change detection
* Security event logging
* Continuous monitoring
* Security reporting
* Defensive security automation
* Command-line security tooling
* Automated security testing
* Continuous Integration (CI)

---

# 📚 What I Learned

Building SecureFIM provided practical experience with:

* Designing a Python security utility
* Using cryptographic hashes for integrity verification
* Building a command-line security application
* Detecting file system changes
* Implementing security event logging
* Generating machine-readable security reports
* Writing automated security tests
* Validating CLI input
* Using Git and GitHub for version control
* Implementing CI with GitHub Actions

---

# 🔮 Future Improvements

Potential future enhancements include:

* 📧 Email and webhook security alerts
* 🔔 Configurable alert thresholds
* 📂 File and directory exclusion patterns
* 🗄️ Persistent hash database
* 🪟 Windows Event Log integration
* 📈 Security monitoring dashboard
* 🔌 SIEM integration
* 🌐 REST API for security events
* 🔐 Digital signature verification

---

# 👨‍💻 Author

**Shabani Athuman Mwamtindi**

**BSc Computer Security and Forensics**

Cybersecurity-focused developer interested in **defensive security, security monitoring, digital forensics, security tooling, and practical cybersecurity automation**.

---

## ⭐ Project Goal

SecureFIM was built as a practical cybersecurity portfolio project to demonstrate how fundamental security concepts such as **cryptographic hashing, file integrity monitoring, logging, automated testing, and continuous integration** can be combined into a functional defensive security tool.
