
# Question 1: Displaying Results for an Individual Polling Unit

from flask import Flask, request
import pymysql

app = Flask(__name__)

# Connect to the database
def connect_db():
    return pymysql.connect(host='localhost',
                           user='bincom',
                           password='password',
                           database='bincom_test',
                           cursorclass=pymysql.cursors.DictCursor)

@app.route('/polling_unit_results/<int:polling_unit_id>')
def polling_unit_results(polling_unit_id):
    conn = connect_db()
    cursor = conn.cursor()

    # Query to retrieve results for the specified polling unit
    sql = "SELECT * FROM announced_pu_results WHERE polling_unit_uniqueid = %s"
    cursor.execute(sql, (polling_unit_id,))
    results = cursor.fetchall()

    cursor.close()
    conn.close()

    if results:
        return {'results': results}
    else:
        return {'message': 'No results found for the specified polling unit.'}

if __name__ == '__main__':
    app.run(debug=True)
