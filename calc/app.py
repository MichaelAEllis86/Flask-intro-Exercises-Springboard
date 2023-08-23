# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

print("I am running!")

@app.route('/add')
def do_addition():
    print(request.args)
    a=int(request.args['a'])
    b=int(request.args["b"])
    print(type(a))
    print(type(b))
    print(a)
    print(b)
    added=add(a,b)
    print(added)
    return f"{added}"
    
@app.route('/sub')
def do_subtraction():
    print(request.args)
    a=int(request.args['a'])
    b=int(request.args["b"])
    print(type(a))
    print(type(b))
    print(a)
    print(b)
    subtracted=sub(a,b)
    print(subtracted)
    return f"{subtracted}"


@app.route('/mult')
def do_multiplication():
    print(request.args)
    a=int(request.args['a'])
    b=int(request.args["b"])
    print(type(a))
    print(type(b))
    print(a)
    print(b)
    multiplied=mult(a,b)
    print(multiplied)
    return f"{multiplied}"

@app.route('/div')
def do_division():
    print(request.args)
    a=int(request.args['a'])
    b=int(request.args["b"])
    print(type(a))
    print(type(b))
    print(a)
    print(b)
    divided=div(a,b)
    print(divided)
    return f"{divided}"

operations={"add":add,
            "sub":sub,
            "mult":mult,
            "div":div
            }

@app.route("/math/<operation>")
def do_math(operation):
    print(request.args)
    a=int(request.args['a'])
    b=int(request.args["b"])
    print(type(a))
    print(type(b))
    print(a)
    print(b)
    result=operations[operation](a,b)
    print(result)
    return f"{result}"

    # alternatively with ellif statements

    # if (operation=="add"):
    #     added=add(a,b)
    #     print(added)
    #     return f"{added}"
    # elif (operation=="sub"):
    #     subtracted=sub(a,b)
    #     print(subtracted)
    #     return f"{subtracted}"
    # elif (operation=="mult"):
    #      multiplied=mult(a,b)
    #      print(multiplied)
    #      return f"{multiplied}"
    # elif (operation=="div"):
    #     divided=div(a,b)
    #     print(divided)
    #     return f"{divided}"
    # else: return "invalid operation valid operations are add, sub, mult and div"

       
   
   
    
