# Playwright E-Commerce Framework

Automation Framework built with Python, Pytest and Playwright following QA Automation best practices.

## Tech Stack

- Python
- Pytest
- Playwright
- Page Object Model (POM)
- GitHub Actions
- Data Driven Testing (JSON)
- HTML Reports
- Automatic Screenshots on Failure

---

## Framework Architecture

```text
playwright-ecommerce-framework

├── .github/
│ └── workflows/
│ └── playwright-tests.yml

├── data/
├── fixtures/
├── pages/
├── reports/
├── screenshots/
├── tests/
├── utils/

├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## Implemented Features

### Authentication

- Valid Login
- Locked User Login Validation

### Inventory

- Product Count Validation

### Cart

- Add Product To Cart

### Checkout

- Complete End-to-End Purchase Flow

---

## Test Coverage

| Test | Status |
|--------|--------|
| Login | ✅ |
| Negative Login | ✅ |
| Inventory | ✅ |
| Add To Cart | ✅ |
| Checkout | ✅ |

---

## Design Patterns

- Page Object Model (POM)
- Fixtures
- Data Driven Testing
- Reusable Components

---

## Reporting

HTML Reports generated automatically.

```bash
pytest
```

Report location:

```text
reports/report.html
```

---

## Screenshots on Failure

When a test fails, a screenshot is automatically captured and stored in:

```text
screenshots/
```

---

## CI/CD

GitHub Actions executes the test suite automatically on:

- Push
- Pull Request

---

## Run Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Install browsers:

```bash
playwright install
```

Execute tests:

```bash
pytest
```

---

## Future Enhancements

- API Testing
- Parallel Execution
- Cross Browser Testing
- Docker Support
- Azure DevOps Pipeline
- Allure Reports