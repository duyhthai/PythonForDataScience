flask --app server --debug run

curl -X GET -i -w '\n' localhost:5000/data

curl -X POST -i -w '\n'   --url http://localhost:5000/person   --header 'Content-Type: application/json'   --data '{
        "id": "4e1e61b4-8a27-11ed-a1eb-0242ac120002",
        "first_name": "John",
        "last_name": "Horne",
        "graduation_year": 2001,
        "address": "1 hill drive",
        "city": "Atlanta",
        "zip": "30339",
        "country": "United States",
        "avatar": "http://dummyimage.com/139x100.png/cc0000/ffffff"
}'

curl -X GET -i -w '\n' localhost:5000/person/4e1e61b4-8a27-11ed-a1e
b-0242ac120002

curl -X GET -i -w '\n' localhost:5000/count

curl -X DELETE -i localhost:5000/person/66c09925-589a-43b6-9a5d-d1601cf53

curl -X GET -i -w '\n' localhost:5000/find_person?q=Tanya
