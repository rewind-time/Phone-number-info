import phonenumbers
from phonenumbers import timezone
from phonenumbers import geocoder
from phonenumbers import carrier
import pyautogui

my_ph = pyautogui.prompt('Enter a phone number: ')
ph = phonenumbers.parse(my_ph)
format = phonenumbers.PhoneNumberFormat.INTERNATIONAL
formatted = phonenumbers.format_number(ph, format)
Carrier = carrier.name_for_number(ph, None)
timeZone = timezone.time_zones_for_number(ph)
print('Phone: ', formatted)
print('Detail: ', ph)
print('Time zone: ', timeZone)
print('Carrier: ', Carrier)
# print(phonenumbers.PhoneMetadata.load_all())
