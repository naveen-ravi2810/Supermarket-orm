from pydantic import BaseModel, Field
from datetime import  date


class ProductSchema(BaseModel):
    product_name : str = Field(max_length=40, min_length=6)
    product_desc : str = Field(max_length=400, min_length=10)
    product_price : float = Field(gt=0)
    product_tax : float = Field(gt=0, lt=100)
    product_seller_id : int = Field(gt=0)
    product_category : str = Field(min_length=1, max_length=20)


class CustomerSchema(BaseModel):
    customer_name : str = Field(max_length=40, min_length=6)
    customer_phone : int = Field(gt=6000000000, lt=9999999999)
    customer_email : str
    customer_dob : date = Field(lt=date.today())
