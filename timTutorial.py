from fastapi import FastAPI, Query,HTTPException
from typing import Optional
from pydantic import BaseModel
from fastapi import Path 
app=FastAPI()
class Item(BaseModel):
    name:str
    price:float
    brand:Optional[str]=None
class UpdateItem(BaseModel):
    name:Optional[str]=None
    price:Optional[float]=None
    brand:Optional[str]=None
stock={
    1:{
        "Name":"Ground",
        "Price":"456",
        "Brand":"GG"
        }
}
@app.get("/")
def home():
    return ("First line of code in FastAPI")
@app.get("/pasge")
def pasge():
    return("This is another reloaded page")
@app.get("/inventory/{item_id}")
def inventory(item_id:int = Path(...,description="ID of the item that you want to see"),gt=0,le=1):
    item=stock.get(item_id)
    if item:
        return {"Name is": item["Name"]}
    else:
        return {"Error": "No item"}
@app.get("/get-by-name/{item_id}")
def get_item(*,item_id:int,name:Optional[str]=None,id:int):
    for item_id in stock:
        if stock[item_id]["Name"]==name:
            return stock[item_id]
    return HTTPException(status_code=404,detail="Item not")
@app.post("/create-item/{item_id}")
def create_item(item:Item,item_id:int):
    if item_id in stock:
        return {"Error":"Item there"}
    stock[item_id]=Item
    return stock[item_id]
@app.put("/update-item/{item_id}")
def update_item(item_id:int,item:Item):
    if item_id not in stock:
        return {"Error":"Item not"}
    if item.name!=None:
        stock[item_id].name=item.name
    if item.price!=None:
        stock[item_id].price=item.price
    if item.brand!=None:
        stock[item_id].brand=item.brand
    return stock[item_id]
@app.delete("/delete-item")
def delete_item(item_id:int=Query(...,description="ID of item to delete"),gt=0):
    if item_id not in stock:
        return {"Error":"Item not in "}
    del stock[item_id]
    return {"Successful":"Wow mate"}
 