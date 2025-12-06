# UI Testing Playground Automation

Автоматизация UI-тестов с использованием **Python + Selenium + Pytest**.  
Тесты запускаются автоматически через **GitLab CI/CD**.

Запуск локально
```bash
pip install -r requirements.txt
pytest -v
allure serve reports
