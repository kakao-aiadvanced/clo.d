import os
from openai import OpenAI

def gpt4omini(prompt, content):
    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY")
    )
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
    	{"role": "system", "content": prompt},
    	{
    	    "role": "user",
    	    "content": content 
    	}
        ]
    )

    print(completion.choices[0].message)

gpt4omini("You are a helpful assistant.", "Write a haiku about recursion in programming.")

gpt4omini(
"""
Translate the following English words or phrases into Korean. Examples are provided:
	1.	“hello” → “안녕하세요”
	2.	“apple” → “사과”
	3.	“book” → “책”
	4.	“house” → “집”
	5.	“love” → “사랑”
""",
"Now, translate “dog” into Korean."
)

gpt4omini(
"""
You are a sentiment analysis model that evaluates movie reviews. Your task is to classify the sentiment of a review as either Positive or Negative based on the content of the review. Respond with only “Positive” or “Negative.” Here are some examples:
	1.	Review: “The cinematography was breathtaking and the performances were exceptional.”
Sentiment: Positive
	2.	Review: “The plot was confusing and lacked depth.”
Sentiment: Negative
	3.	Review: “An unforgettable experience with a touching storyline.”
Sentiment: Positive
	4.	Review: “The pacing was too slow, and the characters felt one-dimensional.”
Sentiment: Negative
	5.	Review: “A masterpiece that will stay with you for a long time.”
Sentiment: Positive
"""
, "The storyline was dull and uninspiring."
)

gpt4omini(
"""
Convert the following natural language requests into SQL queries:
	1.	Natural Language: “Find all employees with a salary greater than 50,000.”
SQL Query: SELECT * FROM employees WHERE salary > 50000;
	2.	Natural Language: “Find all products that are out of stock.”
SQL Query: SELECT * FROM products WHERE stock = 0;
	3.	Natural Language: “Get the names of students who scored above 90 in math.”
SQL Query: SELECT name FROM students WHERE math_score > 90;
	4.	Natural Language: “Find all orders placed in the last 30 days.”
SQL Query: SELECT * FROM orders WHERE order_date >= DATE_SUB(CURDATE(), INTERVAL 30 DAY);
	5.	Natural Language: “Count the number of customers in each city.”
SQL Query: SELECT city, COUNT(*) FROM customers GROUP BY city;
"""
, "Find the average salary of employees in the marketing department."
)

gpt4omini(
"""
Solve the following problems step-by-step:
Example 1:

Problem: 23 + 47

Step-by-step solution:
	1.	Break the numbers into their place values: 23 = 20 + 3, 47 = 40 + 7.
	2.	Add the tens: 20 + 40 = 60.
	3.	Add the ones: 3 + 7 = 10.
	4.	Combine the results: 60 + 10 = 70.

Answer: 70
Example 2:

Problem: 123 - 58

Step-by-step solution:
	1.	Break the numbers into their place values: 123 = 100 + 20 + 3, 58 = 50 + 8.
	2.	Subtract the tens and hundreds: 100 + 20 - 50 = 70.
	3.	Subtract the ones: 3 - 8. Since 3 is smaller than 8, borrow 10 from the tens (making 70 into 60). Now 13 - 8 = 5.
	4.	Combine the results: 60 + 5 = 65.

Answer: 65
"""
, "Solve the following problem step-by-step: 345 + 678 - 123"
)
