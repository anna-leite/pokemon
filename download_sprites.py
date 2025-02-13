import urllib.request

def download_image(url, save_as):
    urllib.request.urlretrieve(url, save_as)

# download front images
for i in range (1, 151):
    url = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/" + str(i) + ".png"
    save_as = "front_" + str(i) + ".png"
    download_image(url, save_as)


# download back images
for i in range (1, 151):
    url = "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/" + str(i) + ".png"
    save_as = "back_" + str(i) + ".png"
    download_image(url, save_as)
