from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def home(request):
    result = ''
    if request.method == 'POST':
        try:
            num1 = float(request.POST.get('num1'))
            num2 = float(request.POST.get('num2'))
            op = request.POST.get('operation')

            if op == 'add':
                result = num1 + num2
            elif op == 'sub':
                result = num1 - num2
            elif op == 'mul':
                result = num1 * num2
            elif op == 'div':
                result = num1 / num2
        except Exception as e:
            result = f"Error: {e}"

    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Simple Calculator</title>
        <style>
            body {{
                font-family: Arial;
                background: linear-gradient(to right, #141e30, #243b55);
                color: white;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                margin: 0;
            }}
            .card {{
                background-color: rgba(255, 255, 255, 0.1);
                padding: 30px;
                border-radius: 10px;
                box-shadow: 0 4px 10px rgba(0,0,0,0.5);
                text-align: center;
            }}
            input, select {{
                padding: 10px;
                margin: 10px;
                border-radius: 5px;
                border: none;
                width: 80%;
            }}
            button {{
                background-color: #00c9ff;
                padding: 10px 20px;
                border: none;
                border-radius: 5px;
                cursor: pointer;
                font-weight: bold;
            }}
            .result {{
                margin-top: 20px;
                font-size: 1.2em;
                color: #ffff88;
            }}
        </style>
    </head>
    <body>
        <div class="card">
            <h2>Simple Calculator</h2>
            <form method="post">
                <input type="number" name="num1" placeholder="First number" required><br>
                <select name="operation">
                    <option value="add">+</option>
                    <option value="sub">-</option>
                    <option value="mul">*</option>
                    <option value="div">/</option>
                </select><br>
                <input type="number" name="num2" placeholder="Second number" required><br>
                <button type="submit">Calculate</button>
            </form>
            <div class="result">{f"Result: {result}" if result != '' else ''}</div>
        </div>
    </body>
    </html>
    """
    return HttpResponse(html)
