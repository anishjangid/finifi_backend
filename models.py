from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class Invoice(BaseModel):
    vendor_name: str
    invoice_number: str
    status: str  # Dropdown values can be validated in the API logic
    net_amount: float
    invoice_date: datetime
    due_date: datetime
    department: str
    po_number: Optional[str] = None
    created_time: datetime = Field(default_factory=datetime.utcnow)
    created_date: datetime = Field(default_factory=datetime.utcnow)