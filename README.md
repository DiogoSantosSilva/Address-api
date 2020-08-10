# Address-api
Api for add addresses, just for test purpose

<h2>
Build an image
</h2>

docker build -t flag_name .

<h2>
Run a containser
</h2>

docker run -p 8000:8000 flag_name_or_image_id

<h2>
Example of addres to post
</h2>

{
            "street_name": "Rua teste",
            "number": 55,
            "complement": "teste",
            "neighbourhood": {
                "name": "teste"
            },
            "city": {
                "name": "sao paulo"
            },
            "state": {
                "name": "sao paulo"
            },
            "country": {
                "name": "brasil"
            },
            "zipcode": "13060226",
        }