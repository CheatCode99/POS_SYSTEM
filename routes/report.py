from app import app
from flask import request
from Function.report_func import daily_sales_report, weekly_sales_report, monthly_sales_report, sales_by_criteria
from datetime import date, datetime,timedelta

@app.get('/report/daily')
def daily_report():
    input_date = request.args.get("date") or request.form.get("date")

    if not input_date:
        input_date = date.today().strftime("%Y-%m-%d")

    return daily_sales_report(input_date)

@app.get('/report/weekly')
def weekly_report():
    today = date.today()

    start_of_week = today - timedelta(days=today.isoweekday() - 1)
    end_of_week = start_of_week + timedelta(days=6)

    start_str = start_of_week.strftime("%Y-%m-%d")
    end_str = end_of_week.strftime("%Y-%m-%d")

    report = weekly_sales_report(start_str, end_str)

    return {
        "week_start": start_str,
        "week_end": end_str,
        "report": report
    }, 200

@app.get('/report/monthly')
def monthly_report():
    today = date.today()
    year = today.year
    month = today.month

    report = monthly_sales_report(year, month)

    return {
        "year": year,
        "month": month,
        "report": report
    }, 200

@app.get('/report/criteria')
def criteria_report():
    product_id = request.form.get("product_id")
    category_id = request.form.get("category_id")
    user_id = request.form.get("user_id")
    return sales_by_criteria(
        product_id=int(product_id) if product_id else None,
        category_id=int(category_id) if category_id else None,
        user_id=int(user_id) if user_id else None
    )
