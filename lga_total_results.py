
# Question 2: Displaying Summed Total Result 
# of Polling Units under a Local Government

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

@app.route('/lga_total_results/<int:lga_id>')
def lga_total_results(lga_id):
    conn = connect_db()
    cursor = conn.cursor()

    # Query to retrieve summed total result for the specified local government
    sql = "SELECT party_abbreviation, SUM(party_score) AS total_score FROM announced_pu_results JOIN polling_units ON announced_pu_results.polling_unit_uniqueid = polling_units.uniqueid WHERE polling_units.lga_id = %s GROUP BY party_abbreviation"
    cursor.execute(sql, (lga_id,))
    results = cursor.fetchall()

    cursor.close()
    conn.close()

    if results:
        return {'results': results}
    else:
        return {'message': 'No results found for the specified local government.'}

if __name__ == '__main__':
    app.run(debug=True)
