""" Specifies routing for the application"""
from flask import redirect, render_template, request, jsonify, session
from app import app
from app import database as db_helper

@app.route("/delete/<int:Wish_ID>", methods=['POST'])
def delete(Wish_ID):            
    """ recieved post requests for entry delete """
    try:
        db_helper.remove_Wish_by_Wish_id(Wish_ID)
        result = {'success': True, 'response': 'Removed Wish'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}
    return jsonify(result)

@app.route("/delete-offer/<int:Offer_ID>", methods=['POST'])
def delete_offer(Offer_ID):            
    """ recieved post requests for entry delete """
    try:
        db_helper.remove_Offer_by_Offer_id(Offer_ID)
        result = {'success': True, 'response': 'Removed Offer'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}
    return jsonify(result)

@app.route("/edit/<int:Wish_ID>", methods=['POST'])
def update(Wish_ID):
    """ recieved post requests for entry updates """
    data = request.get_json()
    try:
        db_helper.update_wish(Wish_ID, data)
        result = {'success': True, 'response': 'Updated'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}
    return jsonify(result)

@app.route("/edit-offer/<int:Offer_ID>", methods=['POST'])
def update_offer(Offer_ID):
    """ recieved post requests for entry updates """
    data = request.get_json()
    try:
        db_helper.update_offer(Offer_ID, data)
        result = {'success': True, 'response': 'Updated'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}
    return jsonify(result)

@app.route("/create", methods=['POST'])
def create():
    """ recieves post requests to add new task """
    data = request.get_json()
    db_helper.insert_wish(data)
    result = {'success': True, 'response': 'Done'}
    return jsonify(result)

@app.route("/create-offer", methods=['POST'])
def create_offer():
    """ recieves post requests to add new task """
    data = request.get_json()
    db_helper.insert_offer(data)
    result = {'success': True, 'response': 'Done'}
    return jsonify(result)

@app.route("/search", methods=['POST'])
def search():
    """ recieves post requests to add new task """
    data = request.get_json()
    searched_list = db_helper.Search_Wishlist_by_Product_Name(data)
    session['searched_list'] = searched_list
    result = {'success': True, 'response': 'Done'}
    return jsonify(result)
    return redirect(url_for('b'))

@app.route("/search-offer", methods=['POST'])
def search_offer():
    """ recieves post requests to add new task """
    data = request.get_json()
    searched_list = db_helper.Search_Offerlist_by_Product_Name(data)
    session['searched_list_offer'] = searched_list
    result = {'success': True, 'response': 'Done'}
    return jsonify(result)
    return redirect(url_for('b'))


@app.route("/query", methods=['POST'])
def advanced():
    """ recieves post requests to add new task """
    # data = request.get_json()
    advanced_list = db_helper.Search_Query()        # advanced one
    session['advanced_list'] = advanced_list
    result = {'success': True, 'response': 'Done'}
    print("here")
    return jsonify(result)

@app.route("/query1", methods=['POST'])
def advanced1():
    """ recieves post requests to add new task """
    # data = request.get_json()
    advanced_list1 = db_helper.Search_Query1()
    session['advanced_list1'] = advanced_list1
    result = {'success': True, 'response': 'Done'}
    print("here")
    return jsonify(result)

@app.route("/search_result")
def search_result():
    """ returns rendered homepage """
    searched_list = session.get('searched_list', None)
    return render_template("search_result.html", items=searched_list)

@app.route("/search_result_offer")
def search_result_offer():
    """ returns rendered homepage """
    searched_list = session.get('searched_list_offer', None)
    return render_template("search_result_offer.html", items=searched_list)

@app.route("/compare", methods=['POST'])
def compare():
    try:
        data = request.get_json()
        db_helper.procedure(data)       # should change
        result = {'success': True, 'response': 'Add one user'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}   # !!! this might the part to say invalid usr?
    return jsonify(result)

@app.route("/start_compare")
def start_compare():
    return render_template("compare.html")

    
@app.route("/match")
def advanced_result():
    """ returns rendered homepage """
    advanced_list = db_helper.display_goodprice() # should change
    return render_template("goodprice1.html", items=advanced_list)

@app.route("/hot")
def hot():
    """ returns rendered homepage """
    advanced_list = db_helper.display_hot() # should change
    return render_template("hot.html", items=advanced_list)


@app.route("/advanced_query1")
def advanced_result1():
    """ returns rendered homepage """
    advanced_list1 = session.get('advanced_list1', None)
    return render_template("advanced_result1.html", items=advanced_list1)


@app.route("/login")
def login():
    return render_template("login.html")

# modi
@app.route("/user_in")
def proc():
    return render_template("user_in.html")

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/buy")
def buy():
    """ returns rendered homepage """
    items = db_helper.fetch_wish_list()
    return render_template("wish.html", items=items)

@app.route("/sell")
def sell():
    items = db_helper.fetch_offer_list()
    return render_template("offer.html", items=items)

@app.route("/see_user")
def user_list():
    items = db_helper.fetch_product_list()
    return render_template("user.html", items=items)    

@app.route("/logined")
def logined():
    return render_template("hometouser.html")      

# add gyh
@app.route("/add_user", methods=['POST'])
def register():
    try:
        data = request.get_json()
        db_helper.register_user(data)
        result = {'success': True, 'response': 'Add one user'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}   # !!! this might the part to say invalid usr?
    return jsonify(result)

# modi
@app.route("/check_user", methods=['POST'])
def check_user():
    try:
        data = request.get_json()
        count = db_helper.check_user_p(data)
        result = {'success': True, 'response': count}           # newone
    except Exception as e: 
        print("panic:",e)
        result = {'success': False, 'response': 'Something went wrong'}   # !!! this might the part to say invalid usr?
    return jsonify(result)
