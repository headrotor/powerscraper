from urllib.request import urlopen
url = "https://poweroutage.us/area/utility/380"
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")
print(html)
