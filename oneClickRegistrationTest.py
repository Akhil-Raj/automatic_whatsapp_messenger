import requests

def test_get_name_from_phone(phone):
    try:
        response = requests.get(f'https://www.gitalifenyc.com/api/get-name-from-phone?phone={phone}')
        data = response.json()
        if not (response.ok):
            raise Exception
        print('Get Name Response:', data)
    except Exception as e:
        print('Error fetching name:', e)
        exit(0)

def test_mark_registered(phone):
    try:
        response = requests.post('https://www.gitalifenyc.com/api/mark-registered', json={'contact': phone})
        data = response.json()
        if not (response.ok):
            raise Exception
        print('Mark Registered Response:', data)
    except Exception as e:
        print('Error marking registered:', e)
        exit(0)

if __name__ == '__main__':
    # Replace 'YOUR_PHONE_NUMBER' with the actual phone number you want to test
    phone_number = 'YOUR_PHONE_NUMBER'

    test_get_name_from_phone(phone_number)
    test_mark_registered(phone_number)