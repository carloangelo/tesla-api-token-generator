# tesla-api-token-generator
Generates tesla api tokens using tesla credentials

**Requires Python3**

## Run
```python token_generator.py <username> <password>```

## Alternative Method -- use curl

Replace **TESLA_USERNAME** and **TESLA_PASSWORD**

```
curl -X POST -H "Cache-Control: no-cache" -H "Content-Type: multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW" -F "grant_type=password" -F "client_id=e4a9949fcfa04068f59abb5a658f2bac0a3428e4652315490b659d5ab3f35a9e" -F "client_secret=c75f14bbadc8bee3a7594412c31416f8300256d7668ea7e6e7f06727bfb9d220" -F "email=TESLA_USERNAME" -F "password=TESLA_PASSWORD" "https://owner-api.teslamotors.com/oauth/token"
```
