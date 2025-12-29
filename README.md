# Nelson Llanes - Inventory Management System

A Python-based inventory management program that allows users to add, update, remove, and view products in a formatted table.  
The program includes file handling, input validation.

---

## How to Run the Program

### Requirements
- Python 3 installed
- `db.txt` in the same directory (automatically created if missing)

### Command to Run
```bash
python NelsonLlanes_coursework1.py
```

---

## Implemented Features

| Feature | Status |
|---------|---------|
| View inventory in a formatted output | Completed |
| Add items with input validation | Completed |
| Update existing products (name, price, quantity, category, brand) | Completed |
| Remove products by ID | Completed |
| Save changes to `db.txt` automatically | Completed |
| Load inventory when the program starts | Completed |
| Basic exception handling with try/except | Implemented |

---


## Data File Structure (`db.txt`)

```json
{
  "inventory": { ... },
  "categories": [ ... ],
  "brand_info": [ ... ],
  "product_ids": [ ... ]
}
```

The file is automatically created if missing.

---

## Known Limitations

- No advanced search functionality (ID-based only)
- Expiration date is not validated as a real date format
- If `db.txt` is manually edited incorrectly, it may cause JSON load errors. case, delete db.txt
- The program stores data in memory and does not use an external database

---

## Author

Nelson Llanes  
Python Coursework - Inventory Management System
