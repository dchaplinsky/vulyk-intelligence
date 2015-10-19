# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from vulyk.models.task_types import AbstractTaskType

from vulyk_intelligence.models.tasks import (
    IntelligenceAnswer, IntelligenceTask)


class IntelligenceTaskType(AbstractTaskType):
    """
    Intelligence Task to work with Vulyk.
    """
    answer_model = IntelligenceAnswer
    task_model = IntelligenceTask

    name = 'Проверка кандидатов по открытым источникам'
    description = ''

    template = 'base.html'
    helptext_template = 'help.html'
    type_name = 'intelligence_task'

    redundancy = 5

    JS_ASSETS = ['static/scripts/handlebars.js',
                 'static/scripts/jquery.serializejson.js',
                 'static/scripts/base.js', ]

    CSS_ASSETS = ['static/styles/bootstrap-social.css',
                  'static/styles/base.css', ]
