from flask import Flask, render_template, request
from sql_con import get_db_conection



app = Flask(__name__)

@app.route('/form_get', methods = ['GET'])
def formGET_index():
    if request.method == 'GET':
        conn = get_db_conection()
        data = conn.execute('select "id", "username" ,"firstname", "lastname" from user').fetchall()
        conn.close()
        print("len data", len(data))
        if len(data) != 0:
            print(data)
            for k in data:
                print(k[0], k[1], k[2], k[3])
            print('req.args:', len(request.args))
            if(len(request.args) != 0):
                Firstname = request.args.get('firstname')
                Lastname = request.args.get('lastname')
                conn = get_db_conection()
                data = conn.execute('select "id", "username" ,"firstname", "lastname" from user where firstname=? AND lastname=?'\
                    , (Firstname, Lastname)).fetchall()
                conn.close()
                print(data)
                if data is None:
                    # return if serach is none
                    return render_template('form_get.html')
                else:
                    for k in data:
                        print(k[0], k[1], k[2], k[3])
                    # return from serach query
                    return render_template('form_get.html', data=data)
            # return if we query data successfuly    
            return render_template('form_get.html', data=data)
        # return if len data grom query all is 0
        return render_template('form_get.html')

@app.route('/form_post', methods = ['GET', 'POST'])
def formPOST_index():
    if request.method == 'GET':
        return render_template('form_post.html')
    elif request.method == 'POST':
        print(len(request.form))
        if len(request.form) != 0:
            for key,value in request.form.items():
                print(key,value)
            Firstname = request.form.get('firstname')
            Lastname = request.form.get('lastname')
            print(Firstname)
            print(Lastname)
            return render_template('form_post.html', data = [Firstname, Lastname])
        
if __name__ == 'main':
    app.run(debug=True)