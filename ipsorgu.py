import requests
print ('''
Coder : MrXBlack
Telegram : @KaosMrx
Instagram : @sayinbyman
''')
def kori():
	ip = input('İp Adresini Giriniz: ')
	url = f'http://ip-api.com/json/{ip}'
	res = requests.get(url).json()
	country = res['country']
	countryCode = res['countryCode']
	region = res['region']
	city = res['city']
	zip = res['zip']
	timezone = res['timezone']
	status = res['status']
	isp = res['isp']
	regionName = res['regionName']
	print('-----------------------------------------')
	print(f'Ülke : {country}')
	print(f'ÜlkeKodu : {countryCode}')
	print(f'Bölge : {region}')
	print(f'Şehir : {city}')
	print(f'zip : {zip}')
	print(f'SaatDilimi : {timezone}')
	print(f'Hat Türü: {isp}')
	print(f'Bölgeİsmi : {regionName}')
	print('--------------------------------------------')
kori()
