country_capital = open("file.txt", "a")

country_capital.write("\n Maldives - Male")
country_capital.close()

country_capital = open("file.txt", "w")
country_capital.write("Sri Lanka - Colombo")
country_capital.write("\nNepal - Kathmandu")
country_capital.close()

cafe_menu = open("cafe_menu.txt", "w")
cafe_menu.write("Chowmein - 100")
cafe_menu.write("\nMomo - 120")
cafe_menu.close()