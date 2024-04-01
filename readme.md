# Document Management System
## Description:
This Django project provides a Document Management System (DMS) that allows users to manage metadata and upload/download documents. Users can register, upload metadata, upload documents, and retrieve document information.

## Installation and Setup:
1. Clone the repository:
2. Install dependencies:
'''
pip install -r requirements.txt
'''
3. Apply migrations:
'''
python manage.py migrate
'''
4. Run the development server:
'''
python manage.py runserver
'''

## Usage:
- **Register a User:**
  - **Endpoint:** `/register/`
  - **Method:** POST
  - **Parameters:**
    - `email` (string): User's email address
    - `password` (string): User's password
  - **Response:** User registration confirmation or error message if email already exists.

- **Upload Metadata:**
  - **Endpoint:** `/upload_metadata/`
  - **Method:** POST
  - **Parameters:**
    - `name` (string): Name of the metadata
    - `string` (string): Metadata content
  - **Response:** Confirmation message on successful metadata upload or error message if metadata with the same name already exists.

- **Get Metadata:**
  - **Endpoint:** `/get_metadata/`
  - **Method:** GET
  - **Parameters:**
    - `name` (string): Name of the metadata to retrieve
  - **Response:** Metadata information including ID, name, and string.

- **Get All Metadata:**
  - **Endpoint:** `/get_all_metadata/`
  - **Method:** GET
  - **Response:** All metadata stored in the system.

- **Upload Document:**
  - **Endpoint:** `/upload/<str:filename>`
  - **Method:** POST
  - **Parameters:**
    - `file` (file): Document file to upload
  - **Response:** Confirmation message on successful document upload.

- **Get All Documents:**
  - **Endpoint:** `/documents/`
  - **Method:** GET
  - **Response:** List of all documents with their IDs and file URLs.

- **Get Document by Filename:**
  - **Endpoint:** `/document/<str:filename>`
  - **Method:** GET
  - **Parameters:**
    - `filename` (string): Name of the document to retrieve
  - **Response:** Document information including ID, name, and file URL.

## Note:
- All endpoints, except registration, require authentication. Ensure you provide a valid authentication token in your requests.
- Ensure proper error handling on the client side for a smoother user experience.
- This Django project provides a flexible solution for managing documents and associated metadata efficiently. If you have any questions or encounter issues, please contact the project maintainers.