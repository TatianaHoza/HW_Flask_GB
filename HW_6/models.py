''' Таблица пользователей должна содержать следующие поля: id (PRIMARY KEY), имя, фамилия, адрес электронной почты и пароль.
• Таблица заказов должна содержать следующие поля: id (PRIMARY KEY), id пользователя (FOREIGN KEY), id товара (FOREIGN KEY), дата заказа и статус заказа.
• Таблица товаров должна содержать следующие поля: id (PRIMARY KEY), название, описание и цена.'''

from pydantic import BaseModel, Field


class UserIn(BaseModel):
    first_name: str = Field(max_length=40)
    last_name: str = Field(max_length=40)
    email: str = Field(max_length=80)
    password: str = Field(min_length=20)


class User(BaseModel):
    id: int
    first_name: str = Field(max_length=40)
    last_name: str = Field(max_length=40)
    email: str = Field(max_length=80)
    password: str = Field(min_length=20)


class OrderIn(BaseModel):
    status: str = Field(default="Заказ принят")


class Order(BaseModel):
    id: int
    user_id: int = Field(foreign_key=True)
    product_id: int = Field(foreign_key=True)
    date: str
    status: str = Field(default="Заказ принят")



class ProductIn(BaseModel):
    title: str = Field(max_length=40)
    description: str = Field(max_length=1000)
    price: float = Field(gt=0, le=10000)


class Product(BaseModel):
    id: int
    title: str = Field(max_length=40)
    description: str = Field(max_length=1000)
    price: float = Field(gt=0, le=10000)


