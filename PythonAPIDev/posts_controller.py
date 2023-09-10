import logging
from fastapi import FastAPI, Response, status, HTTPException
from fastapi.responses import JSONResponse
import uvicorn
import model as mdl
import posts_repository as myr


logger = logging.getLogger(__name__)

# name of application
app = FastAPI()

my_posts = {
                0: mdl.Post(title="top beaches in italy", content="description of beaches", rating=3, postType=mdl.PostType.TRAVEL),
                1: mdl.Post(title="favorite food", content="pizza", published=False, rating=6, postType=mdl.PostType.FOOD)
} 
     

# path operation = route
# @ = decorator. turns method into endpoint
@app.get("/", status_code=status.HTTP_200_OK)
async def root():
    return {"message": "Hello Humans"}

@app.get("/v1/posts", status_code=status.HTTP_200_OK) # status here = default path operation
async def get_posts():
    if not my_posts:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f"get: no posts found")  

    return my_posts

@app.get("/v1/posts/{id}", status_code=status.HTTP_200_OK)
def get_post(id: int) -> mdl.Post: # : int -> validates request param is of type int and casts
    if id not in my_posts:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f"get with id: {id} was not found")        
    
    return my_posts[id]

    # return JSONResponse(headers={"location": "Nothing"},
    #                     content={"data": my_posts[id]},
    #                     media_type="application/JSON")
    

# in plural is standard API convention
@app.post("/v1/posts", status_code=status.HTTP_200_OK)
# async def create_posts(payload: dict = Body(...)): # converting body to dict and storing in payload variable
async def create_posts(new_posts: mdl.Post): # using pydantic, data is automatically validated 
    print (new_posts.dict()) # prints to logs
    try:
        id = len(my_posts)
        my_posts[id] = new_posts
        # raise Exception('This is the exception you expect to handle')
        return new_posts.dict()
    
    except Exception:
        logger.warning('No Insert', exc_info=True)
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail=f"Insert Failed")       

@app.put("/v1/posts/{id}", status_code=status.HTTP_200_OK) 
async def update_post(id: int, post: mdl.Post):

    if id not in my_posts:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f"update with id: {id} was not found")        

    my_posts[id] = post
    return {"msg": "Post Updated", "data": my_posts[id]}

@app.delete("/v1/posts/{id}", status_code=status.HTTP_204_NO_CONTENT) 
async def delete_post(id: int):

    if id not in my_posts:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail=f"delete with id: {id} was not found")        

    my_posts.pop(id)
        

# __main__ executes if run directly not imported
# For debugging with breakpoints in VS Code
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)