from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, FloatField, RadioField
from wtforms.validators import DataRequired, Length, NumberRange

class LoanForm(FlaskForm):
    monto = FloatField("Monto: ", validators=[DataRequired(), NumberRange(min=500, max=20000)])  
    periodo = RadioField("Periodo: ", 
                        choices=['2','4','6','8','10','12'],
                        validators=[DataRequired()])
    modalidad_pago = RadioField("Modalidad Pago: ",
                                choices=['Quincenal','Mensual'],
                                validators=[DataRequired()])
    submit = SubmitField("Continuar")