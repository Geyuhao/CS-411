"""Defines all the functions related to the database"""
from app import db




def fetch_wish_list() -> dict:
    """Reads all tasks listed in the todo table

    Returns:
        A list of dictionaries
    """

    conn = db.connect()
    query_results = conn.execute("Select * from Wish_list;").fetchall()
    conn.close()
    todo_list = []
    for result in query_results:
        item = {
            "Wish_ID": result[0],
            "Create_Date": result[1],
            "Acceptable_Price": result[2],
            "Wisher_Name": result[3],
            "Product_Name": result[4],
        }
        todo_list.append(item)

    return todo_list

def fetch_offer_list() -> dict:
    conn = db.connect()
    query_results = conn.execute("Select * from Offer_list;").fetchall()
    conn.close()
    todo_list = []
    for result in query_results:
        item = {
            "Offer_ID": result[0],
            "Create_Date": result[1],
            "Prodiving_Price": result[2],
            "Provider_Name": result[3],
            "Product_Name": result[4],
            "Condition_status":result[5],
        }
        todo_list.append(item)
    return todo_list

def fetch_product_list() -> dict:
    conn = db.connect()
    query_results = conn.execute("Select * from Product;").fetchall()
    conn.close()
    user_list = []
    for result in query_results:
        item = {
            "Product_Name": result[3],
            "Brand": result[0],
            "Manufactor": result[1],
        }
        user_list.append(item)
    return user_list

# Newly added
def insert_wish(data: dict) -> None:
    """Insert new task to todo table.

    Args:
        text (str): Task description

    Returns: The task ID for the inserted entry
    """
    conn = db.connect()
    query = 'Insert Into Wish_list (Product_Name, Acceptable_Price, Wisher_Name) VALUES ("{}", "{}","{}");'.format(
        data["Product Name"], data["Acceptable Price"], data["Your Name"])
    conn.execute(query)
    query_results = conn.execute("Select LAST_INSERT_ID();")
    query_results = [x for x in query_results]
    task_id = query_results[0][0]
    conn.close()

def insert_offer(data: dict) -> None:
    conn = db.connect()
    query = 'Insert Into Offer_list (Product_Name, Prodiving_Price, Provider_Name) VALUES ("{}", "{}","{}");'.format(
        data["Product Name"], data["Offer Price"], data["Your Name"])
    conn.execute(query)
    query_results = conn.execute("Select LAST_INSERT_ID();")
    query_results = [x for x in query_results]
    task_id = query_results[0][0]
    conn.close()

# Newly added
def update_wish(task_id: int, data: dict) -> None:
    """Insert new task to todo table.

    Args:
        text (str): Task description

    Returns: The task ID for the inserted entry
    """

    conn = db.connect()
    query = 'Update Wish_list set Product_Name = "{}", Acceptable_Price = "{}", Wisher_Name = "{}" Where Wish_ID = "{}"'.format(
        data["Product Name"], data["Acceptable Price"], data["Your Name"], task_id)
    conn.execute(query)
    query_results = conn.execute("Select LAST_INSERT_ID();")
    query_results = [x for x in query_results]
    task_id = query_results[0][0]
    conn.close()

def update_offer(task_id: int, data: dict) -> None:
    conn = db.connect()
    query = 'Update Offer_list set Product_Name = "{}", Prodiving_Price = "{}", Provider_Name = "{}" Where Offer_ID = "{}"'.format(
        data["Product Name"], data["Offer Price"], data["Your Name"], task_id)
    conn.execute(query)
    query_results = conn.execute("Select LAST_INSERT_ID();")
    query_results = [x for x in query_results]
    task_id = query_results[0][0]
    conn.close()


def remove_Wish_by_Wish_id(Wish_ID: int) -> None:
    """ remove entries based on Wish_ID """
    conn = db.connect()
    query = 'Delete From Wish_list where Wish_ID={};'.format(Wish_ID)
    conn.execute(query)
    conn.close()

def remove_Offer_by_Offer_id(Offer_ID: int) -> None:
    """ remove entries based on Offer_ID """
    conn = db.connect()
    query = 'Delete From Offer_list where Offer_ID={};'.format(Offer_ID)
    conn.execute(query)
    conn.close()

def Search_Wishlist_by_Product_Name(data: dict) -> dict:
    """ Search entries based on Product_Name """
    conn = db.connect()
    query = 'Select * From Wish_list where Product_Name="{}";'.format(data["Product Name"])
    sqlresult = conn.execute(query).fetchall()
    conn.close()
    search_list = []
    for result in sqlresult:
        item = {
            "Wish_ID": result[0],
            "Create_Date": result[1],
            "Acceptable_Price": result[2],
            "Wisher_Name": result[3],
            "Product_Name": result[4],
        }
        search_list.append(item)
    return search_list

def Search_Offerlist_by_Product_Name(data: dict) -> dict:
    """ Search entries based on Product_Name """
    conn = db.connect()
    query = 'Select * From Offer_list where Product_Name="{}";'.format(data["Product Name"])
    sqlresult = conn.execute(query).fetchall()
    conn.close()
    search_list = []
    for result in sqlresult:
        item = {
            "Offer_ID": result[0],
            "Create_Date": result[1],
            "Prodiving_Price": result[2],
            "Provider_Name": result[3],
            "Product_Name": result[4],
            "Condition_status":result[5],
        }
        search_list.append(item)
    return search_list

def Search_Query() -> dict:
    conn = db.connect()
    query = '''
            SELECT w.Product_Name, o.Prodiving_Price, Provider_Name, Wisher_Name, o.Condition_status
            FROM Wish_list w Join Offer_list o USING (Product_Name)
            WHERE w.Product_Name in
                (SELECT o.Product_Name
                FROM Wish_list w Join Offer_list o USING (Product_Name)
                WHERE w.Product_Name = o.Product_Name 
                GROUP BY o.Product_Name
                HAVING COUNT(o.Product_Name) > 1)
            ORDER BY w.Product_Name, o.Prodiving_Price
            LIMIT 40;
            '''

    sqlresult = conn.execute(query).fetchall()
    conn.close()
    search_list = []
    for result in sqlresult:
        item = {
            "Product_Name": result[0],
            "Prodiving_Price": result[1],
            "Provider_Name": result[2],
            "Wisher_Name": result[3],
            "Condition_status": result[4],
        }
        search_list.append(item)

    return search_list

def display_goodprice() -> dict:
    conn = db.connect()
    query = '''
            Select * From MerchantTable;
            '''

    sqlresult = conn.execute(query).fetchall()
    conn.close()
    search_list = []
    for result in sqlresult:
        item = {
            "Product_name": result[0],
            "Merchant_name": result[1],
            "Providing_price": result[2]
        }
        search_list.append(item)

    return search_list

def display_hot() -> dict:
    conn = db.connect()
    query = '''
            Select * From HotProducts;
            '''

    sqlresult = conn.execute(query).fetchall()
    conn.close()
    search_list = []
    for result in sqlresult:
        item = {
            "Product_Name": result[0],
            "Merchant_Name": result[2],
            "Providing_Price": result[1]
        }
        search_list.append(item)

    return search_list

def Search_Query1() -> dict:
    conn = db.connect()
    query = """(SELECT w.Product_Name, Provider_Name, avg(o.Prodiving_Price)
            FROM Wish_list w JOIN Offer_list o ON w.Product_Name = o.Product_Name
            GROUP BY Product_Name, Provider_Name)
            UNION
            (SELECT Product_Name, Merchant, avg(Highest_price)
            FROM Transactions t
            WHERE Merchant != ''   
            GROUP BY Product_Name, Merchant)
            limit 40;"""

    sqlresult = conn.execute(query).fetchall()
    conn.close()
    search_list = []
    for result in sqlresult:
        item = {
            "Product_Name": result[0],
            "Provider_Name": result[1],
            "Prodiving_Price": result[2]
        }
        search_list.append(item)

    return search_list

# added gyh
def register_user(data: dict) -> None:
    conn = db.connect()
    username = data["User"]
    password = data["Password"]
    birthday = data["Birthday"]
    print("check",username,password,birthday)
    query = 'Insert Into User (Users_Name, Users_Password, Birthday) VALUES ("{}", "{}","{}");'.format(username, password, birthday)
    conn.execute(query)
    conn.close()

# newone
def check_user_p(data: dict) -> None:
    conn = db.connect()
    username = data["User"]
    password = data["Password"]
    # print(username,password)
    query = "SELECT COUNT(*) FROM User WHERE Users_Name='{}' and Users_Password='{}';".format(username,password)
    count = conn.execute(query)
    count = count.fetchall()[0][0]
    conn.close()
    print("count is:",count)
    return count

def procedure(data: dict) -> None:
    connection = db.raw_connection()
    product = data["Product Name"]
    price = data["Price"]
    print("Hmm2")
    try:
        cursor = connection.cursor()
        cursor.callproc('Result', [product, price])
        print("Hmm3")
        cursor.close()
        connection.commit()
    finally:
        print("Hmm1")
        connection.close()

    # conn = db.raw_connection()
    
    
    # try:
    #     cursor_obj = conn.cursor()
    #     cursor_obj.callproc("Result", [product, price])
    #     cursor_obj.close()
    #     print("Hmm1")
    #     conn.commit()
    # finally:
    #     conn.close()
    #     print("Hmm0")
    
    
    
    # query = "SELECT * FROM User WHERE Users_Name={} and Users_Password={}".format(username,password)
    # conn.execute(query)
    #conn.close()