# Freaking-Template-Language-FTL
A Declarative DSL for generating dilosi.gov.gr digital service templates

# FTL – Setup & Quickstart

## Prerequisites
- **Git**
- **Python 3.8+** and **pip**
- (Optional) **VS Code** for best editing experience

## 1) Clone the repository
```bash
git clone https://github.com/ETsagkaris/Freaking-Template-Language-FTL.git
cd Freaking-Template-Language-FTL
```

## 2) Create and activate a virtual environment

**macOS / Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

**Windows (PowerShell)**

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
```

## 3) Install textx

```bash
pip install textX
```

## 4) VSCode extension
There is an ftl-ext extension packed in this repo, simple open the repo in VSCode and run debug mode (F5) to test the extension

## 5) Run examples
Call ftl/dsl.py function and provide a .ftl file
```bash
python ftl/dsl.py ftl/samples/test.ftl
```

Θέλεις να σου ετοιμάσω και το `requirements.txt` (με τουλάχιστον το `textX`) για να το βάλεις μαζί στο repo;
```
