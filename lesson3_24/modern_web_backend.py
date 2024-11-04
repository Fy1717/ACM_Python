from flask import Flask, jsonify

app = Flask(__name__)

class Food:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        

@app.route('/foods')
def food_list():
    try:
        biber_dolmasi = Food("Biber Dolması", 10.5) 
        pilav = Food("pilav", 30) 
        manti = Food("mantı", 10) 

        my_food_list = [biber_dolmasi.name, pilav.name, manti.name]
        
        return jsonify({"data": my_food_list})
    except Exception as e:
        return jsonify({"error": str(e)})


# Sayfa görüntülenme sayacı
page_views = {"mainPage": 0, "categoryPage": 0, "productPage": 0}

# Kullanıcı bazlı loglama
user_logs = {}

# Fonksiyonel loglama işlemi
def log_page_view(page_type, username):
    # Kullanıcı bazlı loglama
    user_logs[username] = user_logs.get(username, page_views)
    user_logs[username][page_type] = user_logs[username].get(page_type, 0) + 1

    print(user_logs)
    

# MainPage görüntülenme endpoint'i
@app.route('/')
def page():
    log_page_view("mainPage", 'main')

    return jsonify({'message': 'Sayfa görüntülendi!'})


# Kategori sayfası endpoint'i
@app.route('/category')
def category_page():
    log_page_view("categoryPage", 'ahmet')

    return jsonify({'message': 'Kategori sayfası görüntülendi!'})


# Ürün sayfası endpoint'i
@app.route('/product')
def product_page():
    log_page_view("productPage", 'ahmet')

    return jsonify({'message': 'Ürün sayfası görüntülendi!'})


if __name__ == '__main__':
    app.run(debug=True)
