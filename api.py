from fastapi import FastAPI
from fastapi import Request, Form ## need to import this when using FastApi and as will have HTTP exceptions, this needs to be imported too. 
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates ## Using jinja2 template to separate html from python code
import sqlite3  ## as using sqlite3
##  from typing import List ## use this to import List from typing module. Not using now as code changed. 
# from main import Recipes, UpdateRecipes ## import models from the main page. 
from fastapi.staticfiles import StaticFiles ## importing static files to serve static files, as using html and css, this is required from fastapi


app = FastAPI()  ## app to run using fastapi - is required for FastApi to run. 
templates = Jinja2Templates(directory="templates") ##this line required to use jinja2templates. Makes reference to the html file which is stored within the templates direcory. 

app.mount("/static", StaticFiles(directory="static"), name="static") ##this assigns an url which will llow http requests 


def get_db_connection():  ## this creates a connection to the db 
    conn = sqlite3.connect('recipes.db')
    conn.row_factory = sqlite3.Row # allows access to columns by name, like accessing dictionary
    return conn ##returns the connection object. 

@app.get("/", response_class=HTMLResponse)  ## GET request for all recipes in list
async def get_recipes(request: Request):  #function created, no arguements required as not changing the state. 
    conn = get_db_connection() #connection to db 
    c = conn.cursor() #sets variable c to connection cursor
    c.execute('SELECT * FROM recipes') #command to select all from recipes database 
    recipes = c.fetchall() ##fetch and display all rows within database. 
    conn.close() #close connection 
    return templates.TemplateResponse("index.html", {"request": request, "recipes": recipes}) ##allows for the response via html using template


@app.post("/add_recipe/") ##post/add request for a new recipe to be added. Second line of code relates to the specifcs of the form to be displayed on the front end in terms of categories. 
async def add_recipe(name: str = Form(...), category: str = Form(...), prep_time: int = Form(...), rating: float = Form(...), url: str = Form(...), image_url: str = Form(...)):
    # print(f"Received data: name={name}, category={category}, prep_time={prep_time}, rating={rating}, url={url}, image_url={image_url}") not required, was part of test
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('''
        INSERT INTO recipes (name, category, prep_time, rating, url, image_url)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (name, category, prep_time, rating, url, image_url)) ##add all of the listed data fields
    conn.commit() ##commit changes to DB 
    conn.close() ##close connection 
    return "<div>Recipe successfully added</div>" ##this response will show on front end as a message to confirm added successfully. 

@app.delete("/delete_recipe/{recipe_id}") ## delete request
async def delete_recipe(recipe_id: int): 
    conn = get_db_connection() 
    c = conn.cursor()
    c.execute('DELETE FROM recipes WHERE id = ?', (recipe_id,)) #execute deletion 
    conn.commit() #commit changes
    conn.close() #close connection 
    return "<div>Recipe successfully deleted</div>" ##this response will show in front end to confirm deleted successfully. 

# @app.get("/recipes/{recipe_id}", response_class=HTMLResponse) ## additional get request to fetch one recipe only 
# async def get_recipe(recipe_id: int, request: Request): 
#     conn = get_db_connection()
#     c = conn.cursor()
#     c.execute('SELECT * FROM recipes WHERE id=?', (recipe_id,))
#     recipe = c.fetchone() ## display one recipe
#     conn.close()
#     # Render edit form
#     edit_form = f"""
#         <form id="edit-form-{recipe_id}" hx-put="/recipe/{recipe_id}" hx-target="#recipe-{recipe_id}" hx-swap="outerHTML">
#             <label>Name:</label>
#             <input type="text" name="name" value="{'name'}">
#             <label>Category:</label>
#             <input type="text" name="category" value="{'category'}">
#             <label>Prep Time (minutes):</label>
#             <input type="number" name="prep_time" value="{'prep_time'}">
#             <label>Rating (out of 10):</label>
#             <input type="number" name="rating" value="{'rating'}">
#             <label>Link to website:</label>
#             <input type="url" name="url" value="{'url'}">
#             <label>Image URL:</label>
#             <input type="url" name="image_url" value="{'image_url'}">
#             <button type="submit">Save changes to recipe</button>
#         </form>
#     """ ##above detail relates to the form to be displayed on the front end, and correlates to all the data in the database. 
#     return HTMLResponse(content=edit_form, status_code=200)


@app.put("/recipes/{recipe_id}", response_class=HTMLResponse)  ##edit request
def update_item(recipe_id: int, request: Request):
    conn = get_db_connection()
    c = conn.cursor()
    name = request.form.get('name') ##lists all columns of database 
    category = request.form.get('category')
    prep_time = request.form.get('prep_time')
    rating = request.form.get('rating')
    url = request.form.get('url')
    image_url = request.form.get('image_url')
    
    c.execute('''
            UPDATE recipes
            SET name=?, category=?, prep_time=?, rating=?, url=?, image_url=?
            WHERE id=?
            ''', (name, category, prep_time, rating, url, image_url)) ##to execute changes to the database 
    conn.commit() ##commit changes
    conn.close() ##close connection
    return {"message": "Recipe updated successfully"}
    