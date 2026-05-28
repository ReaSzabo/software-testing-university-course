# Behave + Selenium demo for saucedemo test page

Course assignment for Software Testing (ILBPM9939L).
Stack: Python + Behave + Selenium + webdriver-manager, testing https://www.saucedemo.com/.

## Run project:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
behave
```

Scenarios and points:

- Scenario: Logout
- Scenario: Open About page
- Scenario: Twitter link opens correct page
- Scenario: Facebook link opens correct page
- Scenario: LinkedIn link opens correct page
- Scenario Outline: Login attempts (4 examples)
- Scenario Outline: Cart count grows as items are added (6 examples)
- Scenario Outline: Remove buttons grow with cart items (6 examples)
- Scenario Outline: Cart count decreases as items are removed (6 examples)
- Scenario Outline: Products can be sorted by different filters (4 examples)

Totals:
- 5 Scenarios
- 5 Scenario Outlines
- 31 total test cases

Estimated points by the given rules:
- Scenario: 3 points * 5 = 15 points
- Scenario Outline: Login attempts = 2 + 4 = 6 points
- Scenario Outline: Cart growth = 2 + 6 = 8 points, max 6 points
- Scenario Outline: Cart remove growth = 2 + 6 = 8 points, max 6 points
- Scenario Outline: Cart remove decrease = 2 + 6 = 8 points, max 6 points
- Scenario Outline: Products sorting = 2 + 4 = 6 points
- Total: 15 + 6 + 6 + 6 + 6 + 6 = 45 points

