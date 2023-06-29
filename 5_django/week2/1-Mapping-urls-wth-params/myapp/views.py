from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def menuitems(request, dish):
    items = {
        'pasta': "Pasta is a type of food made from a dough consisting of flour, water, and sometimes eggs, which is typically cooked by boiling and then served with various sauces, vegetables, or meats. It is a staple in Italian cuisine and enjoyed worldwide for its versatility and comforting taste.",
        'falafel': 'Falafel is a popular Middle Eastern dish made from ground chickpeas or fava beans, mixed with herbs, spices, and onions. It is typically formed into small patties or balls and then deep-fried or baked, resulting in a crispy exterior and a soft, flavorful interior.',
        'cheesecake': "Cheesecake is a rich and creamy dessert made with a crust typically made from crushed cookies or graham crackers, and a filling consisting of cream cheese, sugar, and eggs. It is often flavored with vanilla or other extracts and can be topped with various fruits, chocolate, or caramel for added sweetness and visual appeal."

    }
    description = items[dish]
    return HttpResponse(f"<h2> {dish} </h2>" + description)

def drinks(request, drink_name):
    drink = {
        'mocha': "Mocha is a beverage that combines espresso and chocolate, creating a flavorful and aromatic drink. It typically consists of a shot of espresso, steamed milk, chocolate syrup or cocoa powder, and sometimes whipped cream or chocolate shavings for garnish. Mocha is loved for its delightful blend of coffee and chocolate flavors.",
        'tea': 'Tea is a widely consumed beverage made by infusing dried leaves from the Camellia sinensis plant in hot water. With a variety of types, including black, green, white, and herbal teas, it offers a range of flavors and health benefits. Tea can be enjoyed plain or with additions like sugar, honey, milk, or lemon, and is known for its soothing and invigorating properties.',
        'lemonade': "Lemonade is a refreshing beverage made by mixing freshly squeezed lemon juice, water, and sugar. It is often served chilled and can be customized with additional ingredients like mint leaves, fruit slices, or carbonated water. Lemonade is appreciated for its tart and tangy taste, making it a popular choice to quench thirst on hot days."

    }
    choice_of_drink = drink[drink_name]
    return HttpResponse(f"<h2> {drink_name} </h2>" + choice_of_drink)

# def home(request):
#     path = request.path
#     scheme = request.scheme
#     method = request.method
#     address = request.META['REMOTE_ADDR']
#     user_agent = request.META['HTTP_USER_AGENT']
#     path_info = request.path_info
#     response = HttpResponse()
#     response.headers['Age'] = 20
#     response.headers['Isim'] = "Ertan"

#     msg = f"""
#             <br>Path:{path}
#             <br>Address:{address}
#             <br>Scheme:{scheme}
#             <br>Method:{method}
#             <br>User agent:{user_agent}
#             <br>Path info:{path_info}
#             <br>Response header:{response.headers}
#             """
#     return HttpResponse(msg, content_type="text/html", charset='utf-8')
