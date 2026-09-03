import sqlite3

DB_NAME = "customers.db"

def create_database():
    """Create the customers table if it does not already exist."""

    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            phone TEXT
        )
    """)

    connection.commit()
    connection.close()

def add_customer(name: str, email: str, phone: str = ""):
    """Add a new customer to the database."""

    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO customers (name, email, phone)
            VALUES (?, ?, ?)
            """,
            (name, email, phone)
        )

        connection.commit()

        return {
            "id": cursor.lastrowid,
            "name": name,
            "email": email,
            "phone": phone
        }

    except sqlite3.IntegrityError:
        raise ValueError(
            "A customer with this email already exists."
        )

    finally:
        connection.close()

def list_customers():
    """Return all customers from the database."""

    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute(
        "SELECT id, name, email, phone FROM customers"
    )

    customers = cursor.fetchall()

    connection.close()

    return [
        {
            "id": customer[0],
            "name": customer[1],
            "email": customer[2],
            "phone": customer[3]
        }
        for customer in customers
    ]

def get_customer(customer_id: int):
    """Find a customer by ID."""

    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT id, name, email, phone
        FROM customers
        WHERE id = ?
        """,
        (customer_id,)
    )

    customer = cursor.fetchone()

    connection.close()

    if customer is None:
        raise ValueError("Customer not found.")

    return {
        "id": customer[0],
        "name": customer[1],
        "email": customer[2],
        "phone": customer[3]
    }

def delete_customer(customer_id: int):
    """Delete a customer by ID."""

    connection = sqlite3.connect(DB_NAME)
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM customers WHERE id = ?",
        (customer_id,)
    )

    connection.commit()

    deleted = cursor.rowcount

    connection.close()

    if deleted == 0:
        raise ValueError("Customer not found.")

    return f"Customer {customer_id} deleted successfully."

if __name__ == "__main__":
    create_database()
    print("Database created successfully.")