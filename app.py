from flask import Flask

FAI=Flask(__name__)
@FAI.route('/wish')

def wish():
    return "Good Morning"

@FAI.route('/greetings')
def greetings():
    return "Welcome To Flask"

if __name__=='__main__':
    FAI.run(debug=True)



