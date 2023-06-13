import requests

url = 'https://mirdit.bitrix24.ru/bitrix/services/main/ajax.php?action=crm.site.form.fill'

headers = {
    'Accept': '*/*',
    'Connection': 'keep-alive',
    'Host': 'mirdit.bitrix24.ru'
}

payload = {
    'id':["4"],
    'sec':["5ly97x"],
    'LEAD_NAME':["dsa"],
    'LEAD_LAST_NAME':["asd"],
    'LEAD_PHONE':["+678-48764-78-46-78"],
    'LEAD_EMAIL':["sdf@fsd.fgyhj"],
    'LEAD_COMMENTS':["asd"]
}

response = requests.request("POST", url, headers=headers, data=payload)

assert response.status_code == 200

print(response.status_code)
print(response.json())
