app_name = "chimmi_garments"
app_title = "Chimmi Garments Management"
app_publisher = "Dinesh.R"
app_description = "App to manage building flow for Chimmi Garments"
app_email = "dineshrn79@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/chimmi_garments/css/chimmi_garments.css"
# app_include_js = [
#     "/assets/chimmi_garments/js/pos_item_cart.js",
#     "/assets/chimmi_garments/js/pos_item_selector.js"
# ]

# include js, css files in header of web template
# web_include_css = "/assets/chimmi_garments/css/chimmi_garments.css"
# web_include_js = "/assets/chimmi_garments/js/chimmi_garments.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "chimmi_garments/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {
#     "point-of-sale": "public/js/pos_item_cart.js"
# }

# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "chimmi_garments.utils.jinja_methods",
# 	"filters": "chimmi_garments.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "chimmi_garments.install.before_install"
# after_install = "chimmi_garments.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "chimmi_garments.uninstall.before_uninstall"
# after_uninstall = "chimmi_garments.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "chimmi_garments.utils.before_app_install"
# after_app_install = "chimmi_garments.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "chimmi_garments.utils.before_app_uninstall"
# after_app_uninstall = "chimmi_garments.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "chimmi_garments.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"chimmi_garments.tasks.all"
# 	],
# 	"daily": [
# 		"chimmi_garments.tasks.daily"
# 	],
# 	"hourly": [
# 		"chimmi_garments.tasks.hourly"
# 	],
# 	"weekly": [
# 		"chimmi_garments.tasks.weekly"
# 	],
# 	"monthly": [
# 		"chimmi_garments.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "chimmi_garments.install.before_tests"

# Overriding Methods
# ------------------------------
#
override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "chimmi_garments.event.get_events"
"erpnext.controllers.queries.customer_query": "chimmi_garments.custom_code.queries.school_query",
"erpnext.selling.page.point_of_sale.point_of_sale": "chimmi_garments.custom_code.point_of_sale"

}
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "chimmi_garments.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["chimmi_garments.utils.before_request"]
# after_request = ["chimmi_garments.utils.after_request"]

# Job Events
# ----------
# before_job = ["chimmi_garments.utils.before_job"]
# after_job = ["chimmi_garments.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"chimmi_garments.auth.validate"
# ]
