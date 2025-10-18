"""
WADE Coleta - Flask app (consolidated)

This file contains a single clean Flask application. When executed directly
(`python app.py`) it will start the development server bound to 0.0.0.0 so
you can access it from other devices on the same LAN for testing.
"""

from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
import os


app = Flask(__name__)
# Use environment variable if provided, otherwise a default secret for dev
app.secret_key = os.environ.get('JOJO_SECRET', 'dev_secret_wade_2025')


@app.context_processor
def inject_session():
    return {'session': session}


def init_db():
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            empresa_nome TEXT,
            nota_fiscal TEXT,
            barcode TEXT,
            product_name TEXT,
            boxes_received INTEGER,
            units_per_box INTEGER
        )
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS empresas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_empresa TEXT UNIQUE,
            email TEXT UNIQUE,
            senha TEXT
        )
    ''')
    # Inserir uma empresa de exemplo se não existir
    c.execute('SELECT COUNT(*) FROM empresas')
    if c.fetchone()[0] == 0:
        c.execute('''
            INSERT INTO empresas (nome_empresa, email, senha)
            VALUES ('Empresa Exemplo', 'exemplo@empresa.com', '123456')
        ''')
    conn.commit()
    conn.close()


init_db()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login_empresa', methods=['GET', 'POST'])
def login_empresa():
    error = None
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('senha')
        
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        c.execute('SELECT nome_empresa FROM empresas WHERE email = ? AND senha = ?', (email, senha))
        empresa = c.fetchone()
        conn.close()
        
        if empresa:
            session['empresa_logada'] = True
            session['nome_empresa'] = empresa[0]
            return redirect(url_for('empresa_dashboard'))
        else:
            error = 'Email ou senha incorretos.'
    
    return render_template('login_empresa.html', error=error)


@app.route('/logout_empresa')
def logout_empresa():
    session.pop('empresa_logada', None)
    session.pop('nome_empresa', None)
    return redirect(url_for('index'))


@app.route('/empresa_dashboard')
def empresa_dashboard():
    # Verificar se a empresa está logada
    if not session.get('empresa_logada'):
        return redirect(url_for('login_empresa'))
    
    nome_empresa = session.get('nome_empresa')
    
    # Buscar apenas os dados da empresa logada
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('''
        SELECT empresa_nome, nota_fiscal, barcode, product_name, boxes_received, units_per_box
        FROM produtos
        WHERE empresa_nome = ?
        ORDER BY nota_fiscal, id DESC
    ''', (nome_empresa,))
    rows = c.fetchall()
    conn.close()
    
    # Agrupar por nota fiscal
    agrupados = {}
    for row in rows:
        empresa, nota = row[0], row[1]
        key = (empresa, nota)
        if key not in agrupados:
            agrupados[key] = []
        agrupados[key].append({
            'barcode': row[2],
            'product_name': row[3],
            'boxes_received': row[4],
            'units_per_box': row[5]
        })
    
    return render_template('empresa_dashboard.html', agrupados=agrupados, nome_empresa=nome_empresa)


@app.route('/empresa/limpar_nota', methods=['POST'])
def empresa_limpar_nota():
    if not session.get('empresa_logada'):
        return redirect(url_for('login_empresa'))
    
    nome_empresa = session.get('nome_empresa')
    nota = request.form.get('nota')
    
    if nota:
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        # Só permite limpar notas da própria empresa
        c.execute('DELETE FROM produtos WHERE empresa_nome=? AND nota_fiscal=?', (nome_empresa, nota))
        conn.commit()
        conn.close()
    
    return redirect(url_for('empresa_dashboard'))


@app.route('/admin_login', methods=['GET', 'POST'])
def admin_login():
    error = None
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'lucas' and password == '197520':
            session['admin_logged_in'] = True
            return redirect(url_for('admin'))
        else:
            error = 'Usuário ou senha incorretos.'
    return render_template('admin_login.html', error=error)


@app.route('/coleta', methods=['GET', 'POST'])
def coleta():
    # Verificar se a empresa está logada
    if not session.get('empresa_logada'):
        return redirect(url_for('login_empresa'))
    
    nome_empresa = session.get('nome_empresa')
    
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            produtos = data.get('produtos', [])
            conn = sqlite3.connect('data.db')
            c = conn.cursor()
            for p in produtos:
                c.execute('''
                    INSERT INTO produtos (empresa_nome, nota_fiscal, barcode, product_name, boxes_received, units_per_box)
                    VALUES (?, ?, ?, ?, ?, ?)
                ''', (
                    nome_empresa,  # Usar o nome da empresa logada
                    p.get('nota_fiscal'),
                    p.get('barcode'),
                    p.get('product_name'),
                    p.get('boxes_received'),
                    p.get('units_per_box')
                ))
            conn.commit()
            conn.close()
            return ('', 204)
        else:
            nota_fiscal = request.form.get('nota_fiscal')
            barcode = request.form.get('barcode')
            product_name = request.form.get('product_name')
            boxes_received = request.form.get('boxes_received')
            units_per_box = request.form.get('units_per_box')
            conn = sqlite3.connect('data.db')
            c = conn.cursor()
            c.execute('''
                INSERT INTO produtos (empresa_nome, nota_fiscal, barcode, product_name, boxes_received, units_per_box)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (nome_empresa, nota_fiscal, barcode, product_name, boxes_received, units_per_box))
            conn.commit()
            conn.close()
            return redirect(url_for('coleta'))
    
    return render_template('coleta.html', nome_empresa=nome_empresa)


@app.route('/admin')
def admin():
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    conn = sqlite3.connect('data.db')
    c = conn.cursor()
    c.execute('''
        SELECT empresa_nome, nota_fiscal, barcode, product_name, boxes_received, units_per_box
        FROM produtos
        ORDER BY empresa_nome, nota_fiscal, id DESC
    ''')
    rows = c.fetchall()
    
    # Buscar empresas cadastradas
    c.execute('SELECT nome_empresa, email FROM empresas ORDER BY nome_empresa')
    empresas = c.fetchall()
    
    conn.close()
    agrupados = {}
    for row in rows:
        empresa, nota = row[0], row[1]
        key = (empresa, nota)
        if key not in agrupados:
            agrupados[key] = []
        agrupados[key].append({
            'barcode': row[2],
            'product_name': row[3],
            'boxes_received': row[4],
            'units_per_box': row[5]
        })
    return render_template('admin.html', agrupados=agrupados, empresas=empresas)


@app.route('/admin/cadastrar_empresa', methods=['POST'])
def cadastrar_empresa():
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    
    nome_empresa = request.form.get('nome_empresa')
    email = request.form.get('email')
    senha = request.form.get('senha')
    
    if nome_empresa and email and senha:
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        try:
            c.execute('''
                INSERT INTO empresas (nome_empresa, email, senha)
                VALUES (?, ?, ?)
            ''', (nome_empresa, email, senha))
            conn.commit()
        except sqlite3.IntegrityError:
            # Empresa ou email já existe
            pass
        conn.close()
    
    return redirect(url_for('admin'))


@app.route('/admin/limpar_nota', methods=['POST'])
def limpar_nota():
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    empresa = request.form.get('empresa')
    nota = request.form.get('nota')
    if empresa and nota:
        conn = sqlite3.connect('data.db')
        c = conn.cursor()
        c.execute('DELETE FROM produtos WHERE empresa_nome=? AND nota_fiscal=?', (empresa, nota))
        conn.commit()
        conn.close()
    return redirect(url_for('admin'))


if __name__ == '__main__':
    # Run on 0.0.0.0 so other devices on the LAN (your phone) can connect.
    # Keep debug=True for development; remove in production.
    app.run(debug=True, use_reloader=False, host='0.0.0.0', port=5000)

