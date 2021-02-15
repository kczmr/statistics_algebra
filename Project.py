import pandas as pd
import mysql.connector as msql
from mysql.connector import Error
import statistics as st
import numpy as np
import scipy.stats as sc
import matplotlib.pyplot as plt
from datetime import datetime

df = pd.read_csv('sales.csv', delimiter=',')

Regions = df['Region'].unique()
Countries = df['Country'].unique()
Items = df[['Item Type', 'Unit Price', 'Unit Cost']].drop_duplicates('Item Type')
Sales_Channel = df['Sales Channel'].unique()
Order_Priority = df['Order Priority'].unique()
Orders = df[['Order ID', 'Order Date', 'Ship Date', 'Units Sold']]
Profits = df[['Total Revenue', 'Total Cost', 'Total Profit']]

try:
    conn = msql.connect(host='localhost', database='sales',
                        user='root', password='xd')
    if conn.is_connected():

        cursor = conn.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()

        # for row in Countries:
        #     cursor.execute("INSERT INTO countries(country_name) VALUES('%s')" % row)
        #     print("Record inserted")
        #     conn.commit()

        # for row in Regions:
        #     cursor.execute("INSERT INTO regions(region_name) VALUES('%s')" % row)
        #     print("Record inserted")
        #     conn.commit()

        # for i, row in Items.iterrows():
        #     cursor.execute("INSERT INTO items(item_name, price, cost) VALUES(%s,%s,%s)", (row['Item Type'],
        #     row['Unit Price'], row['Unit Cost']))
        #     print("Record inserted")
        #     conn.commit()

        # for row in Sales_Channel:
        #     cursor.execute("INSERT INTO sales_channel(type_name) VALUES('%s')" % row)
        #     print("Record inserted")
        #     conn.commit()

        # for row in Order_Priority:
        #     cursor.execute("INSERT INTO orders_priority(level) VALUES('%s')" % row)
        #     print("Record inserted")
        #     conn.commit()

        # for i, row in Orders.iterrows():
        #     cursor.execute("INSERT INTO orders(id,order_date,ship_date,units_sold) VALUES(%s,%s,%s,%s)",
        #                    (row['Order ID'], datetime.strptime(row['Order Date'],'%m/%d/%Y').strftime('%Y-%m-%d'),
        #                     datetime.strptime(row['Ship Date'],'%m/%d/%Y').strftime('%Y-%m-%d'), row['Units Sold']))
        #     print("Record inserted")
        #     conn.commit()

        # for i, row in Profits.iterrows():
        #     cursor.execute("INSERT INTO profits(revenue,cost,profit) VALUES(%s,%s,%s)", (row['Total Revenue'],
        #     row['Total Cost'], row['Total Profit']))
        #     print("Record inserted")
        #     conn.commit()

        cursor.execute("SELECT * FROM regions")
        regions = cursor.fetchall()

        cursor.execute("SELECT * FROM countries")
        countries = cursor.fetchall()

        cursor.execute("SELECT * FROM sales_channel")
        sales_channel = cursor.fetchall()

        cursor.execute("SELECT * FROM items")
        items = cursor.fetchall()

        cursor.execute("SELECT * FROM orders_priority")
        orders_priority = cursor.fetchall()

        cursor.execute("SELECT * FROM profits")
        profits = cursor.fetchall()

        cursor.execute("SELECT units_sold from orders")
        units_sold = cursor.fetchall()

        # for index, row in enumerate(df['Order ID']):
        #     for revenue in profits:
        #         if df['Total Revenue'][index] == revenue[1]:
        #             tmp_revenue = revenue[0]
        #             print(tmp_revenue)
        #     for region in regions:
        #         if df['Region'][index] == region[1]:
        #             tmp_region = region[0]
        #     for country in countries:
        #         if df['Country'][index] == country[1]:
        #             tmp_country = country[0]
        #     for sale_channel in sales_channel:
        #         if df['Sales Channel'][index] == sale_channel[1]:
        #             tmp_sale_channel = sale_channel[0]
        #     for item in items:
        #         if df['Item Type'][index] == item[1]:
        #             tmp_item = item[0]
        #     for order_p in orders_priority:
        #         if df['Order Priority'][index] == order_p[1]:
        #             tmp_order = order_p[0]
        #
        #     cursor.execute("INSERT INTO orders(id,order_date,ship_date,units_sold,region_id,country_id, "
        #                    "sale_channel_id,item_id,profit_id,order_priority_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,
        #                    %s,%s)",(np.int(df['Order ID'][index]),
        #                     datetime.strptime(df['Order Date'][index], '%m/%d/%Y').strftime('%Y-%m-%d'),
        #                     datetime.strptime(df['Ship Date'][index], '%m/%d/%Y').strftime('%Y-%m-%d'),
        #                     np.int(df['Units Sold'][index]), tmp_region, tmp_country, tmp_sale_channel, tmp_item,
        #                     tmp_revenue,tmp_order))
        #     conn.commit()
        #     print('Inserted')

        def stats(col):
            print('MAX value = ', np.max(col))
            print('MIN value = ', np.min(col))
            print('MEAN value = ', np.mean(col))
            print('MEDIAN value = ', np.median(col))
            print('STD = ', st.stdev(col))
            print('VARIANCE = ', st.variance(col))
            print('UPPER MEDIAN = ', st.median_high(col))
            print('LOWER MEDIAN = ', st.median_low(col))

        print('Total Revenue:')
        stats(df['Total Revenue'])
        print('Total Cost:')
        stats(df['Total Cost'])
        print('Total Profit:')
        stats(df['Total Profit'])

        plt.hist(df['Total Revenue'])
        plt.show()

except Error as e:
    print("Error", e)
