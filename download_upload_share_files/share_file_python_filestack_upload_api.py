from filestack import Client

api_key = "AonyAQ1TKS5SC083GfNFWz"

client = Client(api_key)
new_link = client.upload(filepath="myfile.txt")

print(new_link.url)