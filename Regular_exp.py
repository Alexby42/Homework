import re
def extract_image_links(link):
    links = []
    regular = r'(http|https)(://)([0-9a-zA-z.]+)(/)([a-z0-9]+)\.(jpg|png|gif)'
    search = re.finditer(regular, link)
    for found in search:
        links.append(found[0])
    return links
sample_html = ("<img src='https://example.com/image1.jpg'> <img src='http://example.com/image2.png'>"
               "<img src='https://example.com/image3.gif'>")
image_links = extract_image_links(sample_html)
if image_links:
    for image_link in image_links:
        print(image_link)
else:
    print("Нет ссылок с картинками в HTML тексте.")