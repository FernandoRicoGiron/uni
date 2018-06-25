import urllib, base64
from django import template

from io import StringIO


from datetime import datetime, timedelta

from django.utils.timesince import timesince
import math


register = template.Library()

@register.filter
def nu(val):
    if val == None:
       return ""
    else: 
        return val

