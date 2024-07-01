from fastapi import FastAPI, Request, Form ## need to import this when using FastApi and as will have HTTP exceptions, this needs to be imported too. 
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
import sqlite3  ## as using sqlite3
from typing import List ## use this to import List from typing module. 
# from main import Recipes, UpdateRecipes ## import models from the main page. 
from fastapi.staticfiles import StaticFiles


app = FastAPI()  ## app to run using fastapi - is required for FastApi to run. 
templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")


def get_db_connection():  ## this creates a connection to the db 
    conn = sqlite3.connect('recipes.db')
    conn.row_factory = sqlite3.Row # allows access to columns by name, like accessing dictionary
    return conn ##returns the connection object. 

@app.get("/", response_class=HTMLResponse)  ## GET request for all recipes in list
async def get_recipes(request: Request):  #function created, no arguements required as not changing the state. 
    conn = get_db_connection() #connection to db 
    c = conn.cursor() #sets variable c to connection cursor
    c.execute('SELECT * FROM recipes') #command to select all from recipes database 
    recipes = c.fetchall() ##fetch all rows which has already been set above using conn.row_factory
    conn.close() #close connection 
    return templates.TemplateResponse("index.html", {"request": request, "recipes": recipes})


@app.post("/add_recipe/")
async def add_recipe(name: str = Form(...), category: str = Form(...), prep_time: int = Form(...), rating: float = Form(...), url: str = Form(...), image_url: str = Form(...)):
    print(f"Received data: name={name}, category={category}, prep_time={prep_time}, rating={rating}, url={url}, image_url={image_url}")
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('''
        INSERT INTO recipes (name, category, prep_time, rating, url, image_url)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (name, category, prep_time, rating, url, image_url))
    conn.commit()
    conn.close()
    return JSONResponse({"status": "Recipe Successfully Added"})

# @app.get("/recipes/{recipe_id}", response_model=Recipes)  
# async def get_recipe(id: int ): # = Path(..., description="The ID of the recipe you want to view"))
#     conn = get_db_connection()
#     c = conn.cursor()
#     c.execute('SELECT * FROM recipes WHERE id = ?', (recipe_id,))
#     recipe = c.fetchone()
#     conn.close()
#     if recipe_id is None:
#         raise HTTPException(status_code=404, detail="Recipe not found") #error message raised 
#     return dict(recipe) #simple convertion to a dictionary required, as no changes are being made. 


# @app.get("/search_recipe", response_model=List[Recipes]) ##get function to search by name 
# async def get_recipe_by_search(request: Request, search: str = Query("", alias="search")):
#     conn = get_db_connection()
#     c = conn.cursor()
    
#     if search: 
#         query = f"%{search}%"
#         c.execute("SELECT * FROM recipes WHERE name = LIKE ?' OR category LIKE ?", (query, query))
#     else:
#         c.execute("SELECT * FROM recipes")
        
#     recipes = c.fetchall()
#     conn.close()
#     return templates.TemplateResponse("index.html", {"request": request, "recipes": recipes})

    # if not recipes: ##if no recipe
    #     raise HTTPException(status_code=404, detail="No recipe matching this name") ##raise exception 
    # return [dict(recipe) for recipe in recipes] ##returns dictionary response 
    

# @app.post("/recipes/{recipe_id}", response_model=Recipes) ##update receipe 
# async def update_recipe(request: Request, recipe_id: int, name: str = Form(...), category: str = Form, prep_time: int = Form, rating: float = Form, url: str = Form, image_url: str = Form):
#     conn = get_db_connection()
#     c = conn.cursor()
#     c.execute('UPDATE items SET name = ?, category = ?, prep_time = ?, rating = ?, url = ?, image_url = ?ecipes WHERE id = ?',(name, category, prep_time, rating, url, image_url)) 
#     if c.rowcount == 0:
#         raise HTTPException(status_code=404, detail="Unable to find recipe")
#     conn.commit()
#     c.execute("SELECT * FROM recipes")
#     recipes = c.fetchall()
#     conn.close
    
    
#     recipe = c.fetchone()
#     if recipe is None: #if no recipe
#         conn.close()
#         raise HTTPException(status_code=404, detail="Recipe not found") #raise exception 

#     updated_data = {key: value for key, value in update.dict().items() if value is not None}
#     set_clause = ", ".join([f"{key} = ?" for key in updated_data.keys()])
#     c.execute(f'UPDATE recipes SET {set_clause} WHERE id = ?', (*updated_data.values(), recipe_id))
#     conn.commit()
#     conn.close()
#     return {**dict(recipe), **updated_data} ##this is used to merge two dictionaries. dict(recipe) relates to original db, updated data them updated info. Will allow an updated version 
# #cnverts row (recipe) to a disctionary. ** used to open the key value pairsnthen creates a new dictionary whilst merging the two. 


@app.delete("/delete_recipe/{recipe_id}")
async def delete_recipe(recipe_id: int):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('DELETE FROM recipes WHERE id = ?', (recipe_id,)) #otherwise execute deletion 
    conn.commit() #commit changes
    conn.close() #close connection 
    return JSONResponse({"status": "Recipe successfully deleted"})

