import frappe
import csv
import base64
from frappe.utils import get_site_path

@frappe.whitelist()
def download_customer_csv(customer_group=""):
    """
    Fetch all fields from the Customer Doctype dynamically, append POS Invoice items (with status 'Paid'), and export as a CSV file.
    Log each step into a log file at /home/ubuntu/log.txt.
    """
    # Define the log file path
    log_file_path = "/home/ubuntu/log.txt"  # Custom log file location

    # Initialize the log file
    with open(log_file_path, "w") as log_file:
        log_file.write("Starting customer export process...\n")

    # Log function to write messages to the log file
    def log(message):
        with open(log_file_path, "a") as log_file:
            log_file.write(f"{message}\n")

    log("Fetching customer meta data...")
    # Get all fieldnames from the Customer doctype dynamically
    customer_meta = frappe.get_meta("Customer")
    all_fields = [df.fieldname for df in customer_meta.fields if frappe.db.has_column("Customer", df.fieldname)]

    # Ensure "name" (Docname) is included
    if "name" not in all_fields:
        all_fields.insert(0, "name")

    log(f"Fields to include in CSV: {', '.join(all_fields)}")

    # Apply filters if a Customer Group is selected
    filters = {}
    if customer_group:
        filters["customer_group"] = customer_group
        log(f"Filtering customers by customer group: {customer_group}")

    log("Fetching customer data...")
    # Fetch customer data
    customers = frappe.get_all("Customer", fields=all_fields, filters=filters)

    if not customers:
        log("No customers found for the selected filter.")
        frappe.throw("No customers found for the selected filter.")

    log(f"Found {len(customers)} customers.")

    # Fetch POS Invoice items for each customer (only for paid invoices)
    pos_items = {}  # Dictionary to store item counts for each customer
    log("Fetching POS Invoice items for each customer (status: Paid)...")
    for customer in customers:
        log(f"Processing customer: {customer.name}")
        # Get POS Invoices linked to the customer with status 'Paid'
        pos_invoices = frappe.get_all(
            "POS Invoice",
            filters={"customer": customer.name, "status": "Paid"},  # Filter by status
            fields=["name"]
        )
        if pos_invoices:
            log(f"Found {len(pos_invoices)} paid POS Invoices for customer {customer.name}.")
            # Fetch items from each POS Invoice
            for pos_invoice in pos_invoices:
                items = frappe.get_all(
                    "POS Invoice Item",
                    filters={"parent": pos_invoice.name},
                    fields=["item_code", "qty"]
                )
                for item in items:
                    if item.item_code not in pos_items:
                        pos_items[item.item_code] = {}
                    if customer.name not in pos_items[item.item_code]:
                        pos_items[item.item_code][customer.name] = 0
                    pos_items[item.item_code][customer.name] += item.qty or 0
                    log(f"Added {item.qty} of item {item.item_code} for customer {customer.name}.")
        else:
            log(f"No paid POS Invoices found for customer {customer.name}.")

    log(f"Found {len(pos_items)} unique items across all paid POS Invoices.")

    # Add POS Invoice items as columns
    for item_code in pos_items.keys():
        all_fields.append(f"Item: {item_code}")
    log(f"Added {len(pos_items)} item columns to the CSV.")

    # Create a temporary file path for the CSV
    file_path = get_site_path("public", "files", "Customer_List.csv")
    log(f"Writing CSV data to {file_path}...")

    # Write data to CSV
    with open(file_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(all_fields)  # Write header row
        log("CSV header row written.")

        for customer in customers:
            row = [customer.get(field, "") for field in all_fields if not field.startswith("Item: ")]
            for item_code in pos_items.keys():
                row.append(pos_items[item_code].get(customer.name, 0))
            writer.writerow(row)
            log(f"Row written for customer {customer.name}.")

    log("CSV file created successfully.")

    # Read the file content and encode it as base64
    with open(file_path, "rb") as file:
        file_content = file.read()
        encoded_content = base64.b64encode(file_content).decode("utf-8")
    log("CSV file encoded as base64.")

    # Return the file content and name
    log("Returning file content and name to the frontend.")
    return {
        "file_content": encoded_content,
        "file_name": "Customer_List.csv"
    }