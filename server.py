from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined


app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"


@app.route("/")
def show_homepage():
    """Show homepage"""
    jobs = ["Software Engineer", "QA Engineer", "Product Manager"]

    return render_template("index.html")

@app.route("/application-form")
def application_form():
    """Show application form"""

    return render_template("application-form.html")

@app.route("/application-success", methods=["POST"])
def submit_application():
    """Submits application and returns response"""

    firstname = request.form.get("firstname")
    lastname = request.form.get("lastname")
    salary = request.form.get("salary")
    job = request.form.get("job")

    salary = "${amount:,.2f}".format(amount=float(salary))

    return render_template("application-response.html",
                           firstname=firstname,
                           lastname=lastname,
                           salary=salary,
                           job=job)


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
