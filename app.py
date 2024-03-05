# Flask  application to manage polling unit results


from flask import Flask, render_template, request, redirect
import pymysql

app = Flask(__name__)

# Connect to the database
def connect_db():
    return pymysql.connect(host='localhost',
                           user='bincom',
                           password='password',
                           database='bincom_test',
                           cursorclass=pymysql.cursors.DictCursor)

# Display the form for inputting new polling unit results
@app.route('/new_polling_unit_form')
def new_polling_unit_form():
    return render_template('new_polling_unit_form.html')

# Save the new polling unit results to the database
@app.route('/save_polling_unit_results', methods=['POST'])
def save_polling_unit_results():
    polling_unit_id = request.form['polling_unit_id']
    party_abbreviation = request.form['party_abbreviation']
    party_score = request.form['party_score']

    conn = connect_db()
    cursor = conn.cursor()

    # Insert the new polling unit results into the database
    sql = "INSERT INTO announced_pu_results (polling_unit_uniqueid, party_abbreviation, party_score) VALUES (%s, %s, %s)"
    cursor.execute(sql, (polling_unit_id, party_abbreviation, party_score))
    conn.commit()

    cursor.close()
    conn.close()

    return redirect('/new_polling_unit_form')

if __name__ == '__main__':
    app.run(debug=True)
