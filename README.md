# SINTINEL

> **Level up or log out.**

SINTINEL is an IT diagnostics and troubleshooting toolkit being developed by **InkyShaman**. Its goal is to give technicians a fast, reliable snapshot of a customer's computer by collecting system, hardware, and network information.

## 🛡️ Overview

SINTINEL is built in Python with a modular architecture so each diagnostic system can be developed and tested independently.

### Current diagnostic areas
- System information
- Hardware diagnostics
- Network diagnostics
- CPU information
- CPU cores and threads
- CPU usage
- RAM capacity and usage
- Storage capacity, used space, and free space
- Windows version and architecture
- GPU detection
- GPU VRAM detection

## 🚧 Current Status

**Version:** 0.1 — Early Development

### Working
- [x] Python project structure
- [x] Main application menu
- [x] System information module
- [x] Network diagnostics module
- [x] Hardware diagnostics module
- [x] CPU detection
- [x] RAM detection
- [x] Storage detection
- [x] Windows information
- [x] NVIDIA GPU detection
- [x] GPU VRAM reporting
- [x] Git/GitHub version control

### In Development
- [ ] AMD GPU driver-based detection
- [ ] Intel GPU driver-based detection
- [ ] Improved multi-GPU detection
- [ ] Hardware health checks
- [ ] Expanded network troubleshooting
- [ ] Diagnostic reports
- [ ] Logging
- [ ] Automated recommendations
- [ ] Technician-friendly reporting

## 🧠 Design Philosophy

> **Collect accurate information first. Diagnose second.**

Whenever possible, SINTINEL should retrieve hardware information from the operating system or vendor driver/interface rather than relying on hard-coded assumptions.

The GPU system is being designed around vendor/driver information so SINTINEL can eventually support NVIDIA, AMD, and Intel graphics accurately.

## 🧰 Technology

- Python 3
- `psutil`
- Windows system utilities
- GPU vendor driver utilities
- Git
- GitHub
- Visual Studio Code

## 📁 Project Structure

```text
SINTINEL/
├── .gitignore
├── src/
│   ├── main.py
│   ├── system_info.py
│   ├── network_info.py
│   └── hardware_info.py
└── README.md
```

### Module Responsibilities

**`main.py`** — Controls the application menu and connects the diagnostic modules.

**`system_info.py`** — Collects operating-system and system-level information.

**`network_info.py`** — Handles network diagnostics and connectivity information.

**`hardware_info.py`** — Collects CPU, RAM, storage, and GPU information.

## 💻 Installation

Clone the repository:

```bash
git clone https://github.com/izzy120/InkyShaman-IT-Toolkit.git
cd InkyShaman-IT-Toolkit
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it in Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
pip install psutil
```

## ▶️ Running SINTINEL

From the project root:

```powershell
python src/main.py
```

Example menu:

```text
SINTINEL IT TOOLKIT

1. System Information
2. Network Diagnostics
3. Hardware Diagnostics
4. Exit
```

## 🔬 Development Roadmap

### Phase 1 — Foundation
- [x] Python project
- [x] Main menu
- [x] Modular diagnostic files
- [x] Git version control
- [x] GitHub repository

### Phase 2 — Hardware Intelligence
- [x] CPU information
- [x] RAM information
- [x] Storage information
- [x] Windows information
- [x] NVIDIA GPU detection
- [x] NVIDIA VRAM detection
- [ ] AMD driver detection
- [ ] Intel driver detection
- [ ] Multi-GPU support

### Phase 3 — Network Diagnostics
- [x] Basic network information
- [ ] Connectivity testing
- [ ] Ping diagnostics
- [ ] DNS diagnostics
- [ ] Gateway detection
- [ ] Network adapter information
- [ ] Bandwidth/utilization information

### Phase 4 — Technician Tools
- [ ] Diagnostic scan
- [ ] Hardware health status
- [ ] Hardware warnings
- [ ] System report generation
- [ ] Report export
- [ ] Logging
- [ ] Error reporting

### Phase 5 — SINTINEL Intelligence
- [ ] Automated troubleshooting recommendations
- [ ] Common-problem detection
- [ ] Corrective-action recommendations
- [ ] Technician mode
- [ ] Customer-friendly reports
- [ ] Advanced hardware analysis

### Phase 6 — Production
- [ ] Graphical interface
- [ ] Installer/package
- [ ] Portable technician version
- [ ] Configuration system
- [ ] Automated updates
- [ ] Full documentation

## 🎯 Long-Term Goal

SINTINEL is intended to become a professional IT diagnostic platform for computer repair, troubleshooting, optimization, and customer support.

The goal is simple: instead of opening multiple Windows utilities and manually collecting information, a technician should eventually be able to launch SINTINEL and receive a clear diagnostic report.

The long-term vision is for SINTINEL to become a core tool in the **InkyShaman IT workflow**.

## 🧑‍💻 Project

**Developer:** InkyShaman  
**Project:** SINTINEL  
**Purpose:** IT diagnostics, troubleshooting, and system information  
**Status:** Active development

## 📜 License

License information will be added as the project approaches its first public release.

## ⚡ Motto

> **LEVEL UP OR LOG OUT.**
