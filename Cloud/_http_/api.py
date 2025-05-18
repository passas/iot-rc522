from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from django.db import IntegrityError
from .models import User, Contract, Ticket, Train, TemperatureHumidity

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from .permissions import IsAgent, IsSensor

from datetime import date

class Register(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        data = {}
        u = request.user
        if u.role == 'Agent': #u.is_authenticated
            if 'email' in request.POST:
                try:
                    u = User.objects.create_user(username=request.POST['email'], password='xxx')
                    u.save()
                except IntegrityError:
                    data['message'] = 'Credentials already in use'
                    return JsonResponse(status=200, data=data)
                data['message'] = 'Successfully registred'
                return JsonResponse(status=201, data=data)
            else:
                data['message'] = 'Bad request'
                return JsonResponse(status=400, data=data)
        else:
            data['message'] = 'Permission denied'
            return JsonResponse(status=403, data=data)

class HealthView(APIView):
    permission_classes = [AllowAny]
    def get(self, request, format=None):
        data = {
            'method': 'GET',
            'status': 'health'
        }
        return JsonResponse(status=200, data=data)
    def post(self, request, format=None):
        data = {
            'method': 'POST',
            'status': 'health'
        }
        return JsonResponse(status=200, data=data)
    
class HealthAgent(APIView):
    permission_classes = [IsAgent]
    #Headers:
    #   Authorization: Bearer <token>
    def get(self, request, format=None):
        data = {
            'method': 'GET',
            'status': 'health'
        }
        return JsonResponse(status=200, data=data)
    def post(self, request, format=None):
        data = {
            'method': 'POST',
            'status': 'health'
        }
        return JsonResponse(status=200, data=data)
    
class Client(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        data = {}
        u = request.user
        if u.role == 'Agent':
            if 'card_id' and 'email' and 'first_name' and 'last_name' in request.POST:
                try:
                    u = User.objects.create_user(
                        username=request.POST['email'],
                        password='xxx',
                        card_id=request.POST['card_id'],
                        first_name=request.POST['first_name'],
                        last_name=request.POST['last_name'],
                    )
                    u.save()
                except IntegrityError:
                    data['message'] = 'Credentials already in use'
                    return JsonResponse(status=200, data=data)
                data['message'] = 'Successfully registred'
                return JsonResponse(status=201, data=data)
            else:
                data['message'] = 'Bad request'
                return JsonResponse(status=400, data=data)
        else:
            data['message'] = 'Permission denied'
            return JsonResponse(status=403, data=data)
        
class Contracts(APIView):
    permission_classes = [IsAgent]
    def get(self, request, format=None):
        contracts = {}
        desconto_jovem = 0.25
        desconto_estudante = 1
        passes = {
            'Normal': [0.00, 20.0, 20.1, 35.2, 40.3, 45.4, 50.5, 55.6, 60.7, 65.8],
            'Jovem': [0.00, 20.0*(1-desconto_jovem), 20.1*(1-desconto_jovem), 35.2*(1-desconto_jovem), 40.3*(1-desconto_jovem), 45.4*(1-desconto_jovem), 50.5*(1-desconto_jovem), 55.6*(1-desconto_jovem), 60.7*(1-desconto_jovem), 65.8*(1-desconto_jovem)],
            'Estudante': [0.00, 20.0*(1-desconto_estudante), 20.1*(1-desconto_estudante), 35.2*(1-desconto_estudante), 40.3*(1-desconto_estudante), 45.4*(1-desconto_estudante), 50.5*(1-desconto_estudante), 55.6*(1-desconto_estudante), 60.7*(1-desconto_estudante), 65.8*(1-desconto_estudante)],
        }
        desconto_meio = 0.5
        desconto_quarto = 0.75
        titulos = {
            'Normal': [0.00, 1.60, 1.60, 1.95, 2.20, 2.55, 2.90, 3.25, 3.55, 3.90],
            'Meio': [0.00, 1.60*(1-desconto_meio), 1.60*(1-desconto_meio), 1.95*(1-desconto_meio), 2.20*(1-desconto_meio), 2.55*(1-desconto_meio), 2.90*(1-desconto_meio), 3.25*(1-desconto_meio), 3.55*(1-desconto_meio), 3.90*(1-desconto_meio)],
            'Quarto': [0.00, 1.60*(1-desconto_quarto), 1.60*(1-desconto_quarto), 1.95*(1-desconto_quarto), 2.20*(1-desconto_quarto), 2.55*(1-desconto_quarto), 2.90*(1-desconto_quarto), 3.25*(1-desconto_quarto), 3.55*(1-desconto_quarto), 3.90*(1-desconto_quarto)],
        }
        itenerario = ['Braga', 'Nine', 'Famalicao', 'Trofa', 'Ermesinde', 'Porto S.Bento']
        zonas = [
            [1],
            [2,1],
            [3,2,1],
            [5,3,2,1],
            [7,5,4,2,1],
            [8,6,5,4,2,1],
        ]
        expire = date.today()
        expire = expire.replace(year=expire.year+1)
        contracts['contracts'] = passes
        contracts['expire'] = expire
        contracts['tickets'] = titulos
        contracts['stops'] = itenerario
        contracts['zones'] = zonas
        return JsonResponse(status=200, data=contracts)
    
    def post(self, request, format=None):
        data = {}
        if 'card_id' and 'contract' and 'c_zone1' and 'c_zone2' and 'c_price' and 'c_expire' in request.POST:
            try:
                u = User.objects.get(card_id=request.POST['card_id'])
                if u is not None:
                    Contract.objects.create(
                        user=u,
                        type=request.POST['contract'],
                        zone1=request.POST['c_zone1'],
                        zone2=request.POST['c_zone2'],
                        price=request.POST['c_price'],
                        expire=request.POST['c_expire']
                    )
                else:
                    data['message'] = 'User not registred'
                    return JsonResponse(status=200, data=data)
            except IntegrityError:
                data['message'] = 'Wrong info'
                return JsonResponse(status=200, data=data)
            data['message'] = 'Successfully registred'
            return JsonResponse(status=201, data=data)
        else:
            data['message'] = 'Bad request'
            return JsonResponse(status=400, data=data)
        
class Tickets(APIView):
    permission_classes = [IsAgent]
    def post(self, request, format=None):
        data = {}
        if 'card_id' and 'ticket' and 't_zone1' and 't_zone2' and 't_amount' in request.POST:
            try:
                Ticket.objects.create(
                    card_id=request.POST['card_id'],
                    type=request.POST['ticket'],
                    zone1=request.POST['t_zone1'],
                    zone2=request.POST['t_zone2'],
                    amount=request.POST['t_amount']
                )
            except IntegrityError:
                data['message'] = 'Wrong info'
                return JsonResponse(status=200, data=data)
            data['message'] = 'Successfully registred'
            return JsonResponse(status=201, data=data)
        else:
            data['message'] = 'Bad request'
            return JsonResponse(status=400, data=data)
        
    def put(self, request, format=None):
        data = {}
        if 'card_id' and 'ticket' and 't_zone1' and 't_zone2' and 't_amount' in request.data:
            try:
                #t = Ticket.objects.get(card_id=request.data['card_id'])
                t = Ticket.objects.filter(card_id=request.data['card_id']).last()
                if t is not None:
                    t.type=request.data['ticket']
                    t.zone1=request.data['t_zone1']
                    t.zone2=request.data['t_zone2']
                    t.amount=request.data['t_amount']
                    t.save()
                else:
                    data['message'] = "Card id doesn't exist"
                    return JsonResponse(status=200, data=data)
            except IntegrityError:
                data['message'] = 'Wrong info'
                return JsonResponse(status=200, data=data)
            data['message'] = 'Successfully registred'
            return JsonResponse(status=201, data=data)
        else:
            data['message'] = 'Bad request'
            return JsonResponse(status=400, data=data)
        
class Sensor(APIView):
    permission_classes = [IsSensor]
    def post(self, request, format=None):
        data = {}
        train_id = request.user.card_id # Ups!
        if 'temperature' and 'humidity' and 'timestamp' in request.POST:
            t = None
            if Train.objects.filter(id=train_id).exists():
                t = Train.objects.get(id=train_id)
            else:
                t = Train.objects.create(id=train_id)
            if t is not None:
                try:
                    TemperatureHumidity.objects.create(
                        train=t,
                        temperature=request.POST['temperature'],
                        humidity=request.POST['humidity'],
                        timestamp=request.POST['timestamp']
                    )
                except IntegrityError:
                    data['message'] = 'Server conflict'
                    return JsonResponse(status=1409, data=data)
                data['message'] = 'Successfully registred'
                return JsonResponse(status=201, data=data)
            else:
                data['message'] = 'Server conflict'
                return JsonResponse(status=409, data=data)
        else:
            data['message'] = 'Bad request'
            return JsonResponse(status=400, data=data)
