from __future__ import unicode_literals
import frappe
from frappe import auth
import datetime
import json, ast

current_date = datetime.datetime.today().strftime('%Y-%m-%d')
current_user = frappe.session.user

@frappe.whitelist(allow_guest=True)
def login(url):
    usr = 'api@erpcloud.systems'
    pwd = 'Ecs_2022'
    try:
        login_manager = frappe.auth.LoginManager()
        login_manager.authenticate(user=usr, pwd=pwd)
        login_manager.post_login()

    except frappe.exceptions.AuthenticationError:
        frappe.clear_messages()
    domain_status = frappe.db.sql(""" select status as status from `tabAllowed Domains Detail` where domain like '%{url}%' """.format(url=url),as_dict=1)
    modules_icons = frappe.db.sql(""" select module as module , icon as icon from `tabModules Icons`""",as_dict=1)
    doctypes_icons = frappe.db.sql(""" select doctypes as doctypes , icon as icon from `tabDocType Icons`""",as_dict=1)

    status = {}
    module_icons = {}
    doctype_icons = {}

    for state in domain_status:
        status.update({url: state.status})

    for m_icon in modules_icons:
        module_icons.update({m_icon.module : m_icon.icon})

    for d_icon in doctypes_icons:
        doctype_icons.update({d_icon.doctypes: d_icon.icon})



    return status, module_icons, doctype_icons

@frappe.whitelist(allow_guest=True)
def check_domain(url):
    all_domains = frappe.db.sql(""" select
                                `tabAllowed Domains Detail`.domain as domain_url,
                                if(`tabAllowed Domains`.disabled = 1, "Domain Is Inactive", "Domain Is Active") as domain_status
                                from `tabAllowed Domains` join `tabAllowed Domains Detail` 
                                on `tabAllowed Domains Detail`.parent = `tabAllowed Domains`.name
                                where `tabAllowed Domains Detail`.domain like '{url}'
                            """.format(url=url), as_dict=1)
    for x in all_domains:
        return x.domain_status

    else:
        return "Domain Is Inactive"




