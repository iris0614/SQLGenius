from tiny_sql_agent.db_connection import db_connection
from tiny_sql_agent.tiny_sql_agent import tiny_sql_agent

class result_evaluation:
    def __init__(self):
        self.db = db_connection("Chinook.db")

    def run(self, test_dataset):
        self.agent = tiny_sql_agent(self.db)
        for question, answer in test_dataset:
            result = self.agent.run(question)
            print(f"Question: {question}\nResult: {result}\nAnswer: {answer}\n")

if __name__ == "__main__":
    test_dataset = [
            # ("Which country's customers spent the most? And how much did they spend?", "The country whose customers spent the most is the USA, with a total expenditure of $523.06"),
            # ("What was the most purchased track of 2013?", "The most purchased track of 2013 was Hot Girl."),
            # ("How many albums does the artist Led Zeppelin have?","Led Zeppelin has 14 albums"),
             ("What is the total price for the album “Big Ones”?","The total price for the album 'Big Ones' is 14.85"),
            # ("Which sales agent made the most in sales in 2009?", "Steve Johnson made the most sales in 2009"),
    ]
    result_evaluation().run(test_dataset)
    