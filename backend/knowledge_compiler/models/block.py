from pydantic import BaseModel,Field,field_validator
from uuid import UUID



class Block(BaseModel) :
    """
    Base model representing the smallest structural unit
    extracted from a document page.
    """
    block_id : UUID
    content : str 
    page_number : int =  Field(ge=1) 
    block_order : int =  Field(ge=0)
    @field_validator("content")
    def validate_content(cls, value:str)->str:
       value = value.strip()

       if not value :
          raise ValueError("Content cannot be empty")

       return value


class HeadingBlock(Block) :
    """
    Represents a document heading.
    """
    heading_level : int = Field(ge=1)



class ParagraphBlock(Block) :
    """
    Represents a normal paragraph.
    """
