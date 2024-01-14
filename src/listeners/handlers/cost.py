import boto3
from datetime import datetime
from dateutil.relativedelta import *

def handler(respond):
  cost_explorer = boto3.client('ce')

  today = datetime.today()
  month_start = datetime(today.year, today.month, 1)

  result = cost_explorer.get_cost_and_usage(
    TimePeriod = {
      'Start': str(month_start.strftime('%Y-%m-%d')),
      'End': str(today.strftime('%Y-%m-%d'))
    },
    Granularity='MONTHLY',
    Metrics=['UnblendedCost']
  )

  total_cost = round(float(result['ResultsByTime'][0]['Total']['UnblendedCost']['Amount']), 2)
  respond(f"오늘 기준 이번달 사용 금액은 {total_cost} 달러입니다.")