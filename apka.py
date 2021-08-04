

# projekt apki, w którą wpisuje co masz w lodówce/spiżarce i losuje Ci jakiś przepis ze strony
# z bibliotek które się przydadzą to na bank webscraping, czyli requests i beautifulsoup
# jakiś framework z interfejsem graficznym, na pewno nie tkinter bo jest brzydki
# pewno biblioteka random, żeby przepis był losowy
# oczywiście biblioteka lxml, bo do beautifulsoup

# najpierw zrobię okienko, potem zadbam o funkcjonalność
import tkinter
import tkinter as tk
import requests
from bs4 import BeautifulSoup
import lxml

# z klasą jest więcej pierdolenia, więc robię samymi funkcjami
recipes_links = []
for page in range(2, 54):
    result = requests.get("https://food52.com/recipes/search?o=newest&page="+str(page)+"&tag=test-kitchen-approved")
    if result.status_code == 200:
        g_cookies = result.cookies.get_dict()
        result = requests.get("https://food52.com/recipes/search?o=newest&page=" + str(page) + "&tag=test-kitchen-approved",
                              headers = headers, cookies = g_cookies)

    website = result.content
    soup = BeautifulSoup(website, "lxml")
    for h3_tag in soup.find_all("h3"):
        a_tag = h3_tag.find("a")
        try:
            recipes_links.append(a_tag.attrs["href"])
        except:
            pass
# h5 consists of recipe ingredients
print(recipes_links)
root = tk.Tk()
root.title("Eat the random")
root.geometry("300x300")
skladnik_var = tk.StringVar()
lista_sklad = []
def submit():
    skladnik = skladnik_var.get()
    lista_sklad.append(skladnik)
    print(lista_sklad)
    skladnik_entry.delete(0, tkinter.END)
def remove():
    lista_sklad.clear()
    print(lista_sklad)
def show():
    root_sklad = tk.Tk()
    root_sklad.title("Ingredients")
    root_sklad.geometry("200x200")
    label_lista = tk.Label(root_sklad, text = lista_sklad)
    label_lista.pack()
    root_sklad.mainloop()
def find_recipe():
    similar = 0
    for x in recipes_links:
        result_1 = requests.get("https://food52.com"+x)
        inside = result_1.content
        soup_find = BeautifulSoup(inside, "lxml")
        for skladnik in lista_sklad:
            if skladnik in soup_find.find_all("h5"):
                similar += 1
            if similar < 4:
                pass
            else:
                print(x)
skladnik_entry = tk.Entry(root, textvariable = skladnik_var, width = 30)
skladnik_entry.place(x = 60, y = 50)

sub_btn = tk.Button(root, text = "Add ingredient", command = submit)
sub_btn.place(x = 70, y = 80)

remove_btn = tk.Button(root, text = "Clear list", command = remove)
remove_btn.place(x = 170, y = 80)

show_btn = tk.Button(root, text = "Show ingredients", command = show)
show_btn.place(x = 60, y = 110)

find_recipe_btn = tk.Button(root, text = "Find recipe")
find_recipe_btn.place(x = 170, y = 110)
root.mainloop()

