from dataclasses import dataclass


@dataclass
class Customer:

    first_name: str = None
    last_name: str = None
    mobile_number: str = None
    email: str = None
    password: str = None
    nationality: str = None
    entity: str = None
    country_of_birth: str = None
    date_of_birth: str = None
    country_of_residence: str = None
    address_city: str = None
    address_street: str = None
    address_post_code: str = None
    address_building_number: str = None
    occupation_status: str = None
    detailed_profession: str = None
