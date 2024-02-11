import requests
from bs4 import BeautifulSoup

# url = "https://uk.wikipedia.org/w/index.php?title=Категорія:Жіночі_імена&pagefrom=Феофанія+%28значення%29#mw-pages"
#
# header = {
#     "Accept": "*/*",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
# }
#
# req = requests.get(url, headers=header)
# src = req.text
#
# with open("woman_names3.html", "w") as file:
#     file.write(src)

# with open("woman_names.html") as file:
#     scr = file.read()
#
# soup = BeautifulSoup(scr, "lxml")
#
# table_head = soup.find_all("table", class_="wikitable")
# results = []
# for trs in table_head:
#     trs = trs.find("tbody").find_all("tr")
#     for tds in trs:
#         tds = tds.find("td")
#         a = tds.find("a")
#         if a is not None:
#             results.append(a.text)
#         # for a in tds:
#         #     a = a.find("a")
#         #     print(a)
#         #     if a is not None:
#         #         print(a.text)
#
# print(results)
#
# file = open("woman_names.txt", "w", encoding="utf-8")
# for i in range(len(results)):
#     file.write(results[i]+ ",")
# # print(tds)
# # print(table_head)
#--------------------------------------------------------
#
# with open("woman_names3.html") as file:
#     scr = file.read()
#
# soup = BeautifulSoup(scr, "lxml")
#
# table_head = soup.find_all("div", class_="mw-category-group")
# result = []
#
# for ul in table_head:
#     ul = ul.find_all("ul")
#     for li in ul:
#         li = li.find_all("li")
#         for a in li:
#             a = a.find_all("a")
#             for t in a:
#                 result.append(t.text)
# #
# print(result)
#
# results = []
# for i in range(len(result)):
#     a = result[i].split(" (ім'я)")
#     for j in range(len(a)):
#         results.append(a[j])
#
# full_result = []
#
# for i in range(len(results)):
#     a = results[i].split(" (значення)")
#     for j in range(len(a)):
#         full_result.append(a[j])
#
# print(full_result)
#
# file = open("woman_names.txt", "w", encoding="utf-8")
#
# for i in range(len(full_result)):
#     file.write(full_result[i] + " ")

# ----------------------------------------------------


# for div in table_head:
#     div = div.find_all('div')
#     for li in div:
#         li = li.find_all("li")
#         for a in li:
#             a = a.find_all("a")
#             for t in a:
#                 result.append(t.text)

# print(result)
# for i in range(len(result)):
#     if result[i] == "Яснолик":
#         # print(i)

# results = result[30:256]
# print(results)
# file = open("man_names.txt", "w", encoding="utf-8")
# for i in range(len(results)):
#     file.write(results[i] + ",")

# print(table_head)

# file = open("man_names.txt", "r", encoding="utf-8")
# # result = []
# result = file.read()
# results = result.split(",")
#
# print(results)



# with open("man_names2.html") as file:
#     scr = file.read()

# soup = BeautifulSoup(scr, "lxml")
