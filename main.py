# from pydantic import BaseModel, Field ## need this when using sqlite3 and fastapi, not needed if using sql alchemy. Using field and literal to define some of the entries in DB. 
# from typing import Optional, Literal  ## using as some fields will be optional. 

# ##Using pydantic for guaranteeing the data input. Popular when used with fastApi. Parse and validate environment variables. 

# class Recipes(BaseModel):  ##model used to add a new recipe defining the name of each category and the data type required 
#     name: str
#     category: Literal['Breakfast', 'Lunch', 'Dinner', 'Dessert', 'Snack', 'Drink'] ##Using literal so I can define what category can be used 
#     prep_time: Optional[int] = None  ##Using this Optional method allows for this field to be blank when submitted the data 
#     rating: Optional[float] = Field(None, ge=0, le=10) ##using field function to ensure I set limits on what can be entered. Ie it is options, so can have none, ge means >=0, le means <=10
#     url: str  
#     image_url: Optional[str]  
    
# class UpdateRecipes(BaseModel): ## Model used to update a recipe already stored in the database. 
#     name: Optional[str]
#     category: Optional[Literal['Breakfast', 'Lunch', 'Dinner', 'Dessert', 'Snack', 'Drink']]
#     prep_time: Optional[int] = None
#     rating: Optional[float] = Field(None, ge=0, le=10)
#     url: Optional[str]  
#     image_url: Optional[str]  
    
    
    #### commented this out as not required for coding for a static page when using htmx. However 