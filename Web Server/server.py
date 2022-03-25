from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__) 

@app.route("/") 
def homepage():
    return render_template('/index.html')

@app.route("/<string:url_input>") 
def pages(url_input=None):
    return render_template('/' + url_input)


def write_to_txt(data):
    with open('./database.txt', mode='a') as database: # to write the data in the txt file
        email = data['email']
        subject = data['subject']
        message = data['message']
        database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
    with open('./database.csv', newline='', mode='a') as database2: # to write the data in the csv file
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                              # csv file to write in
                                         # delimiter
                                                        # when quoting use this character
                                                                       # only quote when absolutely necessary
                                                                       # (when text contains special chars)
        csv_writer.writerow([email,subject,message])


@app.route('/submit_form', methods=['POST', 'GET']) # POST = saves info. GET = send info.
def submit_form():
    if request.method == 'POST': 
        try:
            data = request.form.to_dict() # requests the data from the form and returns it in a dictionary with
                                        # the names and input values
            print(data) # prints the data in the terminal
            write_to_csv(data)
            return redirect('/thankyou.html') # redirects to the thank you page
        except Exception as err:
            return f'Did not save to database {err}'
    else:
        return 'Something went wrong. Try again!'

