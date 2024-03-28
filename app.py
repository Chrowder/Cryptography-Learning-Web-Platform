from flask import Flask, render_template, request, redirect, url_for, jsonify
from py.shiftCipher import shift_cipher, brute_force_caesar_cipher
from py.substitutionCipher import substitution_cipher,decrypt_substitution_cipher
from py.permutationCipher import permutation_cipher

app = Flask(__name__)


# 主页路由
@app.route('/')
def index():
    return render_template('index.html')


# 加密路由
@app.route('/encrypt', methods=['POST'])
def encrypt():
    text = request.json['text']
    key = request.json['key']
    cipher_type = request.json['cipherType']

    if cipher_type == 'shiftCipher':
        encrypted_text = shift_cipher(text, int(key))
    elif cipher_type == 'permutationCipher':
        encrypted_text = permutation_cipher(text, [int(digit) for digit in key])
    elif cipher_type == 'substitutionCipher':
        encrypted_text = substitution_cipher(text, key)
    else:
        encrypted_text = "Invalid cipher type selected."

    return jsonify(encryptedText = f"{encrypted_text}")


# 解密路由
@app.route('/decrypt', methods=['POST'])
def decrypt():
    text = request.json['text']
    key = request.json['key']
    cipher_type = request.json['cipherType']

    if key != "":
        if cipher_type == 'shiftCipher':
            decrypted_text = shift_cipher(text, -int(key))
        elif cipher_type == 'permutationCipher':
            decrypted_text = permutation_cipher(text, [int(digit) for digit in key])
        elif cipher_type == 'substitutionCipher':
            decrypted_text = decrypt_substitution_cipher(text, key)
        else:
            decrypted_text = "Invalid cipher type selected."
    else:
        if cipher_type == 'shiftCipher':
            decrypted_text = brute_force_caesar_cipher(text)
        # elif cipher_type == 'permutationCipher':
        #
        # elif cipher_type == 'substitutionCipher':

        else:
            decrypted_text = "Invalid cipher type selected."


    return jsonify(decryptedText = f"{decrypted_text}")




if __name__ == '__main__':
    app.run(debug=True)
