"""Simple runner to start the FastAPI app with Uvicorn for local testing.

Usage (from the `backend` folder):

    python -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

Or run this script directly (requires `uvicorn` installed in the active Python environment):

    python run_uvicorn.py
"""

if __name__ == '__main__':
    import os
    import sys

    try:
        import uvicorn
    except Exception:
        print('uvicorn is not installed in this Python environment. Install with: pip install "uvicorn[standard]"')
        sys.exit(1)

    uvicorn.run('app.main:app', host=os.environ.get('UVICORN_HOST', '127.0.0.1'), port=int(os.environ.get('UVICORN_PORT', 8000)), reload=True)
