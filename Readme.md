# Invoice Management System

This is a Django application for managing invoices and their details.

## Functionality

- **View Invoices**: Displays a list of invoices along with their details.
- **Add Invoice**: Allows users to add a new invoice along with multiple details.
- **Update Invoice**: Supports updating the invoice information and its associated details.
- **Delete Invoice**: Enables deleting an invoice by its ID.

## Getting Started

### Prerequisites

- Python 3.x
- Django

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/saketh-mallojjala/Django-Restframework.git
   cd Django-Restframework
   
2. **Create and activate a virtual environment:**
   ```bash
    python -m venv venv
    source venv/bin/activate  

3. **Install dependencies:**
    ```bash
       pip install -r requirements.txt
4. **Run migrations:**
    ```bash
        python manage.py migrate
5. **Run the development server:**
    ```bash
       python manage.py runserver
      ```
   Access the application at http://127.0.0.1:8000/

## Usage
- Add Invoice: Visit http://127.0.0.1:8000/addinvoice/ to add a new invoice with details.
- View Invoices: Visit http://127.0.0.1:8000/viewinvoice/ to view all invoices along with their details.
- Update Invoice: Visit http://127.0.0.1:8000/updateinvoice/ to update the details of an existing invoice.
- Delete Invoice: Visit http://127.0.0.1:8000/deleteinvoice/ to delete an existing invoice.
   