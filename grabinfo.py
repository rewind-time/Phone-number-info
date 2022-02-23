#importing all the modules
import phonenumbers
from phonenumbers import timezone
from phonenumbers import geocoder
from phonenumbers import carrier
import pyautogui

#define all the variables
my_ph = pyautogui.prompt('Enter a phone number: ')
ph = phonenumbers.parse(my_ph)
format = phonenumbers.PhoneNumberFormat.INTERNATIONAL
city = geocoder.description_for_number(ph, 'nl')
formatted = phonenumbers.format_number(ph, format)
Carrier = carrier.name_for_number(ph, None)
timeZone = timezone.time_zones_for_number(ph)
IsValid = phonenumbers.is_valid_number(ph)

#main function
def main():
    print('Phone: ', formatted)
    print('Detail: ', ph)
    print('Time zone: ', timeZone)
    print('Carrier: ', Carrier)
    print('Country: ', city)
    if IsValid: print("This phone number is valid.")
    else: print("this phone number is not valid")

    print(phonenumbers.PhoneMetadata.load_all())

#run the script
if __name__ == '__main__':
    main()
