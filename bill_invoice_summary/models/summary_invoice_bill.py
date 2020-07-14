# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import date, datetime, timedelta

class SummaryInvoiceBill(models.Model):
    _name = "summary.invoice.bill"
    _description = "Summary For Invoice & Bill"

    invoice_overdue_total = fields.Float(string="Total Invoice Overdue",default=0.0)
    bill_overdue_total = fields.Float(string="Total Bill Overdue",default=0.0)
    invoice_due_within_7_days_next = fields.Float(default=0.0)
    bill_due_within_7_days_next = fields.Float(default=0.0)
    invoice_due_within_one_month_next = fields.Float(default=0.0)
    bill_due_within_one_month_next = fields.Float(default=0.0)
    unpaid_invoice_from_last_week = fields.Float(default=0.0)
    unpaid_bill_from_last_week = fields.Float(default=0.0)
    unpaid_invoice_from_one_month_before = fields.Float(default=0.0)
    unpaid_bill_from_one_month_before= fields.Float(default=0.0)
    invoice_payment_total = fields.Float(default=0.0)
    bill_payment_total = fields.Float(default=0.0)
    Average_time_to_get_paid_invoice = fields.Float(defult=0.0)
    Average_time_to_get_paid_bill = fields.Float(default=0.0)
    Last_updated = date = fields.Date(default=fields.Date.today)
    currency_id = fields.Many2one('res.currency', string='Currency',
                              default=lambda self: self.env.user.company_id.currency_id)
    
    @api.multi
    def summary_calculate(self):
        updated_data = {
            "Last_updated" : date.today(),
            "invoice_overdue_total" : self.search([]).calculate_inv_due()[0],
            "bill_overdue_total" : self.search([]).calculate_bill_due()[0],
            "invoice_due_within_7_days_next": self.search([]).calculate_inv_due_next()[0],
            "bill_due_within_7_days_next": self.search([]).calculate_bill_due_next()[0],
            "invoice_due_within_one_month_next": self.search([]).calculate_inv_due_next_one_month()[0],
            "bill_due_within_one_month_next": self.search([]).calculate_bill_due_next_one_month()[0],
            "unpaid_invoice_from_last_week": self.search([]).calculate_unpaid_inv_last_week()[0],
            "unpaid_bill_from_last_week": self.search([]).calculate_unpaid_bill_last_week()[0],
            "unpaid_invoice_from_one_month_before": self.search([]).calculate_unpaid_inv_month_ago()[0],
            "unpaid_bill_from_one_month_before": self.search([]).calculate_unpaid_bill_month_ago()[0],
            "invoice_payment_total": self.search([]).compute_inv_payment()[0],
            "bill_payment_total":self.search([]).compute_bill_payment()[0],
            "Average_time_to_get_paid_invoice" : self.search([]).avg_inv_payment()[0],
            "Average_time_to_get_paid_bill" : self.search([]).avg_bill_payment()[0]
        }
       
        self.search([]).write(updated_data)
        return{
            'name': 'Overdue Summary',
            'type': 'ir.actions.act_window',
            'res_model': 'summary.invoice.bill',
            'view_type': 'form',
            'view_mode': 'tree,form',
            'domain': [],
            'view_id': False
       }
    
    @api.one
    @api.depends('residual_company_signed')
    def calculate_inv_due(self):
        total = 0.0
        invoices = self.env['account.invoice'].search([('type','=','out_invoice'),('state','=','open'),('date_due','<',date.today())])
        for data in invoices:
            total += data.residual_company_signed
        return total

    @api.one
    @api.depends('residual_company_signed')
    def calculate_bill_due(self):
        total = 0.0
        bills = self.env['account.invoice'].search([('type','=','in_invoice'),('state','=','open'),('date_due','<',date.today())])
        for data in bills:
            total += data.residual_company_signed
        return total
    
    @api.one
    @api.depends('residual_company_signed')
    def calculate_inv_due_next(self):
        total = 0.0
        invoices = self.env['account.invoice'].search([('type','=','out_invoice'),('state','=','open'),
        ('date_due','<=',date.today()+timedelta(days=7)),('date_due','>=',date.today())])
        for data in invoices:
            total += data.residual_company_signed
        return total

    @api.one
    @api.depends('residual_company_signed')
    def calculate_bill_due_next(self):
        total = 0.0
        bills = self.env['account.invoice'].search([('type','=','in_invoice'),('state','=','open'),
        ('date_due','<=',date.today()+timedelta(days=7)),('date_due','>=',date.today())])
        for data in bills:
            total += data.residual_company_signed
        return total
    
    @api.one
    @api.depends('residual_company_signed')
    def calculate_inv_due_next_one_month(self):
        total = 0.0
        invoices = self.env['account.invoice'].search([('type','=','out_invoice'),('state','=','open'),
        ('date_due','<=',date.today()+timedelta(days=30)),('date_due','>',date.today()+timedelta(days=7))])
        for data in invoices:
            total += data.residual_company_signed
        return total

    @api.one
    @api.depends('residual_company_signed')
    def calculate_bill_due_next_one_month(self):
        total = 0.0
        bills = self.env['account.invoice'].search([('type','=','in_invoice'),('state','=','open'),
        ('date_due','<=',date.today()+timedelta(days=30)),('date_due','>',date.today()+timedelta(days=7))])
        for data in bills:
            total += data.residual_company_signed
        return total

    @api.one
    @api.depends('residual_company_signed')
    def calculate_unpaid_inv_last_week(self):
        total = 0.0
        invoices = self.env['account.invoice'].search([('type','=','out_invoice'),('state','=','open'),
        ('date_due','>=',date.today()-timedelta(days=7)),('date_due','<',date.today())])
        for data in invoices:
            total += data.residual_company_signed
        return total

    @api.one
    @api.depends('residual_company_signed')
    def calculate_unpaid_bill_last_week(self):
        total = 0.0
        bills = self.env['account.invoice'].search([('type','=','in_invoice'),('state','=','open'),
        ('date_due','>=',date.today()-timedelta(days=7)),('date_due','<',date.today())])
        for data in bills:
            total += data.residual_company_signed
        return total

    @api.one
    @api.depends('residual_company_signed')
    def calculate_unpaid_inv_month_ago(self):
        total = 0.0
        invoices = self.env['account.invoice'].search([('type','=','out_invoice'),('state','=','open'),
        ('date_due','>=',date.today()-timedelta(days=30)),('date_due','<',date.today()-timedelta(days=7))])
        for data in invoices:
            total += data.residual_company_signed
        return total

    @api.one
    @api.depends('residual_company_signed')
    def calculate_unpaid_bill_month_ago(self):
        total = 0.0
        bills = self.env['account.invoice'].search([('type','=','in_invoice'),('state','=','open'),
        ('date_due','>=',date.today()-timedelta(days=30)),('date_due','<',date.today()-timedelta(days=7))])
        for data in bills:
            total += data.residual_company_signed
        return total

    @api.one
    def compute_inv_payment(self):
        total = 0.0
        self.env.cr.execute("SELECT account_payment.amount FROM account_payment INNER JOIN account_invoice_payment_rel ON payment_id = id INNER JOIN account_invoice ON invoice_id= account_invoice.id WHERE account_payment.state='posted' and payment_type='inbound'")
        query = self.env.cr.dictfetchall()
        for data in query:
            total += data['amount']
        return total

    @api.one
    def compute_bill_payment(self):
        total = 0.0
        self.env.cr.execute("SELECT account_payment.amount FROM account_payment INNER JOIN account_invoice_payment_rel ON payment_id = id INNER JOIN account_invoice ON invoice_id= account_invoice.id WHERE account_payment.state='posted' and payment_type='outbound'")
        query = self.env.cr.dictfetchall()
        for data in query:
            total += data['amount']
        return total

    @api.one
    def avg_inv_payment(self):
        total = 0.0
        self.env.cr.execute("SELECT account_invoice.date_invoice, payment_date FROM account_payment INNER JOIN account_invoice_payment_rel ON payment_id = id INNER JOIN account_invoice ON invoice_id= account_invoice.id WHERE account_payment.state='posted' and payment_type='inbound'")
        query = self.env.cr.dictfetchall()
        for data in query:
            temp = (data['payment_date']-data['date_invoice']).days
            total += temp
        if (len(query)!=0):
            return total/len(query)
        return 0
    
    @api.one
    def avg_bill_payment(self):
        total = 0.0
        self.env.cr.execute("SELECT account_invoice.date_invoice, payment_date FROM account_payment INNER JOIN account_invoice_payment_rel ON payment_id = id INNER JOIN account_invoice ON invoice_id= account_invoice.id WHERE account_payment.state='posted' and payment_type='outbound'")
        query = self.env.cr.dictfetchall()
        for data in query:
            temp = (data['payment_date']-data['date_invoice']).days
            total += temp
        if (len(query)!=0):
            return total/len(query)
        return 0
    