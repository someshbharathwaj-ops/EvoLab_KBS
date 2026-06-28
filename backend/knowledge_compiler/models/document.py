from uuid import  UUID
from .page import Page
from .enums import DocumentType
from pydantic import Field , BaseModel,field_validator 
from pathlib import Path

class Document(BaseModel) :
    document_id : UUID
    document_type : DocumentType
    source_path : Path
    pages : list[Page]
    @field_validator("source_path")
    def validate_content(cls, value:str)->str:
       value = value.strip()

       if not value :
          raise ValueError("Content cannot be empty")

       return value