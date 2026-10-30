from urllib.request import Request, urlopen


url = "https://www.yahoo.com"
request = Request(url, headers={"User-Agent": "Mozilla/5.0"})

with urlopen(request, timeout=15) as response:
    page = response.read().decode(
        response.headers.get_content_charset() or "utf-8",
        errors="replace",
    )

print(page)