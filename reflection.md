# Lab 5 Reflection — Static Code Analysis

## 1. What is static code analysis, and why is it useful?
Static code analysis examines source code without running it. It helps find potential bugs, insecure patterns, maintainability issues, and style violations early.

## 2. What did Pylint, Bandit, and Flake8 contribute?
Pylint focuses on code quality, common mistakes, and naming. Bandit checks for common security-risk patterns in Python. Flake8 checks style and basic errors such as whitespace, line length, and PEP 8 conventions.

## 3. Which issues were fixed, and why?
The corrected code uses parameterized SQL, avoids a mutable dictionary default, uses SHA-256 for a short display identifier, follows snake_case naming, handles an empty sightings table, validates input, and uses a main guard. These changes improve security, correctness, and maintainability.

## 4. What are the benefits and limitations of static analysis?
Static analysis provides quick, repeatable feedback and can catch issues before tests or manual review. However, tools can produce false positives and cannot prove a program is fully correct or secure. Results should be combined with tests and code review. Actual reports should be checked before claiming all findings are resolved.
