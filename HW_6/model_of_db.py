'''• Таблица пользователей должна содержать следующие поля: id (PRIMARY KEY), имя, фамилия, адрес электронной почты и пароль.
• Таблица заказов должна содержать следующие поля: id (PRIMARY KEY), id пользователя (FOREIGN KEY), id товара (FOREIGN KEY), дата заказа и статус заказа.
• Таблица товаров должна содержать следующие поля: id (PRIMARY KEY), название, описание и цена.
'''
from datetime import datetime
import databases
import sqlalchemy as sa

DATABASE_URL = "sqlite:///store.db"

database = databases.Database(DATABASE_URL)
metadata = sa.MetaData()

users = sa.Table(
    "users",
    metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("first_name", sa.String(80)),
    sa.Column("last_name", sa.String(80)),
    sa.Column("e-mail", sa.String(80)),
    sa.Column("password", sa.String(20)),
)
orders = sa.Table(
    "orders",
    metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("user_id", sa.Integer, sa.ForeignKey('users.id'), nullable=False),
    sa.Column("product_id", sa.Integer, sa.ForeignKey('products.id'), nullable=False),
    sa.Column("date", sa.String(40), nullable=False, default=datetime.now().strftime("%d/%m/%y, %H:%M:%S"),
              onupdate=datetime.now().strftime("%d/%m/%y, %H:%M:%S")),
    sa.Column("status", sa.String(20), nullable=False, server_default="Заказ принят")
)

products = sa.Table(
    "products",
    metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("title", sa.String(40)),
    sa.Column("description", sa.String(1000)),
    sa.Column("price", sa.Float),
)


engine = sa.create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

metadata.create_all(engine)