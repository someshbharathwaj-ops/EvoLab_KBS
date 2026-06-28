from pydantic import BaseModel, Field
from .block import Block

class page(BaseModel) :
   """ structural unit of a document 
   """  
   page_number : int = Field(ge=0)
   blocks : list[Block]
