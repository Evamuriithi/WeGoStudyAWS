import datetime
from faker import Faker
fake = Faker(locale='en_CA')
import random



app = 'WeGoStudy'
wegostudy_url = 'https://www.wegostudy.ca/'
wegostudy_home_page_title = 'WeGoStudy'
wegostudy_partner_login_page_url = 'https://www.wegostudy.ca/partner/home'
new_username = fake.user_name()
new_password = fake.password()
first_name = fake.first_name()
last_name = fake. last_name()
middle_name = fake.first_name()
full_name = f'{first_name} {last_name}'
admin_email = 'pewec@protonmail.com'
admin_password = '789WeStudy!'
email = fake.email()

country_citizenship = fake.country()
phone_number = fake.pyint(11111111111, 77777777777)
address = fake.address()
country = fake.current_country()
country2 = fake.country()
city = fake.city()
province = fake.province_abbr()[0:10]
postalcode = fake.postcode()[0:10]
school = f'{province} University'
program = random.choice(['Computer', 'Physics', 'Statistic', 'Math', 'Biologist', 'Chemistry', 'Architecture'])
gpa = fake.pyint(1,100)
date_of_birth = fake.date()[0:50]
passport_number = fake.pyint(1111111, 7777777)
credentials = random.choices(['Degree', 'Certificate', 'Diploma', 'Doctoral'])
schools = random.choices(['Alexander College', 'Acsenda School of Management', 'Capilano University','Columbia College', 'Durham College', 'Okanagan College'])
gpa_scale = fake.pyint(1,100)


lst_column = ['First Name', 'Last Name', 'Phone Number', 'Mailing Address', 'Postalcode']

lst_id = ['user_partner_detail_attributes_first_name',
          'user_partner_detail_attributes_last_name',
          'partner_phone_number',
          'user_partner_detail_attributes_address_attributes_mailing_address',
          'user_partner_detail_attributes_address_attributes_state_chosen']

lst_value = [first_name, last_name, phone_number, address, postalcode]

filename = '1.mp3'
byPassUrl = 'https://www.google.com/recaptcha/api2/demo'
googleIBMLink = 'https://speech-to-text-demo.ng.bluemix.net/'
