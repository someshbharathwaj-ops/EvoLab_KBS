from pydantic import BaseModel, Field
from .block import Block

class Page(BaseModel) :
   """ Represents a single physical page containing
an ordered collection of document blocks.
   """  
   page_number : int = Field(ge=0)
   blocks : list[Block]
