from fastapi import FastAPI, HTTPException
from models import Invoice
from database import invoice_collection
from bson import ObjectId
from datetime import datetime

app = FastAPI()

# Helper function to convert MongoDB ObjectId to string
def invoice_serializer(invoice) -> dict:
    return {
        "id": str(invoice["_id"]),
        "vendor_name": invoice["vendor_name"],
        "invoice_number": invoice["invoice_number"],
        "status": invoice["status"],
        "net_amount": invoice["net_amount"],
        "invoice_date": invoice["invoice_date"],
        "due_date": invoice["due_date"],
        "department": invoice["department"],
        "po_number": invoice.get("po_number"),
        "created_time": invoice["created_time"],
        "created_date": invoice["created_date"],
    }

# Create an invoice
@app.post("/invoices/")
async def create_invoice(invoice: Invoice):
    invoice_dict = invoice.dict()
    result = invoice_collection.insert_one(invoice_dict)
    if result.inserted_id:
        return {"message": "Invoice created successfully", "id": str(result.inserted_id)}
    raise HTTPException(status_code=500, detail="Failed to create invoice")

# Fetch all invoices
@app.get("/invoices/")
async def get_invoices():
    invoices = invoice_collection.find()
    return [invoice_serializer(invoice) for invoice in invoices]

# Fetch a single invoice by ID
@app.get("/invoices/{invoice_id}")
async def get_invoice(invoice_id: str):
    invoice = invoice_collection.find_one({"_id": ObjectId(invoice_id)})
    if invoice:
        return invoice_serializer(invoice)
    raise HTTPException(status_code=404, detail="Invoice not found")

# Delete an invoice by ID
@app.delete("/invoices/{invoice_id}")
async def delete_invoice(invoice_id: str):
    result = invoice_collection.delete_one({"_id": ObjectId(invoice_id)})
    if result.deleted_count == 1:
        return {"message": "Invoice deleted successfully"}
    raise HTTPException(status_code=404, detail="Invoice not found")