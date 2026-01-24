a = [0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print (a[-1])

#set ([1, 2, 1]) == set([1,2])
 
#print("hello" 'world ' * 2)

# def a(b, c, d): pass

#a =7
#a.__str__()


#import re
#m = re.search(r'(ab[cd]?)', "acdeabdabcde")
#print(m.groups())

#import itertools
#[i for i in filter(lambda x: x % 5,
#    itertools.islice(itertools.count(5), 10))]

#import re
#text = "abc123def456ghi"
#pattern = r"(?:abc)\d+"
#matches = re.findall(pattern, text)
#print(matches)

""""
import logging
logging.basicConfig(level=logging.DEBUG)
def divide(a, b):
    logging.debug(f"Dividing {a} by {b}")
    try:
        result = a / b
    except ZeroDivisionError:
        logging.error("Attemped to divide by zero.")
        return None
    logging.info(f"Division successful: {result}")
    return result

divide(10, 0)
divide(10, 2)
"""


'''
class User:
    def access_page(self,page_type):
        if page_type == 'admin':
            raise Exception("Admins only")
        return "Page accessed"
class Admin(User):
    def access_page(self, page_type):
        return "Admin page accessed"
'''


'''
import asyncio
async def do_work():
    print("Starting work")
    await asyncio.sleep(2)
    print("Work finished")

async def main():
    task1 = asyncio.create_task(do_work())
    task2 = asyncio.create_task(do_work())
    await task1
    await task2

asyncio.run(main())
'''
