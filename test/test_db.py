from db import config
from sqlalchemy import text

def test_config():
    try:
        with config.engine.connect() as conn:
            result = conn.execute(text("SELECT 1")).scalar()
            print(f"Connection OK! Result: {result}")
    except Exception as e:
        print(e)

def main() -> None:
    test_config()

if __name__ == '__main__':
    main()