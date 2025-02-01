import json
import frappe
import logging
from frappe import qb, scrub
from frappe.desk.reportview import get_filters_cond, get_match_cond
from frappe.query_builder import Criterion, CustomFunction
from frappe.query_builder.functions import Locate
from frappe.utils import nowdate, unique
from pypika import Order
import erpnext
from erpnext.stock.get_item_details import _get_item_tax_template

# Configure logging
LOG_FILE = "/home/ubuntu/log.txt"
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

@frappe.whitelist()
@frappe.validate_and_sanitize_search_inputs
def school_query(doctype, txt, searchfield, start, page_len, filters, as_dict=False):
    doctype = "School"  # Ensure we're querying the correct doctype
    conditions = []

    fields = ["name", "school_name"]  # Include school_name in the query

    try:
        searchfields = frappe.get_meta(doctype).get_search_fields()
        searchfields = " or ".join(field + " like %(txt)s" for field in searchfields)

        query = """SELECT {fields} FROM `tabSchool`
            WHERE docstatus < 2
                AND ({scond})
            ORDER BY
                (CASE WHEN locate(%(_txt)s, name) > 0 THEN locate(%(_txt)s, name) ELSE 99999 END),
                (CASE WHEN locate(%(_txt)s, school_name) > 0 THEN locate(%(_txt)s, school_name) ELSE 99999 END),
                idx DESC, name
            LIMIT %(page_len)s OFFSET %(start)s""".format(
            fields=", ".join(fields),
            scond=searchfields,
        )

        params = {
            "txt": f"%{txt}%",
            "_txt": txt.replace("%", ""),
            "start": start,
            "page_len": page_len,
        }

        # Log the query before execution
        logging.info(f"Executing SQL Query: {query}")
        logging.info(f"With Parameters: {json.dumps(params)}")

        results = frappe.db.sql(query, params, as_dict=as_dict)

        # Log the results
        logging.info(f"Query Results: {json.dumps(results, default=str)}")

        return results

    except Exception as e:
        # Log any error that occurs
        logging.error(f"Error executing school_query: {str(e)}", exc_info=True)
        frappe.log_error(f"Error executing school_query: {str(e)}", "School Query Error")
        return []
