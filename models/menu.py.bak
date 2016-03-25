# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

response.logo = A(B(SPAN('Happy Journey')),XML('&trade;&nbsp;'),
                  _class="navbar-brand",_href="http://127.0.0.1:8000/pro1/default/index.html",
                  _id="web2py-logo")
response.title ='ITWS-II Project' ##request.application.replace('_',' ').title()
response.subtitle = ''

## read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'Your Name <you@example.com>'
response.meta.description = 'a cool new app'
response.meta.keywords = 'web2py, python, framework'
response.meta.generator = 'Web2py Web Framework'

## your http://google.com/analytics id
response.google_analytics_id = None

#########################################################################
## this is the main application menu add/remove items as required
#########################################################################

response.menu = [
    (T('Home'), False, URL('default', 'index'), []),
    ('Plan A Trip',False,URL('default','search_flight')),
]
if auth.is_logged_in():
    response.menu.append(('View Bookings',False,URL('default','viewbookings')))
    response.menu.append(('Review',False,'#',[
                                              ('Write a Review',False,URL('default','creview')),
                                              ('View Reviews',False,URL('default','review'))]))
if auth.has_membership('managers'):
    response.menu.append(('Manage',False,'#',[('User',False,URL('default','manage_users')),
                                              ('Review',False,URL('default','manage_review')),
                                              ('Places',False,URL('default','manage_places')),
                                              ('Flight',False,URL('default','manage_flight')),
                                              ('Train',False,URL('default','manage_train'))
                                             ]))

if "auth" in locals(): auth.wikimenu()
