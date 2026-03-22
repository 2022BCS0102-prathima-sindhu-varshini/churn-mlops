1. Install dependencies:
   pip install -r requirements.txt

2. Run API:
   uvicorn app.main:app --reload

3. Open browser:
   http://127.0.0.1:8000/docs

4. Run tests:
   python -m pytest

5. Run Docker:
   docker build -t churn-app .
   docker run -p 8000:8000 churn-app

6. Train ML model:
   python train.py