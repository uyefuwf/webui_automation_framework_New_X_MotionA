# SauceDemo Web UI Automation Framework

A simple, readable, and robust test automation framework for [SauceDemo](https://www.saucedemo.com) built with **Python**, **pytest**, and **Playwright** using the **Page Object Model (POM)** design pattern.

---

## 📁 Project Structure

```text
├── Basepage/
│   └── basepage.py             # Common Playwright wrapper methods (click, fill, get_text, etc.)
├── page/
│   ├── loginpage.py            # Login page locators and user actions
│   ├── inventorypage.py        # Product catalog, sorting, cart badges, and menu actions
│   ├── cartpage.py             # Cart items inspection and checkout navigation
│   └── checkoutpage.py         # Customer information and order completion steps
├── tests/
│   ├── test_login.py           # Login, locked-out user, and logout test cases
│   ├── test_inventory_and_cart.py # Cart badge, multi-item verification, and price sorting
│   └── test_checkout.py        # End-to-end checkout flow test
├── conftest.py                 # Global pytest fixtures providing page instances
├── pytest.ini                  # Pytest configuration, CLI arguments, and markers
├── requirements.txt            # Python dependencies
└── report/
    └── report.html             # Generated HTML test execution report
```

---

## 🚀 Tech Stack

- **Python 3.10+**
- **Playwright** (`playwright` & `pytest-playwright`) - Modern, fast browser automation engine
- **pytest** - Test runner, assertions, and fixture management
- **pytest-html** - HTML test execution reports

---

## ⚙️ Setup & Installation

### 1. Clone the repository and navigate to the project directory:
```bash
git clone <repo-url>
cd NewEdge_MotioA
```

### 2. Create and activate a virtual environment:
```bash
python3 -m venv .venv
source .venv/bin/activate    # On Windows: .venv\Scripts\activate
```

### 3. Install dependencies:
```bash
pip install -r requirements.txt
```

### 4. Install Playwright browser binaries:
```bash
playwright install
```

---

## 🧪 Test Scenarios Covered

| # | Scenario | File | Markers |
|---|---|---|---|
| **1** | Valid login with `standard_user` | `tests/test_login.py` | `smoke`, `func` |
| **2** | Invalid login with incorrect password | `tests/test_login.py` | `negative` |
| **3** | Locked-out user (`locked_out_user`) error validation | `tests/test_login.py` | `negative` |
| **4** | Add single product to cart & verify badge count | `tests/test_inventory_and_cart.py` | `smoke` |
| **5** | Add multiple products, open cart, verify items & quantities | `tests/test_inventory_and_cart.py` | `func` |
| **6** | Complete full checkout flow (cart -> info -> overview -> finish) | `tests/test_checkout.py` | `smoke`, `func` |
| **7** | Sort products (Price low to high) and verify ordering | `tests/test_inventory_and_cart.py` | `func` |
| **8** | Logout from inventory and verify returned to login page | `tests/test_login.py` | `smoke` |

---

## ▶️ Running Tests

### Run all tests (headless by default):
```bash
pytest
```

### Run in headed mode (visible browser window):
```bash
pytest --headed
```

### Run specific test suites:
```bash
# Run only login tests
pytest tests/test_login.py

# Run only inventory & cart tests
pytest tests/test_inventory_and_cart.py

# Run only checkout tests
pytest tests/test_checkout.py
```

### Run by markers:
```bash
# Run smoke tests
pytest -m smoke

# Run negative tests
pytest -m negative

# Run functional tests
pytest -m func
```

### Run on different browsers:
```bash
pytest --browser chromium
pytest --browser firefox
pytest --browser webkit
```

---

## 📊 Reports & Tracing

- **HTML Report**: Automatically saved to [`report/report.html`](report/report.html) after each run. Open it in any browser:
  ```bash
  # Linux
  xdg-open report/report.html
  # macOS
  open report/report.html
  ```

- **Playwright Traces**: Tracing is enabled in `pytest.ini`. You can view interactive traces and step-by-step DOM snapshots with:
  ```bash
  playwright show-trace test-results/<folder_name>/trace.zip
  ```
