"""
Author : Humayra Khanom
"""

import requests

def test_brands_list():
    print("\n=== Test 1: Validate Brand List ===")
    url = "https://automationexercise.com/api/brandsList"
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        expected_brands = ["Polo", "Babyhug", "Biba"]
        unexpected_brands = ["Heineken", "BMW", "Razor"]
        print("\nChecking for expected brands:")
        for brand in expected_brands:
            is_present = any(brand.lower() == b['brand'].lower() for b in data['brands'])
            print(f"Brand '{brand}' is present: {is_present}")
        print("\nChecking for unexpected brands:")
        for brand in unexpected_brands:
            is_absent = all(brand.lower() != b['brand'].lower() for b in data['brands'])
            print(f"Brand '{brand}' is absent: {is_absent}")
    else:
        print(f"Failed to get brands list. Status code: {response.status_code}")

def test_user_login(email, password):
    print("\n=== Test 2: Verify User Login ===")
    url = "https://automationexercise.com/api/verifyLogin"
    data = {
        'email': email,
        'password': password
    }
    response = requests.post(url, data=data)
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        response_data = response.json()
        print(f"\nResponse message: {response_data.get('message', 'No message found')}")
        expected_message = "User exists!"
        is_message_correct = response_data.get('message') == expected_message
        print(f"Message matches expected '{expected_message}': {is_message_correct}")
    else:
        print(f"Failed to verify login. Status code: {response.status_code}")

if __name__ == "__main__":
    test_brands_list()
    email = "humayrakhanom@gmail.com"
    password = "test1234"
    test_user_login(email, password)
