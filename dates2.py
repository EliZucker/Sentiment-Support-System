from gdatabase import google_db

gdb = google_db()

response = gdb.get_data_from_all(query=lambda x: x)

total = 0
for key in response:
    total += len(response[key])
    print(key, len(response[key]))

print('total:', total)
