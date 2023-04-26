from faker import Faker
from random import randint
from app.models.customer import Customer


def get_customer_instance(account: Customer = None):
    fake = Faker()
    name = fake.name().split(),
    mobile_number = f'{randint(10000000, 99999999) }',
    email = fake.email(),
    password = 'Test@123',
    nationality = 'Jordan',
    country_of_birth = 'Cyprus',
    entity = 'cy'
    date_of_birth = '12122000'
    country_of_residence = 'Jordan'
    address_city = 'New York'
    address_street = 'Lombard street'
    address_post_code = '6027'
    address_building_number = '18'
    occupation_status = 'Employed'
    detailed_profession = 'QA automation engineer'
    return Customer(first_name=name[0][0],
                    last_name=name[0][1],
                    mobile_number=mobile_number[0],
                    email=email[0],
                    password=password[0],
                    nationality=nationality[0],
                    country_of_birth=country_of_birth[0],
                    entity=entity,
                    date_of_birth=date_of_birth,
                    country_of_residence=country_of_residence,
                    address_city=address_city,
                    address_street=address_street,
                    address_post_code=address_post_code,
                    address_building_number=address_building_number,
                    occupation_status=occupation_status,
                    detailed_profession=detailed_profession
                    )
