from flask import Flask, render_template, request, redirect, url_for, jsonify
from py.shiftCipher import shift_cipher, brute_force_shift_cipher
from py.substitutionCipher import substitution_cipher,decrypt_substitution_cipher, brute_force_substitution_cipher
from py.permutationCipher import permutation_cipher, decrypt_permutation_cipher, brute_force_permutation_cipher

app = Flask(__name__)


# page
@app.route('/')
def index():
    return render_template('shift_cipher.html')



@app.route('/shift_cipher')
def shift_cipher_page():
    return render_template('shift_cipher.html')



@app.route('/permutation_cipher')
def permutation_cipher_page():
    return render_template('permutation_cipher.html')


@app.route('/substitution_cipher')
def substitution_cipher_page():
    return render_template('substitution_cipher.html')

@app.route('/about')
def about_page():
    return render_template('about.html')




@app.route('/shift_encrypt', methods=['POST'])
def shift_encrypt():
    text = request.json['text']
    key = request.json['key']
    encrypted_text = shift_cipher(text, int(key))

    return jsonify(encryptedText = f"{encrypted_text}")


@app.route('/shift_decrypt', methods=['POST'])
def shift_decrypt():
    text = request.json['text']
    key = request.json['key']
    decrypted_text = shift_cipher(text, -int(key))
    return jsonify(decryptedText = f"{decrypted_text}")


@app.route('/shift_brute_decrypt', methods=['POST'])
def shift_brute_decrypt():
    text = request.json['text']

    decrypted_text, key = brute_force_shift_cipher(text)
    response_data = {
        'key': key,
        'decryptedText': decrypted_text
    }
    return jsonify(response_data)





@app.route('/permutation_encrypt', methods=['POST'])
def permutation_encrypt():
    text = request.json['text']
    key = request.json['key']

    encrypted_text = permutation_cipher(text, [int(digit) for digit in key])


    return jsonify(encryptedText = f"{encrypted_text}")


@app.route('/permutation_decrypt', methods=['POST'])
def permutation_decrypt():
    text = request.json['text']
    key = request.json['key']
    decrypted_text = decrypt_permutation_cipher(text, [int(digit) for digit in key])

    return jsonify(decryptedText = f"{decrypted_text}")



@app.route('/permutation_brute_decrypt', methods=['POST'])
def permutation_brute_decrypt():
    text = request.json['text']

    decrypted_text, key = brute_force_permutation_cipher(text)
    response_data = {
        'key': key,
        'decryptedText': decrypted_text
    }
    return jsonify(response_data)







@app.route('/substitution_encrypt', methods=['POST'])
def substitution_encrypt():
    text = request.json['text']
    key = request.json['key']
    encrypted_text = substitution_cipher(text, key)

    return jsonify(encryptedText = f"{encrypted_text}")


@app.route('/substitution_decrypt', methods=['POST'])
def substitution_decrypt():
    text = request.json['text']
    key = request.json['key']
    decrypted_text = decrypt_substitution_cipher(text, key)
    return jsonify(decryptedText = f"{decrypted_text}")


@app.route('/substitution_brute_decrypt', methods=['POST'])
def substitution_brute_decrypt():
    text = request.json['text']
    print(1)
    decrypted_text, key = brute_force_substitution_cipher(text)
    response_data = {
        'key': key,
        'decryptedText': decrypted_text
    }
    return jsonify(response_data)








if __name__ == '__main__':
    app.run(debug=True)
