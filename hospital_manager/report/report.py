# -*- coding: utf-8 -*-
from odoo import models


class AdmissionReportXlsx(models.AbstractModel):
    _name = 'report.hospital_manager.admission_report'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, admission):
        for obj in admission:
            report_name = obj.sequence
            row = 1
            sheet = workbook.add_worksheet(obj.sequence)
            bold = workbook.add_format({'bold': True})

            sheet.write_string(row, 0, "Nombre de Ficha", bold)
            sheet.write_string(row, 1, obj.sequence)
            sheet.write_string(row, 6, "Cedula", bold)
            sheet.write_string(row, 7, obj.patient_number or '')
            row += 1
            sheet.write_string(row, 0, "Nombre Paciente", bold)
            sheet.write_string(row, 1, obj.patient_id.name)
            sheet.write_string(row, 6, "Hospital", bold)
            sheet.write_string(row, 7, obj.hospital_id.name or '')
            row += 1