#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 17:49:30 2021

@author: Kostja
"""



from django.core.management.base import BaseCommand
import pandas as pd
from webapp.models import Webapp
from django.db import IntegrityError
from django.utils import timezone

class Command(BaseCommand):
    def handle(self, **options):
        try:
            task_df = pd.read_csv('./data/task_data.csv', sep = ',', parse_dates=['timestamp'], infer_datetime_format=True)
            df_temp = task_df['timestamp']
            df_temp.index = task_df['timestamp']
            df_temp = df_temp.tz_localize('UTC').tz_convert('Etc/GMT+4')
            task_df['timestamp'] = df_temp.index
            task_df['duration'] = pd.to_timedelta(task_df['duration'])
    
            row_iterations = task_df.iterrows()
    
            objects = [Webapp(id = row['id'],
                        timestamp  = row['timestamp'],
                        temperature  = row['temperature'],
                        duration  = row['duration'] )
                        for index, row in row_iterations]
            
            Webapp.objects.bulk_create(objects)
            return 'Csv imported succesfully'
        except: 
            return('You probably allready have this rows in your database:\n')