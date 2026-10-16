# Lab 5 — Static Code Analysis Findings

Target: `wildlife_sightings.py`. Line numbers below refer to the original `wildlife_sightings_original.py`. Confirm exact messages and severities by running the tools.

| Issue | Type | Original line(s) | Description | Fix approach |
|---|---|---:|---|---|
| SQL built using string formatting | Security | 9 | User-controlled values can alter the SQL query. | Use parameterized SQL placeholders and pass values separately. |
| Mutable default argument | Bug / quality | 8 | `extras={}` can preserve state across calls. | Default to `None` and create a new dictionary inside the function. |
| MD5 hash | Security / quality | 15 | MD5 is a legacy hash and unsuitable for security-sensitive use. | Use SHA-256 for a display-only identifier; do not use it for authentication. |
| CamelCase function names | Style | 8, 14, 18 | Names do not follow normal Python snake_case conventions. | Rename functions and update calls. |
| Unclear variable `l` | Readability | 29 | Easily confused with digit one. | Use a descriptive variable such as `row`. |
| Empty result crash | Robustness | 28–30 | `min()` raises `ValueError` if no sightings exist. | Return `None` when no species are recorded. |
| Unconditional main call | Maintainability | 41 | Importing the module runs the demo. | Use the `if __name__ == "__main__":` guard. |
| Missing input validation | Robustness | 8–10 | Empty names and negative counts can be recorded. | Validate species, zone, and count; constrain count in the schema. |

## Generate before/after reports (PowerShell)

Install tools:
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install pylint bandit flake8
```

Baseline:
```powershell
pylint wildlife_sightings_original.py > pylint_before.txt 2>&1
bandit -r wildlife_sightings_original.py > bandit_before.txt 2>&1
flake8 wildlife_sightings_original.py > flake8_before.txt 2>&1
```

After fixes:
```powershell
pylint wildlife_sightings.py > pylint_after.txt 2>&1
bandit -r wildlife_sightings.py > bandit_after.txt 2>&1
flake8 wildlife_sightings.py > flake8_after.txt 2>&1
```

The handout target is a Pylint score above 9.5/10. Verify the actual score; do not claim the target is met until measured.
