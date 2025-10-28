import requests
import json
from jsonschema import validate
from jsonschema.exceptions import ValidationError

# Base URL for the API
BASE_URL = "http://localhost:5000"

def load_schema(schema_file):
    with open(schema_file, 'r', encoding='utf-8') as f:
        return json.load(f)

def validate_data(data, schema):
    try:
        validate(instance=data, schema=schema)
        print("✓ Dữ liệu hợp lệ!")
        return True
    except ValidationError as e:
        print("✗ Lỗi validation:")
        print(f"  - Đường dẫn: {' -> '.join(str(x) for x in e.path)}")
        print(f"  - Lỗi: {e.message}")
        return False
    except Exception as e:
        print(f"✗ Lỗi không xác định: {str(e)}")
        return False

def test_book_api():
    print("\n=== Kiểm tra API Book ===")
    try:
        # Load schema
        book_schema = load_schema('bai1_khoahoc_schema.json')
        
        # Get data from API
        response = requests.get(f"{BASE_URL}/api/book")
        if response.status_code == 200:
            data = response.json()
            print("Dữ liệu nhận được:")
            print(json.dumps(data, indent=2, ensure_ascii=False))
            validate_data(data, book_schema)
        else:
            print(f"Lỗi API: {response.status_code}")
    except Exception as e:
        print(f"Lỗi: {str(e)}")

def test_user_api(username):
    print(f"\n=== Kiểm tra API User (username: {username}) ===")
    try:
        # Load schema
        user_schema = load_schema('bai2_users_schema.json')['properties']['users']['items']
        
        # Get data from API
        response = requests.get(f"{BASE_URL}/api/user/{username}")
        if response.status_code == 200:
            data = response.json()
            print("Dữ liệu nhận được:")
            print(json.dumps(data, indent=2, ensure_ascii=False))
            validate_data(data, user_schema)
        else:
            print(f"Lỗi API: {response.status_code}")
    except Exception as e:
        print(f"Lỗi: {str(e)}")

def test_subtract_api(a, b):
    print(f"\n=== Kiểm tra API Subtract (a={a}, b={b}) ===")
    try:
        # Load schema
        subtract_schema = load_schema('subtract_schema.json')
        
        # Prepare data
        data = {"a": a, "b": b}
        
        # Validate request data
        if validate_data(data, subtract_schema):
            # Send request
            response = requests.post(f"{BASE_URL}/api/subtract", json=data)
            if response.status_code == 200:
                result = response.json()
                print("\nKết quả phép trừ:")
                print(f"{a} - {b} = {result['result']}")
            else:
                print(f"Lỗi API: {response.status_code}")
    except Exception as e:
        print(f"Lỗi: {str(e)}")

if __name__ == "__main__":
    # Test book API
    test_book_api()
    
    # Test user API with valid and invalid usernames
    test_user_api("minh123")
    test_user_api("nonexistent")
    
    # Test subtract API with valid and invalid inputs
    test_subtract_api(10, 5)
    test_subtract_api("invalid", 5)  # Should fail validation