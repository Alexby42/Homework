from fastapi import FastAPI, Path
from typing import Annotated
app = FastAPI()
@app.get('/')
async def GetRootPage():
    return 'Главная страница'
@app.get('/user/admin')
async def GetAdminPage():
    return 'Вы вошли как администратор'
@app.get('/user/{userID}')
async def GetUserID(userID: Annotated[int, Path(ge=1, le=100, description='Enter your id', examples='43')]):
    return f'Вы вошли как пользователь №{userID}'
@app.get('/user/{username}/{age}')
async def GetUserInfo(username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username',
                                                   examples='UrbanUser')], age: Annotated[int, Path(ge=18, le=120,
                                                                                                  description=
                                                                                                  'Enter age',
                                                                                                  examples='24')]):
    return f'Информация о пользователе. Имя {username}, возраст {age}'
