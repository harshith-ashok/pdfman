from pydantic import BaseModel


class PDFRequest(BaseModel):
    filename: str
