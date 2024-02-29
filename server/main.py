from flask import Flask, request

app = Flask(__name__)

# Fonction intensive en CPU
def calcul_intensif(n):
    if n < 2:
        return n
    else:
        return calcul_intensif(n-1) + calcul_intensif(n-2)

@app.route('/calcul', methods=['GET'])
def calcul():
    n = int(request.args.get('n', ''))
    result = calcul_intensif(n)
    return f"Résultat: {result}"

if __name__ == '__main__':
    app.run(debug=True)
