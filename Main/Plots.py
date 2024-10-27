from datetime import datetime, timedelta
from DatabaseConnector import Connection
import plotly.express as px
import plotly.graph_objects as go
from os import mkdir
from os.path import exists


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
        fig = px.line(x=dates, y=balances, labels={'x': '', 'y': ''})
        fig.update_traces(line={'width': 7, 'color': 'orange'})
        fig.update_layout(
            font=dict(
                family="Adele",
                size=26,
                color="black",
                ),
            paper_bgcolor='rgba(0.7,0.7,0.7,1)',
            plot_bgcolor='rgba(0.2,0.2,0.3,1)',
)
        if not exists("../Plots"):
            mkdir("../Plots")
        fig.write_image("../Plots/balance_chart.png")


class ExpenditureChart:
    def __init__(self, user_id=1):
        self.user_id = user_id
        self.database = Connection()

    def collect_data(self):
        categories = self.database.get_categories()
        data = []
        for category in categories:
            transactions = self.database.get_transactions_by_category(category[0], self.user_id)
            total = 0
            for transaction in transactions:
                total += transaction[2]
            data.append((category[1], total))
        return data

    def draw_chart(self):
        data = self.collect_data()
        categories = [x[0] for x in data]
        totals = [(-1 * x[1]) for x in data]
        colours = ['blue', 'red', 'green', 'yellow', 'purple', 'grey']
        fig = go.Figure(data=[go.Pie(labels=categories, values=totals, hole=.5)])
        fig.update_traces(textinfo='none', marker=dict(colors=colours))
        fig.update_layout(showlegend=False, paper_bgcolor='rgba(0.7,0.7,0.7,1)',)
        if not exists("../Plots"):
            mkdir("../Plots")
        fig.write_image("../Plots/expenditure_chart.png")


if __name__ == '__main__':
    # balance_chart = BalanceChart()
    # balance_chart.draw_chart('2021-01-01', '2021-12-31')
    expenditure_chart = ExpenditureChart()
    expenditure_chart.draw_chart()