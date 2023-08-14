from flask import Blueprint, render_template, session, flash, redirect, url_for
from datetime import datetime

from models.loans import Loan

from forms.loan_forms import LoanForm 

home_views = Blueprint('home',__name__)

@home_views.route('/')
def index():
    user = session.get('user')
    return render_template('home/index.html')

@home_views.route('/loan/', methods = ['GET', 'POST'])
def loan():
    form = LoanForm()

    if form.validate_on_submit():
        id_cliente = session.get('user')['id']
        monto = form.monto.data
        periodo = form.periodo.data
        modalidad_pago = form.modalidad_pago.data
        fecha_in = datetime.utcnow()

        user = Loan(id_cliente, monto, periodo, modalidad_pago, fecha_in)
        user.save()
        flash ('Prestamo Registrado')

        return redirect(url_for('home.fecha_p'))

    return render_template('home/loan.html', form = form)

@home_views.route('/about/')
def about():
    return render_template('home/about.html') 

@home_views.route('/cover/')
def cover():
    return render_template('home/cover.html')

@home_views.route('/fecha_p/')
def fecha_p():
    return render_template('fecha_p.html')

@home_views.route('/terminos/')
def terminos():
    return render_template('home/terminos.html')

@home_views.route('/address/')
def address():
    return render_template('auth/address.html')

@home_views.route('/calculo/')
def calculo():
    return render_template('home/calculo.html')