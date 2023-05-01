import os
import allure
import pytest

from app.pages.header_page import HeaderPage
from app.pages.registration_page import RegistrationPage
from app.utilities.get_parameters_from_file import data_generator


# @allure.tag('id 1.1')
# @allure.label('owner', 'SergeiT')
# @allure.severity('normal')
# @allure.feature('Registration page')
# @allure.title('Customer fill the correct data')
# @pytest.mark.parametrize('customer_credentials', data_generator('customer_registration_data.csv'))
# def test_fill_the_registration_page_from_file(customer_credentials, wd):
#     registration_page = RegistrationPage(wd)
#     url = f"{os.getenv('URL_PROD')}/cy/en/registration"
#     registration_page.open(url)
#     registration_page.fill_the_first_name(customer_credentials[0])
#     registration_page.fill_the_last_name(customer_credentials[1])
#     registration_page.fill_the_phone(customer_credentials[2])
#     registration_page.fill_the_email(customer_credentials[3])
#     registration_page.fill_the_password(customer_credentials[4])
#     registration_page.click_on_checkbox()
#     registration_page.click_on_next_btn()
#     result = registration_page.assert_text_in_url('/verification')
#     registration_page.assert_test_result(customer_credentials[5], result)


@allure.tag('id 1.2')
@allure.label('owner', 'SergeiT')
@allure.severity('normal')
@allure.feature('Registration page')
@allure.title("Customer doesn't fill the first name")
def test_empty_first_name(wd):
    registration_page = RegistrationPage(wd)
    url = "https://registration.cfifinancial.com/cy/en/registration"
    registration_page.open(url)
    registration_page.click_on_next_btn()
    registration_page.assert_first_name_error('Please complete your first name')


@allure.tag('id 1.3')
@allure.label('owner', 'SergeiT')
@allure.severity('normal')
@allure.feature('Registration page')
@allure.title("Customer fill the first name with incorrect data")
@pytest.mark.parametrize('incorrect_name', data_generator('customer_names.csv'))
def test_incorrect_first_name(incorrect_name, wd):
    registration_page = RegistrationPage(wd)
    url = f"{os.getenv('URL_PROD')}/cy/en/registration"
    registration_page.open(url)
    registration_page.fill_the_first_name(incorrect_name[0])
    registration_page.click_on_next_btn()
    registration_page.assert_first_name_error(incorrect_name[1])


@allure.tag('id 1.4')
@allure.label('owner', 'SergeiT')
@allure.severity('normal')
@allure.feature('Registration page')
@allure.title("Customer doesn't fill the last name")
def test_empty_last_name(wd):
    registration_page = RegistrationPage(wd)
    url = f"{os.getenv('URL_PROD')}/cy/en/registration"
    registration_page.open(url)
    registration_page.click_on_next_btn()
    registration_page.assert_last_name_error('Please complete your last name')


@allure.tag('id 1.5')
@allure.label('owner', 'SergeiT')
@allure.severity('normal')
@allure.feature('Registration page')
@allure.title("Customer doesn't fill mobile number")
def test_empty_mobile_number(wd):
    registration_page = RegistrationPage(wd)
    url = f"{os.getenv('URL_PROD')}/cy/en/registration"
    registration_page.open(url)
    registration_page.click_on_next_btn()
    registration_page.assert_mobile_phone_error('This is a required field.')


@allure.tag('id 1.6')
@allure.label('owner', 'SergeiT')
@allure.severity('normal')
@allure.feature('Registration page')
@allure.title("Customer fill mobile number with incorrect data")
@pytest.mark.parametrize('incorrect_phone', data_generator('customer_phones.csv'))
def test_incorrect_mobile_number(incorrect_phone, wd):
    registration_page = RegistrationPage(wd)
    url = f"{os.getenv('URL_PROD')}/cy/en/registration"
    registration_page.open(url)
    registration_page.fill_the_phone(incorrect_phone)
    registration_page.click_on_next_btn()
    registration_page.assert_mobile_phone_error('Please enter a valid mobile number')


@allure.tag('id 1.7')
@allure.label('owner', 'SergeiT')
@allure.severity('normal')
@allure.feature('Registration page')
@allure.title("Customer doesn't fill email")
def test_empty_email(wd):
    registration_page = RegistrationPage(wd)
    url = f"{os.getenv('URL_PROD')}/cy/en/registration"
    registration_page.open(url)
    registration_page.click_on_next_btn()
    registration_page.assert_email_error('This is a required field.')


@allure.tag('id 1.8')
@allure.label('owner', 'SergeiT')
@allure.severity('normal')
@allure.feature('Registration page')
@allure.title("Customer fill email with incorrect data")
@pytest.mark.parametrize('incorrect_email', data_generator('customer_emails.csv'))
def test_incorrect_email(incorrect_email, wd):
    registration_page = RegistrationPage(wd)
    url = f"{os.getenv('URL_PROD')}/cy/en/registration"
    registration_page.open(url)
    registration_page.fill_the_email(incorrect_email)
    registration_page.click_on_next_btn()
    registration_page.assert_email_error('Email is invalid.')


@allure.tag('1.9.1')
@allure.label('owner', 'SergeiT')
@allure.severity('normal')
@allure.feature('Registration page')
@allure.title("Customer doesn't fill password. Length check")
def test_empty_password_length(wd):
    registration_page = RegistrationPage(wd)
    url = f"{os.getenv('URL_PROD')}/cy/en/registration"
    registration_page.open(url)
    registration_page.click_on_next_btn()
    registration_page.assert_password_length_icon('greyout')


@allure.tag('1.9.2')
@allure.label('owner', 'SergeiT')
@allure.severity('normal')
@allure.feature('Registration page')
@allure.title("Customer doesn't fill password. Upper case check")
def test_empty_password_uppercase(wd):
    registration_page = RegistrationPage(wd)
    url = f"{os.getenv('URL_PROD')}/cy/en/registration"
    registration_page.open(url)
    registration_page.click_on_next_btn()
    registration_page.assert_password_upper_case_icon('greyout')


@allure.tag('1.9.3')
@allure.label('owner', 'SergeiT')
@allure.severity('normal')
@allure.feature('Registration page')
@allure.title("Customer doesn't fill password. Lower case check")
def test_empty_password_lowercase(wd):
    registration_page = RegistrationPage(wd)
    url = f"{os.getenv('URL_PROD')}/cy/en/registration"
    registration_page.open(url)
    registration_page.click_on_next_btn()
    registration_page.assert_password_lower_case_icon('greyout')


@allure.tag('1.9.4')
@allure.label('owner', 'SergeiT')
@allure.severity('normal')
@allure.feature('Registration page')
@allure.title("Customer doesn't fill password. Numbers check")
def test_empty_password_numeric(wd):
    registration_page = RegistrationPage(wd)
    url = f"{os.getenv('URL_PROD')}/cy/en/registration"
    registration_page.open(url)
    registration_page.click_on_next_btn()
    registration_page.assert_password_numeric_icon('greyout')


@allure.tag('1.10')
@allure.label('owner', 'SergeiT')
@allure.severity('normal')
@allure.feature('Registration page')
@allure.title("Customer fill password with lower case letters")
def test_fill_password_lowercase(wd):
    registration_page = RegistrationPage(wd)
    url = f"{os.getenv('URL_PROD')}/cy/en/registration"
    registration_page.open(url)
    registration_page.fill_the_password('abcd')
    registration_page.click_on_next_btn()
    registration_page.assert_password_lower_case_icon('black')


@allure.tag('1.11')
@allure.label('owner', 'SergeiT')
@allure.severity('normal')
@allure.feature('Registration page')
@allure.title("Customer fill password with upper case letters")
def test_fill_password_lowercase(wd):
    registration_page = RegistrationPage(wd)
    url = f"{os.getenv('URL_PROD')}/cy/en/registration"
    registration_page.open(url)
    registration_page.fill_the_password('ABCD')
    registration_page.click_on_next_btn()
    registration_page.assert_password_upper_case_icon('black')


@allure.tag('1.12')
@allure.label('owner', 'SergeiT')
@allure.severity('normal')
@allure.feature('Registration page')
@allure.title("Customer fill password with digits")
def test_fill_password_with_digits(wd):
    registration_page = RegistrationPage(wd)
    url = f"{os.getenv('URL_PROD')}/cy/en/registration"
    registration_page.open(url)
    registration_page.fill_the_password('1234')
    registration_page.click_on_next_btn()
    registration_page.assert_password_numeric_icon('black')


@allure.tag('1.13')
@allure.label('owner', 'SergeiT')
@allure.severity('normal')
@allure.feature('Registration page')
@allure.title("Customer fill password more than 8 chars")
def test_fill_password_more_than_eight_chars(wd):
    registration_page = RegistrationPage(wd)
    url = f"{os.getenv('URL_PROD')}/cy/en/registration"
    registration_page.open(url)
    registration_page.fill_the_password('123456789')
    registration_page.click_on_next_btn()
    registration_page.assert_password_length_icon('black')


@allure.tag('1.14')
@allure.label('owner', 'SergeiT')
@allure.severity('normal')
@allure.feature('Registration page')
@allure.title("Customer fill password more than 20 chars")
def test_fill_password_more_than_twenty_chars(wd):
    registration_page = RegistrationPage(wd)
    url = f"{os.getenv('URL_PROD')}/cy/en/registration"
    registration_page.open(url)
    registration_page.fill_the_password('012345678901234567890')
    registration_page.click_on_next_btn()
    registration_page.assert_password_length_icon('greyout')


@allure.tag('1.15')
@allure.label('owner', 'SergeiT')
@allure.severity('normal')
@allure.feature('Registration page')
@allure.title("Customer fill correct password")
def test_fill_correct_password_length(wd):
    registration_page = RegistrationPage(wd)
    url = f"{os.getenv('URL_PROD')}/cy/en/registration"
    registration_page.open(url)
    registration_page.fill_the_password('Qwer1234')
    registration_page.click_on_next_btn()
    registration_page.assert_password_length_icon('black')
    registration_page.assert_password_numeric_icon('black')
    registration_page.assert_password_upper_case_icon('black')
    registration_page.assert_password_lower_case_icon('black')


@allure.tag('1.16')
@allure.label('owner', 'SergeiT')
@allure.severity('normal')
@allure.feature('Registration page')
@allure.title("Customer doesn't check checkbox")
def test_not_checked_checkbox(wd):
    registration_page = RegistrationPage(wd)
    url = f"{os.getenv('URL_PROD')}/cy/en/registration"
    registration_page.open(url)
    registration_page.click_on_next_btn()
    registration_page.assert_color_of_checkbox_label('f44336')


@allure.tag('1.17')
@allure.label('owner', 'SergeiT')
@allure.severity('normal')
@allure.feature('Registration page')
@allure.title("Assert the checkbox text")
def test_assert_checkbox_text(wd):
    registration_page = RegistrationPage(wd)
    url = f"{os.getenv('URL_PROD')}/cy/en/registration"
    registration_page.open(url)
    registration_page.assert_checkbox_text('By clicking “Next”, you agree to Privacy Policy and Cookies Policy, and understand you may be contacted by Credit Financier Invest (CFI) Ltd in relation to your application.')


@allure.tag('1.18')
@allure.label('owner', 'SergeiT')
@allure.severity('normal')
@allure.feature('Registration page')
@allure.title("Assert the link 'Privacy policy'")
def test_assert_privacy_policy_link(wd):
    registration_page = RegistrationPage(wd)
    url = f"{os.getenv('URL_PROD')}/cy/en/registration"
    registration_page.open(url)
    registration_page.assert_privacy_policy_link('https://cfifinancial.com/files/cy/f/Privacy%20Policy.pdf')


@allure.tag('1.19')
@allure.label('owner', 'SergeiT')
@allure.severity('normal')
@allure.feature('Registration page')
@allure.title("Assert the link 'Cookies policy'")
def test_assert_cookies_policy_link(wd):
    registration_page = RegistrationPage(wd)
    url = f"{os.getenv('URL_PROD')}/cy/en/registration"
    registration_page.open(url)
    registration_page.assert_cookies_policy_link('https://cfifinancial.com/files/cy/f/Cookies-Policy_Nov-22.pdf')


@allure.tag('1.20')
@allure.label('owner', 'SergeiT')
@allure.severity('normal')
@allure.feature('Registration page')
@allure.title("Assert the 'Next' button title")
def test_assert_next_button_title(wd):
    registration_page = RegistrationPage(wd)
    url = f"{os.getenv('URL_PROD')}/cy/en/registration"
    registration_page.open(url)
    registration_page.assert_next_button_title('Next')


@allure.tag('1.21')
@allure.label('owner', 'SergeiT')
@allure.severity('normal')
@allure.feature('Registration page')
@allure.title('Check the phone code visibility')
def test_phone_code_visibility(wd):
    registration_page = RegistrationPage(wd)
    url = f"{os.getenv('URL_PROD')}/cy/en/registration"
    registration_page.open(url)
    registration_page.assert_not_empty_phone_code()


@allure.tag('1.22')
@allure.label('owner', 'SergeiT')
@allure.severity('normal')
@allure.feature('Registration page')
@allure.title('Change the phone code')
def test_change_phone_code(wd):
    registration_page = RegistrationPage(wd)
    url = f"{os.getenv('URL_PROD')}/cy/en/registration"
    registration_page.open(url)
    registration_page.choose_the_phone_code()


@allure.tag('1.23')
@allure.label('owner', 'SergeiT')
@allure.severity('normal')
@allure.feature('Registration page')
@allure.title('Check password invisibility')
def test_check_password_invisibility(wd):
    registration_page = RegistrationPage(wd)
    url = f"{os.getenv('URL_PROD')}/cy/en/registration"
    registration_page.open(url)
    registration_page.assert_password_invisibility()
    registration_page.click_on_eye_icon()
    registration_page.assert_password_visibility()


@allure.tag('2.1')
@allure.label('owner', 'PhoebeG')
@allure.severity('normal')
@allure.feature('Registration page')
@allure.title('Check First Name field title')
def test_check_first_name_title(wd):
    registration_page = RegistrationPage(wd)
    url = f"{os.getenv('URL_PROD')}/cy/en/registration"
    registration_page.open(url)
    registration_page.assert_the_first_name_title('First Name')


@allure.tag('2.2')
@allure.label('owner', 'PhoebeG')
@allure.severity('normal')
@allure.feature('Registration page')
@allure.title('Check Last Name field title')
def test_check_last_name_title(wd):
    registration_page = RegistrationPage(wd)
    url = f"{os.getenv('URL_PROD')}/cy/en/registration"
    registration_page.open(url)
    registration_page.assert_the_last_name_title('Last Name')


@allure.tag('2.3')
@allure.label('owner', 'PhoebeG')
@allure.severity('normal')
@allure.feature('Registration page')
@allure.title('Check Mobile Number field title')
def test_check_mobile_number_title(wd):
    registration_page = RegistrationPage(wd)
    url = f"{os.getenv('URL_PROD')}/cy/en/registration"
    registration_page.open(url)
    registration_page.assert_the_mobile_number_title('Mobile Number')


@allure.tag('2.4')
@allure.label('owner', 'PhoebeG')
@allure.severity('normal')
@allure.feature('Registration page')
@allure.title('Check Email Address field title')
def test_check_email_address_title(wd):
    registration_page = RegistrationPage(wd)
    url = f"{os.getenv('URL_PROD')}/cy/en/registration"
    registration_page.open(url)
    registration_page.assert_the_email_address_title('Email Address')


@allure.tag('2.5')
@allure.label('owner', 'PhoebeG')
@allure.severity('normal')
@allure.feature('Registration page')
@allure.title('Check Create Password field title')
def test_check_password_title(wd):
    registration_page = RegistrationPage(wd)
    url = f"{os.getenv('URL_PROD')}/cy/en/registration"
    registration_page.open(url)
    registration_page.assert_the_password_title('Create Password')


@allure.tag('3.1')
@allure.label('owner', 'PhoebeG')
@allure.severity('normal')
@allure.feature('Registration page')
@allure.title('Check First Name input placeholder')
def test_check_first_name_placeholder(wd):
    registration_page = RegistrationPage(wd)
    url = f"{os.getenv('URL_PROD')}/cy/en/registration"
    registration_page.open(url)
    registration_page.assert_the_first_name_placeholder('Enter your first name')


@allure.tag('3.2')
@allure.label('owner', 'PhoebeG')
@allure.severity('normal')
@allure.feature('Registration page')
@allure.title('Check Last Name input placeholder')
def test_check_last_name_placeholder(wd):
    registration_page = RegistrationPage(wd)
    url = f"{os.getenv('URL_PROD')}/cy/en/registration"
    registration_page.open(url)
    registration_page.assert_the_last_name_placeholder('Enter your last name')


@allure.tag('3.3')
@allure.label('owner', 'PhoebeG')
@allure.severity('normal')
@allure.feature('Registration page')
@allure.title('Check Mobile Country Code input placeholder')
def test_check_mobile_country_code_placeholder(wd):
    registration_page = RegistrationPage(wd)
    url = f"{os.getenv('URL_PROD')}/cy/en/registration"
    registration_page.open(url)
    registration_page.assert_not_empty_phone_code()


@allure.tag('3.4')
@allure.label('owner', 'PhoebeG')
@allure.severity('normal')
@allure.feature('Registration page')
@allure.title('Check Mobile Number input placeholder')
def test_check_mobile_number_placeholder(wd):
    registration_page = RegistrationPage(wd)
    url = f"{os.getenv('URL_PROD')}/cy/en/registration"
    registration_page.open(url)
    registration_page.assert_the_mobile_number_placeholder()


@allure.tag('3.5')
@allure.label('owner', 'PhoebeG')
@allure.severity('normal')
@allure.feature('Registration page')
@allure.title('Check Email Address input placeholder')
def test_check_email_address_placeholder(wd):
    registration_page = RegistrationPage(wd)
    url = f"{os.getenv('URL_PROD')}/cy/en/registration"
    registration_page.open(url)
    registration_page.assert_the_email_address_placeholder('Enter your email address')


@allure.tag('3.6')
@allure.label('owner', 'PhoebeG')
@allure.severity('normal')
@allure.feature('Registration page')
@allure.title('Check Create Password input placeholder')
def test_check_create_password_placeholder(wd):
    registration_page = RegistrationPage(wd)
    url = f"{os.getenv('URL_PROD')}/cy/en/registration"
    registration_page.open(url)
    registration_page.assert_the_create_password_placeholder('Password')


@allure.tag('4.1')
@allure.label('owner', 'PhoebeG')
@allure.severity('normal')
@allure.feature('Registration page')
@allure.title('Check header text')
def test_header_text(wd):
    registration_page = RegistrationPage(wd)
    url = f"{os.getenv('URL_PROD')}/cy/en/registration"
    registration_page.open(url)
    registration_page.assert_header_text('Before you apply: Please read and understand the Risk disclosure, Privacy policy, Order execution policy, Conflicts policy, Terms and conditions, Shares Trading terms and conditions which I agree is provided by the CFI website.')


@allure.tag('4.2')
@allure.label('owner', 'PhoebeG')
@allure.severity('normal')
@allure.feature('Registration page')
@allure.title("Assert the link 'Risk disclosure'")
def test_assert_risk_disclosure_link(wd):
    registration_page = RegistrationPage(wd)
    url = f"{os.getenv('URL_PROD')}/cy/en/registration"
    registration_page.open(url)
    registration_page.assert_risk_disclosure_link('https://cfifinancial.com/files/cy/f/Disclaimer.pdf')


@allure.tag('4.3')
@allure.label('owner', 'PhoebeG')
@allure.severity('normal')
@allure.feature('Registration page')
@allure.title("Assert the link 'Privacy Policy'")
def test_assert_header_privacy_policy_link(wd):
    registration_page = RegistrationPage(wd)
    url = f"{os.getenv('URL_PROD')}/cy/en/registration"
    registration_page.open(url)
    registration_page.assert_privacy_policy_link('https://cfifinancial.com/files/cy/f/Privacy%20Policy.pdf')


@allure.tag('4.4')
@allure.label('owner', 'PhoebeG')
@allure.severity('normal')
@allure.feature('Registration page')
@allure.title("Assert the link 'Order Execution Policy'")
def test_assert_header_order_execution_policy_link(wd):
    registration_page = RegistrationPage(wd)
    url = f"{os.getenv('URL_PROD')}/cy/en/registration"
    registration_page.open(url)
    registration_page.assert_order_execution_policy_link('https://cfifinancial.com/files/cy/f/Order%20Execution%20Policy.pdf')


@allure.tag('4.5')
@allure.label('owner', 'PhoebeG')
@allure.severity('normal')
@allure.feature('Registration page')
@allure.title("Assert the link 'Conflicts Policy'")
def test_assert_header_conflicts_policy_link(wd):
    registration_page = RegistrationPage(wd)
    url = f"{os.getenv('URL_PROD')}/cy/en/registration"
    registration_page.open(url)
    registration_page.assert_conflicts_policy_link('https://cfifinancial.com/files/cy/f/Conflict-of-Interest-Policy_Oct22.pdf')


@allure.tag('4.6')
@allure.label('owner', 'PhoebeG')
@allure.severity('normal')
@allure.feature('Registration page')
@allure.title("Assert the link 'Terms and Conditions'")
def test_assert_header_terms_and_conditions_link(wd):
    registration_page = RegistrationPage(wd)
    url = f"{os.getenv('URL_PROD')}/cy/en/registration"
    registration_page.open(url)
    registration_page.assert_terms_and_condition_link('https://cfifinancial.com/files/cy/f/Terms-and-Conditions_nov22.pdf')


@allure.tag('4.7')
@allure.label('owner', 'PhoebeG')
@allure.severity('normal')
@allure.feature('Registration page')
@allure.title("Assert the link 'Shares Trading terms and conditions'")
def test_assert_header_shares_trading_terms_and_conditions_link(wd):
    registration_page = RegistrationPage(wd)
    url = f"{os.getenv('URL_PROD')}/cy/en/registration"
    registration_page.open(url)
    registration_page.assert_shares_trading_terms_and_condition_link('https://cfifinancial.com/files/cy/f/Shares-Terms-and-Conditions-Nov-22-v2.pdf')


@allure.tag('4.8')
@allure.label('owner', 'PhoebeG')
@allure.severity('normal')
@allure.feature('Registration page')
@allure.title("Assert the link 'CFI CY website'")
def test_assert_cy_website_link(wd):
    registration_page = RegistrationPage(wd)
    url = f"{os.getenv('URL_PROD')}/cy/en/registration"
    registration_page.open(url)
    registration_page.assert_cy_website_link('https://cfifinancial.com/en-cy/about-us/regulatory')


@allure.tag('4.9')
@allure.label('owner', 'PhoebeG')
@allure.severity('normal')
@allure.feature('Registration page')
@allure.title("Assert the first step bullet color")
def test_assert_the_first_step_bullet_color(wd):
    registration_page = RegistrationPage(wd)
    header_page = HeaderPage(wd)
    url = f"{os.getenv('URL_PROD')}/cy/en/registration"
    registration_page.open(url)
    header_page.assert_color_of_step_element('09b9d4', '1')


@allure.tag('4.10')
@allure.label('owner', 'PhoebeG')
@allure.severity('normal')
@allure.feature('Registration page')
@allure.title("Assert the second step bullet color")
def test_assert_the_second_step_bullet_color(wd):
    registration_page = RegistrationPage(wd)
    header_page = HeaderPage(wd)
    url = f"{os.getenv('URL_PROD')}/cy/en/registration"
    registration_page.open(url)
    header_page.assert_color_of_step_element('b3babe', '2')


@allure.tag('4.11')
@allure.label('owner', 'PhoebeG')
@allure.severity('normal')
@allure.feature('Registration page')
@allure.title("Assert the third step bullet color")
def test_assert_the_third_step_bullet_color(wd):
    registration_page = RegistrationPage(wd)
    header_page = HeaderPage(wd)
    url = f"{os.getenv('URL_PROD')}/cy/en/registration"
    registration_page.open(url)
    header_page.assert_color_of_step_element('b3babe', '3')


@allure.tag('4.12')
@allure.label('owner', 'PhoebeG')
@allure.severity('normal')
@allure.feature('Registration page')
@allure.title("Assert the fourth step bullet color")
def test_assert_the_fourth_step_bullet_color(wd):
    registration_page = RegistrationPage(wd)
    header_page = HeaderPage(wd)
    url = f"{os.getenv('URL_PROD')}/cy/en/registration"
    registration_page.open(url)
    header_page.assert_color_of_step_element('b3babe', '4')


@allure.tag('4.13')
@allure.label('owner', 'PhoebeG')
@allure.severity('normal')
@allure.feature('Registration page')
@allure.title("Assert logo visibility")
def test_assert_logo_visibility(wd):
    registration_page = RegistrationPage(wd)
    header_page = HeaderPage(wd)
    url = f"{os.getenv('URL_PROD')}/cy/en/registration"
    registration_page.open(url)
    header_page.assert_logo_visibility()
