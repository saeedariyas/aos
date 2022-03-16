from faker import Faker

fake = Faker(locale='en_CA')

app = 'Advantageonlineshopping'
app_url = 'https://advantageonlineshopping.com/#/'
home_page_title = '\xa0Advantage Shopping'
first_name = fake.first_name()
last_name = fake.last_name()
full_name = first_name+' '+last_name
new_username = f'{first_name}'.lower()
new_password = fake.password()
email = f'{new_username}@{fake.free_email_domain()}'
phone = fake.phone_number()
city = fake.city()
country = fake.current_country()
address = fake.address().replace("\n", " ")[:5]
state = fake.word()
postalcode = fake.postalcode()
email1 = fake.email()
subject = fake.sentence(nb_words=10)
spusername = 'sp_'+new_username
sppassword = 'Sp123'

list_names = ['usernameRegisterPage', 'emailRegisterPage', 'passwordRegisterPage', 'confirm_passwordRegisterPage'
    , 'first_nameRegisterPage', 'last_nameRegisterPage', 'phone_numberRegisterPage',
              'cityRegisterPage', 'addressRegisterPage', 'state_/_province_/_regionRegisterPage',
              'postal_codeRegisterPage']
list_val = [new_username, email, new_password, new_password,
            first_name, last_name, phone,
            city, address, state, postalcode]

list_txtid = ['speakersTxt', 'tabletsTxt', 'laptopsTxt', 'miceTxt', 'headphonesTxt']
list_lblid = ['speakersLink', 'tabletsLink', 'laptopsLink', 'miceLink', 'headphonesLink']
list_txt = ['SPEAKERS', 'TABLETS', 'LAPTOPS', 'MICE', 'HEADPHONES']
