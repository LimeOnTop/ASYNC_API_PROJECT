from config import load_config
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from logger import logger
from models.models import User

app = FastAPI()
fake_users = {
    1: {"username": "john_doe", "email": "john@example.com"},
    2: {"username": "jane_smith", "email": "jane@example.com"},
}

templates = Jinja2Templates(directory="../templates")
config = load_config()
app.debug = config.debug


@app.get("/db")
def get_db_info():
    logger.info(f"Connecting to database: {config.db.database_url}")


@app.get("/")
async def root(request: Request):
    """
    Get home page

    :param request: parameter with 'Request' module instance
    :return: html template 'index.html'
    """
    logger.info("Handling request to root endpoint")
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/calculate")
async def calculate(a: int = 5, b: int = 15):
    """
    Get sum of two numbers

    :param a: int - value for first param
    :param b: int - value for second param
    :return: dict - message with sum of two params
    """
    return {"response": a + b}


@app.get("/custom")
async def read_custom_message():
    """
    Get custom message

    :return: dict - message for endpoint '/custom'
    """
    return {"message": "This is a custom message"}


@app.get("/user")
async def get_user_info():
    """
    Get user info

    :return:  attributes of 'user' instance
    """
    user = User(id=1, name="John Duck", age=24)
    return vars(user)


@app.post("/is_adult")
async def adult_check(user: User):
    is_adult = user.age >= 18
    logger.info(f"Current value of parameter is_adult: {is_adult}")
    return "".join(f"Is adult: {is_adult}")


@app.get("/users/{user_id}")
async def get_curr_user_info(user_id: int):
    """
    Get info of current user

    :param user_id: int - user identifier
    :return: current user attributes
    """
    if user_id in fake_users:
        return fake_users[user_id]
    return {"error": "User not found"}


@app.get("/users")
async def get_users_list(limit: int = 10):
    """
    Get info of current user

    :param limit: int - limit of users
    :return: current user attributes
    """
    return dict(list(fake_users.items())[:limit])
