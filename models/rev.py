# -*- coding: utf-8 -*-
db.define_table('review',
               Field('title',requires=IS_NOT_EMPTY()),
               Field('body','text',requires=IS_NOT_EMPTY()),
               auth.signature)
