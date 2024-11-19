import sqlite3
from tkinter.messagebox import NO
from flask import *

app = Flask(__name__)

def create_connection():
    conn = sqlite3.connect("my1.db")
    conn.row_factory = sqlite3.Row
    
    return conn

def filling_db():
    conn = create_connection()
    curs = conn.cursor()
    
    curs.execute("DROP TABLE IF EXISTS cities")

    curs.execute("""
    CREATE TABLE IF NOT EXISTS cities (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        name_ VARCHAR(50), 
        population_ INTEGER, 
        description_ TEXT, 
        year_of_foundation DATE, 
        image_ VARCHAR(255)
    )
    """
    )
    curs.execute(
    '''
    CREATE TABLE IF NOT EXISTS users (     
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        login VARCHAR(50),
        password VARCHAR(50), 
        psw_repeat VARCHAR(50),
    )
    '''
    )

    curs.execute("INSERT INTO cities (id, name_, population_, description_, year_of_foundation, image_) VALUES (1, 'Одеса', 1 000 000, 'Перлина у моря', 1794, 'https://osama.com.ua/wp-content/uploads/2021/12/36.jpg')")
    curs.execute("INSERT INTO cities (id, name_, population_, description_, year_of_foundation, image_) VALUES (2, 'Київ', 3 000 000, 'Столиця України', 430, 'https://www.nta.ua/wp-content/uploads/2022/02/kyyiv.jpg')")
    curs.execute("INSERT INTO cities (id, name_, population_, description_, year_of_foundation, image_) VALUES (3, 'Харків', 1 421 125, 'Перша столиця України', 1654, 'https://static.ukrinform.com/photos/2022_04/thumb_files/630_360_1651221771-528.jpg')")   
    curs.execute("INSERT INTO cities (id, name_, population_, description_, year_of_foundation, image_) VALUES (4, 'Львів',  717 273, 'Національно-культурний та освітньо-науковий осередок країни', 1256, 'https://ukr-prokat.com/wp-content/uploads/2020/07/lviv.jpg')")
    curs.execute("INSERT INTO cities (id, name_, population_, description_, year_of_foundation, image_) VALUES (5, 'Запоріжжя', 710 052, 'Четвертий за величиною індустріальний центр України з розвиненим машинобудуванням, чорною та кольоровою металургією, хімічною та будівельною промисловістю', 952, 'https://etnoxata.com.ua/image/cache/catalog/image/catalog/stat3/06_2016/22_06_16/z/00.webp')")
    curs.execute("INSERT INTO cities (id, name_, population_, description_, year_of_foundation, image_) VALUES (6, 'Херсон', 279 131, 'Батьківщина кавунів', 18 червня 1778, 'https://upload.wikimedia.org/wikipedia/commons/1/16/%D0%A2%D1%80%D0%B8_%D1%88%D1%82%D1%8B%D0%BA%D0%B0_%D1%82%D0%B0%D0%B2%D1%80%D0%B8%D1%87%D0%B5%D1%81%D0%BA%D0%B8%D0%B9.jpg')")
    curs.execute("INSERT INTO cities (id, name_, population_, description_, year_of_foundation, image_) VALUES (7, 'Вінниця', 369 740, 'Місто рекордів та рекордсменів', '1355 або 1363', 'https://moemisto.ua/img/cache/blog_show_photo/blog/0004/66/29621a187e82764a0a7a3b0665264fb15ebb77ef.jpeg')")
    curs.execute("INSERT INTO cities (id, name_, population_, description_, year_of_foundation, image_) VALUES (8, 'Івано-Франківськ', 238 196, 'Серце Прикарпаття', 1661, 'https://zaxid.net/resources/photos/news/202109/1526378.jpg')")
    curs.execute("INSERT INTO cities (id, name_, population_, description_, year_of_foundation, image_) VALUES (9, 'Чернівці', 264 300, 'Дуже старе місто', 'XII століття', 'http://promin.cv.ua/uploads/posts/2017-10/1507709750_1442180581_68423_800x600_chernovcy.jpg')")
    curs.execute("INSERT INTO cities (id, name_, population_, description_, year_of_foundation, image_) VALUES (10, 'Миколаїв', 470 011, 'Місто кораблів', 1789, 'https://np.pl.ua/wp-content/uploads/2022/07/nikolaev24.com_.ua_-e1658310297435.jpg')")

    conn.commit()

@app.route("/")
def index():
    conn = create_connection()
    curs = conn.cursor()
    
    curs.execute("SELECT * FROM cities")
    sities = curs.fetchall()
    
    return render_template('index.html', sities=sities)

@app.route("/kiev")
def kiev():
    conn = create_connection()
    curs = conn.cursor()
    
    curs.execute("SELECT * FROM cities")
    sities = curs.fetchall()
    
    return render_template('1Kiev.html', sities=sities)

@app.route("/odessa")
def odessa():
    conn = create_connection()
    curs = conn.cursor()
    
    curs.execute("SELECT * FROM cities")
    sities = curs.fetchall()
    
    return render_template('2Odessa.html', sities=sities)

@app.route("/harkiv")
def harkiv():
    conn = create_connection()
    curs = conn.cursor()
    
    curs.execute("SELECT * FROM cities")
    sities = curs.fetchall()
    
    return render_template('3Xarkiv.html', sities=sities)

@app.route("/lviv")
def lviv():
    conn = create_connection()
    curs = conn.cursor()
    
    curs.execute("SELECT * FROM cities")
    sities = curs.fetchall()
    
    return render_template('4Lviv.html', sities=sities)

@app.route("/zaporiggya")
def zp():
    conn = create_connection()
    curs = conn.cursor()
    
    curs.execute("SELECT * FROM cities")
    sities = curs.fetchall()
    
    return render_template('5Zaporigga.html', sities=sities)

@app.route("/herson")
def herson():
    conn = create_connection()
    curs = conn.cursor()
    
    curs.execute("SELECT * FROM cities")
    sities = curs.fetchall()
    
    return render_template('6Herson.html', sities=sities)

@app.route("/vinica")
def vinica():
    conn = create_connection()
    curs = conn.cursor()
    
    curs.execute("SELECT * FROM cities")
    sities = curs.fetchall()
    
    return render_template('7Vinica.html', sities=sities)

@app.route("/Ivano-Frankovsk")
def Iv_Fr():
    conn = create_connection()
    curs = conn.cursor()
    
    curs.execute("SELECT * FROM cities")
    sities = curs.fetchall()
    
    return render_template('8Iv-Fr.html', sities=sities)

@app.route("/chernivci")
def chernivci():
    conn = create_connection()
    curs = conn.cursor()
    
    curs.execute("SELECT * FROM cities")
    sities = curs.fetchall()
    
    return render_template('9Chernivci.html', sities=sities)

@app.route("/mikolaiv")
def mikolaiv():
    conn = create_connection()
    curs = conn.cursor()
    
    curs.execute("SELECT * FROM cities")
    sities = curs.fetchall()
    
    return render_template('10Mikolaiv.html', sities=sities)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == 'POST':
        conn = create_connection()
        curs = conn.cursor()
        
        id = request.form.get('id')
        password = request.form.get('password')
        login = request.form.get('login')
        
        curs.execute("""INSERT INTO users (id, login, password)
                    VALUES (?,?)""", [id, login, password])
        conn.commit()

        print(id, login, password)
        
    return render_template('register.html')


@app.route("/users")
def users():
    conn = create_connection()
    curs = conn.cursor()
    
    curs.execute("SELECT * FROM users")
    users = curs.fetchall()
    
    return render_template('users.html', users = users)

@app.route("/sign_in", methods=["GET", "POST"])  
def sign_in():
    if request.method == 'POST':
        conn = create_connection()
        curs = conn.cursor()
       
        password = request.form.get('password')
        login = request.form.get('login')

        curs.execute("SELECT * FROM users WHERE login=(?) and password=(?)", [login, password])
        user=curs.fetchall()
        if user is None:
            print('Такого користувача немає')
        else:
            print('Ласкаво просимо!')
        
    return render_template('sign_in.html')

app.run(debug=True)