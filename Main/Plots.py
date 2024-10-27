from datetime import datetime, timedelta
from DatabaseConnector import Connection
import plotly.express as px


class BalanceChart:
    def __init__(self, user_id=1):
        self.user_id = user_id
        self.database = Connection()

    def collect_data(self, start_date, end_date):
        current_balance = self.database.get_balance(self.user_id)
        current_date = datetime.now().strftime('%Y-%m-%d')
        end_date_old = (datetime.strptime(end_date, '%Y-%m-%d') + timedelta(days=1)).strftime('%Y-%m-%d')
        transactions_old = self.database.get_transactions_between_dates(end_date_old, current_date, self.user_id)
        for transaction in transactions_old:
            current_balance -= transaction[2]

        transactions = self.database.get_transactions_between_dates(start_date, end_date, self.user_id)
        transactions.sort(key=lambda x: x[3])
        transactions = list(reversed(transactions))
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.strptime(end_date, '%Y-%m-%d')

        iteration_date = end_date
        data = []
        while iteration_date >= start_date:
            for transaction in transactions:
                if transaction[3] == iteration_date:
                    current_balance -= transaction[2]
            data.append((iteration_date, current_balance))
            iteration_date = iteration_date - timedelta(days=1)
        return data

    def draw_chart(self, start_date, end_date):
        data = self.collect_data(start_date, end_date)
        dates = [x[0] for x in data]
        balances = [x[1] for x in data]
        fig = px.line(x=dates, y=balances, title='Balance chart')
        fig.show()


if __name__ == '__main__':
    chart = BalanceChart()
    chart.draw_chart('2024-10-01', '2024-10-30')
