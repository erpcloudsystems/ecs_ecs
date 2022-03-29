from __future__ import unicode_literals
import frappe
import erpnext
from frappe import auth
import datetime
import json, ast

@frappe.whitelist()
def ticket_add(**kwargs):
    ticket = frappe.get_doc(kwargs)
    ticket.insert(ignore_permissions=True)
    ticket_name = ticket.name
    frappe.db.commit()
    if (ticket_name):
        return "Ticket Submitted Successfully"
    else:
        return "Ticket Not Submitted"

@frappe.whitelist()
def ticket_cancel(tic):
    ticket = frappe.get_doc('Ticket', {'remote_ticket_no': tic})
    ticket.cancel()
    frappe.db.commit()
    if ticket:
        return ticket
    else:
        "Nothing"





