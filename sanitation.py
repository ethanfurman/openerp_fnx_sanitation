# -*- coding: utf-8 -*-

from osv import osv
import logging

_logger = logging.getLogger(__name__)

# models

class checklist(osv.Model):
    "sanitation checklist"
    _inherit = "fnx.checklist"
    _name = "sanitation.checklist"


class question(osv.Model):
    "checklist question"
    _inherit = "fnx.checklist.question"
    _name = "sanitation.checklist.question"


class checklist_history(osv.Model):
    "sanitation checklist"
    _inherit = "fnx.checklist.history"
    _name = "sanitation.checklist.history"


class question_history(osv.Model):
    "checklist answer history"
    _inherit = "fnx.checklist.history.answer"
    _name = "sanitation.checklist.history.answer"

