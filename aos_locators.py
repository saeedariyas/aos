from faker import Faker

fake = Faker(locale='en_CA')

app = 'Advantageonlineshopping'
app_url = 'https://advantageonlineshopping.com/#/'
home_page_title = '\xa0Advantage Shopping'
first_name = fake.first_name()
last_name = fake.last_name()
new_username = f'{first_name}'.lower()
new_password = fake.password()
email = f'{new_username}@{fake.free_email_domain()}'
phone = fake.phone_number()
city = fake.city()
country = fake.current_country()
address = fake.address().replace("\n", " ")[:5]
state = fake.word()
postalcode = fake.postalcode()

list_names = ['usernameRegisterPage', 'emailRegisterPage', 'passwordRegisterPage', 'confirm_passwordRegisterPage'
    , 'first_nameRegisterPage', 'last_nameRegisterPage', 'phone_numberRegisterPage',
              'cityRegisterPage', 'addressRegisterPage', 'state_/_province_/_regionRegisterPage',
              'postal_codeRegisterPage']
list_val = [new_username, email, new_password, new_password,
            first_name, last_name, phone,
            city, address, state, postalcode]