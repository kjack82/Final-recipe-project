import sqlite3 ## import sqlite3


conn = sqlite3.connect('recipes.db') ## connect to sqlite3 database, and creates it if it does not already exist. 
c = conn.cursor()  ## this creates a cursor which will work through any commands or queries sent to database. Important for any data requests below. 

c.execute(''' 
CREATE TABLE IF NOT EXISTS recipes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    prep_time INTEGER NOT NULL,
    rating FLOAT NOT NULL,
    url TEXT NOT NULL,
    image_url TEXT NOT NULL
    )
    ''')  

## use ''' as multiple strings split over different lines. Easier than putting all on one line. 
### Using NOT NULL for those where I want something to be input. 
### use execute to execute the SQL command.

insert_query = '''   
    INSERT INTO recipes (name, category, prep_time, rating, url, image_url)
    VALUES (?, ?, ?, ?, ?, ?)
    '''
## inserting using parameters first, ie code above, rathr than inserting directly to database as will mean over-writing should I need to add more data later). 
## 2 prong approach, insert as query above, then  provide the data below, which can then be inserted. 

initial_data = [
    ("Biscoff Brownies", "Dessert", 40, 10, "https://www.janespatisserie.com/2015/07/18/cookie-butter-brownies/", "https://www.janespatisserie.com/wp-content/uploads/2015/07/IMG_3477-533x800.jpg"),
    ("Chocolate Date Bark", "Dessert", 40, 8, "https://nadiashealthykitchen.com/viral-chocolate-date-bark/", "https://nadiashealthykitchen.com/wp-content/uploads/2023/08/viral-chocolate-date-bark_7-min.jpg"),
    ("Date & Pistachio Rolls", "Snack", 50, 8, "https://nadiashealthykitchen.com/date-pistachio-rolls/", "https://nadiashealthykitchen.com/wp-content/uploads/2023/04/date-pistachio-rolls_4-min.jpg"),
    ("Crunchy Nut & Seed Rounds", "Snack", 40, 7, "https://nadiashealthykitchen.com/crunchy-nut-seed-rounds/", "https://nadiashealthykitchen.com/wp-content/uploads/2023/03/crunchy-nut-seed-rounds_3-min.jpg"),
    ("Sundried Tomato and basil chicken lasagne", "Dinner", 70, 9, "https://www.instagram.com/p/CuPu2B1IKBx/", "https://www.dontgobaconmyheart.co.uk/wp-content/uploads/2023/10/chicken-lasagne-744x955.jpg"),
    ("Roasted Garlic & Tomato Soup", "Lunch", 35, 8, "https://lucyandlentils.co.uk/recipe/easy-roasted-tomato-and-garlic-soup", "https://lucyandlentils.co.uk/wp-content/uploads/2022/11/IMG_7510-1080x1440.jpg"),
    ("Veggie Chilli", "Dinner", 25, 10, "https://www.instagram.com/p/C0RFJJst1Re/", "https://img.jamieoliver.com/jamieoliver/recipe-database/107276751.jpg"),
    ("Slowcoooker Cottage Pie", "Dinner", 7, 9, "https://www.instagram.com/p/C3F-6pQov9e/", "https://richanddelish.com/wp-content/uploads/2022/04/Shepherds-pie-with-cheese-768x1024.jpg"),
    ("Frozen Berry Breakfast Crumble", "Breakfast", 40, 9, "https://www.instagram.com/p/C4U8d0kIXog/", "https://media.istockphoto.com/id/1324086905/photo/berry-fruit-crumble-pie-crumble-fruit-crumble-cobbler-cherry-crumble-berry-fruit-crumb-tart.webp?b=1&s=170667a&w=0&k=20&c=thDqzsROS72OXr23OjgcWdWkfAlB3amC1CMqKepRVeE="),
    ("Chilli & Lentil Hot Pot", "Dinner", 25, 9, "https://lucyandlentils.co.uk/recipe/chilli-lentil-hot-pot", "https://lucyandlentils.co.uk/wp-content/uploads/2018/11/IMG_8116-1080x1620.jpg")
    ("Biscoff Sticky Toffee Pudding", "Dessert", 60, 9, "https://www.janespatisserie.com/2024/06/30/biscoff-sticky-toffee-pudding/", "https://www.janespatisserie.com/wp-content/uploads/2024/06/BiscoffStickyToffeePudding7-2-533x800.jpg"),
    ("Mini Lemon & Raspberry Cheesecake", "Dessert", 180, 9.5, "https://www.janespatisserie.com/2022/08/19/mini-lemon-raspberry-cheesecakes/", "https://www.janespatisserie.com/wp-content/uploads/2022/08/MiniLemonRaspberryCheesecakes10-2.jpg"),
    ("Pistachio & Roasted Strawberry Cake with Salted Honey Whip", "Dessert", 60, 8.5, "https://www.recipebyrosie.com/post/pistachio-and-roasted-strawberry-cake-with-salted-honey-whip", "https://static.wixstatic.com/media/037750_fb9b39b193394464b5b617d52b597750~mv2.png/v1/fill/w_723,h_1093,al_c,q_90,usm_0.66_1.00_0.01,enc_auto/037750_fb9b39b193394464b5b617d52b597750~mv2.png"),
    ("Blueberry Coconut Cake", "Dessert", 80, 9, "https://www.recipebyrosie.com/post/blueberry-coconut-cake", "https://www.recipebyrosie.com/post/blueberry-coconut-cake", "https://static.wixstatic.com/media/037750_6a3e100c8e3744d0ad5db26950cb5e47~mv2.jpg/v1/fill/w_723,h_1085,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/037750_6a3e100c8e3744d0ad5db26950cb5e47~mv2.jpg"),
    ("Potato, Salmon & Leek Bake", "Dinner", 60, 8, "https://www.instagram.com/p/C4gSi9CoC30/", "https://drizzleanddip.com/wp-content/uploads/2020/10/O6A2001.jpg"),
    ("Veggie Broth with Orecchiette", "Lunch", 30, 9, "https://www.deliciouslyella.com/en-us/recipes/nourishing-veggie-broth-with-orecchiette/", "https://images.ctfassets.net/8ffyq0lxv9d2/3GklGaNHaLtdzoc3v9ZuoT/b3e9801502b07b8a849f88f19eb9b0d5/__Safia_Shakarchi_-_Deliciously_Ella_-_17.01.2024_-_14.jpg"),
    ("No Layer Gnocci Lasagne", "Dinner", 80, 9, "https://www.instagram.com/p/C0hgIbyIUVP/", "https://myriadrecipes.com/wp-content/uploads/2024/01/Gnocchi-Lasagne-with-Gochujang-3.png"),
    ("Chicken & Chorizo Paella", "Dinner", 60, 9.5, "https://www.bbcgoodfood.com/recipes/chicken-chorizo-paella", "https://cookingformysoul.com/wp-content/uploads/2023/01/chicken-chorizo-paella-6-min.jpg"),
    ("Brownie Donuts", "Dessert", 60, 10, "https://www.janespatisserie.com/2022/04/25/bronuts/", "https://www.janespatisserie.com/wp-content/uploads/2022/04/Bronuts1-2.jpg"),
    ("Greek Chicken & Lemon Potato Platter", "Dinner", 45, 9, "https://www.instagram.com/p/C7MyGuzowLN/", "https://i2.wp.com/www.downshiftology.com/wp-content/uploads/2023/06/Greek-Lemon-Chicken-5.jpg")
]

try:
    c.executemany(insert_query, initial_data)  ## inserts the query and values in to the database. 
    conn.commit()  ## commits the changes to the database. 
    print("Rows inserted")  ## confirms that this has been done 
except sqlite3.Error as e: ## if errors - these are to be printed. 
    print("Error. Unable to insert rows.")
    
try:
    c.execute('SELECT * FROM recipes')  ##this will retrieve all records from db, from coloumns and rows 
    rows = c.fetchall()  ##bringing up all rows
    for row in rows:  ## ensures it goes through every row 
        print(row)
except sqlite3.Error as e:  ## however if this does not work, error caught and message printed. 
    print("Error. Unable to fetch data")

conn.close  ## close the databsde connection 
### ALWAYS CLOSE DB CONNECTION ONCE COMPLETED A TASK 
