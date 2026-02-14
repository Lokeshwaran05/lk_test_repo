import requests
from typing import Optional
# def get_full_name(first_name, last_name):
#     full_name = first_name.title() + " " + last_name.title()
#     return full_name


# print(get_full_name("john", "doe"))

def get_fullname(firstname: str, age: int, lastname:str = 'hi'):
    fullname = firstname.title() + " " + lastname.title() + " is of age " + str(age)
    return fullname


print(get_fullname("John",25))

# def get_items(item_a:str, item_b:int, item_c: bool, item_d: float, item_e: bytes): 
#     return item_a,item_b,item_c,item_d,item_e

def process_items(items: list[str]):
    for item in items:
        print(item)

a= ["apple","banana","orange"]
process_items(a)


def get_data_from_api(url: str | None = None):
    if url is None:
        return "No URL provided"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

print(get_data_from_api("https://jsonplaceholder.typicode.com/todos/1"))

def say_name(name : Optional[str] ):
    print(f"hey {name}")

say_name(name = None)
