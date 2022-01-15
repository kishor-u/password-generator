## Password Generator API 

The API written in Python 3.x generates secure passwords. As input parameters the user must provide
the minimum length, the number of special characters, the number of digits and the number of passwords that shall be created. Then generate the passwords and return them in an array.

### How to Run

- Clone the repo to your system by `git clone https://github.com/kishor-u/password-generator.git`

- Make sure that you have the latest _Python 3.x_ and _Pip 3.x_ installed.

- Open terminal and type `export FLASK_ENV=development && python app.py`

- Your API server will be listening at port `8080`.

- You will be able to hit the API by `http://localhost:8080/password-generator?min_length=20&num_of_special_chars=4&num_of_digits=6&num_of_pass=10` or via CURL 

```shell
curl "http://localhost:8080/password-generator?min_length=20&num_of_special_chars=4&num_of_digits=6&num_of_pass=10"
```

#### Dockerized Setup

Dockerized setup is much classier than manual setup. To achieve this you just have to do this:-

```shell
docker build -t password-generator-api:latest -f Dockerfile .
```

That's it. Now just go and deploy the docker image anywhere you want.

```shell
docker run -d -p 8080:8080 password-generator-api
```

### Examples
```shell
curl "http://localhost:8080/password-generator?min_length=20&num_of_special_chars=4&num_of_digits=6&num_of_pass=10"
{
  "password_array": [
    ",BIi6GCc9118.l,2lS[z",
    "yZ7'-iCa29ku[40"mkQ3",
    "rkXq"'Lv7S8,Vt55P41>",
    "{UL'w766G6/JNU5x`8vb",
    "~nX048}6LET[}1RfoG1h",
    "u7v8VWyw9=p4`64H!cd#",
    "WkVgGAkh09>F]109?O7(",
    "94hupUL-XA16T1>~aK2:",
    "S48LJ?!24Kv5.*z2EjTR",
    "iw@7vTD?8i6szQ17=1;n"
  ]
}
```