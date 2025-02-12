from tiny_sql_agent.db_connection import db_connection
from tiny_sql_agent.tiny_sql_agent import tiny_sql_agent

class result_evaluation:
    def __init__(self):
        self.db = db_connection("Northwind.db")

    def run(self, test_dataset):
        self.agent = tiny_sql_agent(self.db)
        for question, answer in test_dataset:
            result = self.agent.run(question)
            print(f"Question: {question}\nResult: {result}\nExpected Answer: {answer}\n")

if __name__ == "__main__":
    test_dataset = [
        ("Find the name of the customer who placed the most orders?", "The customer who placed the most orders is 'Save-a-lot Markets', with 31 orders"),
        # ("What were our total revenues in 1997?", "The total revenues for the year 1997 were $617085.2035"),
        # ("What is the total amount of customer ALFKI has paid us so far?", "ALFKI has paid a total of $4273.0 so far"),
        # ("Identify the top 3 products with the highest total quantity sold.", "1. Camembert Pierrot - 1,577 units 2. Raclette Courdavault - 1,496 units 3. Gorgonzola Telino - 1,397 units"),
        # ("Create a view with total revenues per customer", "View created with total revenues per customer"),
        # ("Which UK customers have paid us more than 1000 dollars?", 
        # """| CustomerID | CompanyName            | TotalPaid   |
        # |------------|-------------------------|-------------|
        # | AROUT      | Around the Horn         | 13390.65    |
        # | BSBEV      | B's Beverages           | 6089.9      |
        # | CONSH      | Consolidated Holdings   | 1719.1      |
        # | EASTC      | Eastern Connection      | 14761.035   |
        # | ISLAT      | Island Trading          | 6146.3      |
        # | SEVES      | Seven Seas Imports      | 16215.325   |
        # """),
        # ("Which customer has paid the most in total, and how much is it?", "QUICK-Stop with a total of 110277.305"),
        # ("I confirm that Deleting the table 'Customers' from the database", "Check the table structure"),
        # ("Update the 'Customers' table by adding a new column named 'Gender' and set all values to 'Male'.", "Check the table 'Customers'")
    ]
    result_evaluation().run(test_dataset)
