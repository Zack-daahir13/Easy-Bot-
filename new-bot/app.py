from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/5sUy30VbdoyF67poMDkf1fpEj44WblfcJOGkdpA1', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        school = request.form.get('school')
        subjects = request.form.getlist('subjects')
        favorite_subject = request.form.get('favorite_subject')

        # Halkan waxaad kusii daabici kartaa xogta ama aad ugu diri kartaa database
        return f"Magaca: {name}, Dugsiga: {school}, Maadooyinka uu ku fiican yahay: {', '.join(subjects)}, Maadada uu aadka u xiiseeyo: {favorite_subject}"
    
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
