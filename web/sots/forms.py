from flask_wtf import Form
from wtforms import StringField, SelectField, SelectMultipleField, BooleanField, validators, DateField, HiddenField
from sots.config import BaseConfig as ConfigObject
from datetime import datetime
from wtforms.widgets import TextArea

class SearchForm(Form):
    query = StringField('Search Term', [validators.Length(max=255)])
    sort_by = HiddenField(default='nm_name')
    sort_order = HiddenField(default='asc')
    index_field = SelectField('Choices',
                         choices=[
                             ('business_name', 'Business Name'),
                             ('place_of_business_address', 'Business Address'),
                             ('bus_id', 'Business ID'),
                             ('filing_number', 'Filing Number')
                         ])


# TODO Break out index into components -- individual fields w/ and/or
class AdvancedSearchForm(Form):
    # start_date_default = datetime.strptime('1900-01-01', '%Y-%m-%d')
    # end_date_default = datetime.strptime('2016-08-01', '%Y-%m-%d')
    start_date_default = datetime.strptime(ConfigObject.START_DATE, '%Y-%m-%d')
    end_date_default = datetime.strptime(ConfigObject.END_DATE, '%Y-%m-%d')
    sort_by = HiddenField(default='nm_name')
    sort_order = HiddenField(default='asc')
    query = StringField('Search Term', [validators.Length(max=255)])
    query_limit = StringField('Search Term Limit', [validators.Length(max=255), validators.optional()])
    index_field = SelectField('Choices',
                         choices=[
                             ('business_name', 'Business Name'),
                             ('place_of_business_address', 'Business Address'),
                             ('bus_id', 'Business ID'),
                             ('filing_number', 'Filing Number')
                         ])
    start_date = DateField('Start Date', format='%Y-%m-%d', default=start_date_default,
                           validators=[validators.optional()])
    end_date = DateField('End Date', format='%Y-%m-%d', default=end_date_default,
                         validators=[validators.optional()])
    active = BooleanField('Active Businesses Only', default=False, validators=[validators.optional()])
    business_type = SelectMultipleField('Business Type',
                                        validators=[validators.optional()],
                                        default='All Entities',
                                        choices=[('All Entities', 'All Entities'), ('Corporation', 'Corporation'),
                                                 ('Domestic Limited Partnership', 'Domestic Limited Partnership'),
                                                 ('Foreign Limited Partnership', 'Foreign Limited Partnership'),
                                                 ('Domestic Limited Liability Company',
                                                  'Domestic Limited Liability Company'),
                                                 ('Foreign Limited Liability Company',
                                                  'Foreign Limited Liability Company'), (
                                                     'Domestic Limited Liability Partnership',
                                                     'Domestic Limited Liability Partnership'), (
                                                     'Foreign Limited Liability Partnership',
                                                     'Foreign Limited Liability Partnership'),
                                                 ('General Partnership', 'General Partnership'),
                                                 ('Domestic Statutory Trust', 'Domestic Statutory Trust'),
                                                 ('Foreign Statutory Trust', 'Foreign Statutory Trust'),
                                                 ('Other', 'Other'),
                                                 ('Domestic Stock Corporation', 'Domestic Stock Corporation'),
                                                 ('Foreign Stock Corporation', 'Foreign Stock Corporation'),
                                                 ('Domestic Non-Stock Corporation', 'Domestic Non-Stock Corporation'),
                                                 ('Foreign Non-Stock Corporation', 'Foreign Non-Stock Corporation'),
                                                 ('Domestic Credit Union Stock', 'Domestic Credit Union Stock'),
                                                 ('Domestic Credit Union Non-Stock', 'Domestic Credit Union Non-Stock'),
                                                 ('Domestic Bank Stock', 'Domestic Bank Stock'),
                                                 ('Domestic Bank Non-Stock', 'Domestic Bank Non-Stock'),
                                                 ('Domestic Insurance Stock', 'Domestic Insurance Stock'),
                                                 ('Domestic Insurance Non-Stock', 'Domestic Insurance Non-Stock'),
                                                 ('Benefit Corporation', 'Benefit Corporation')])


class FeedbackForm(Form):
    goal_label = 'What were you trying to do and how can we improve it?*'
    general_label = 'General Feedback'
    submitter_label = 'Tell us about yourself'
    goal = StringField(goal_label, [validators.required()], widget=TextArea())
    general = StringField(general_label, widget=TextArea())
    submitter = StringField(submitter_label, widget=TextArea())
    user_agent = HiddenField('user-agent', [validators.required()])