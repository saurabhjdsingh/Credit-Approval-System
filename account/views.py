from datetime import datetime, timedelta
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User, Loan
from .serializers import UserSerializer, LoanSerializer
from .utils import export_user_to_excel, credit_score


# used for importing test data from excel file
from .utils import import_loan_from_excel, import_user_from_excel
class Import(APIView):

    def get(self, request):
        # import_user_from_excel()
        # import_loan_from_excel()
        return JsonResponse({"message":"Data imported successfully"}, status=200)


class register(APIView):
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            export_user_to_excel(User.objects.all())  # Export to Excel after saving
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
       
class check_eligibility(APIView):

    def post(self, request):
        try:
            user = User.objects.get(id=request.data['customer_id'])
        except User.DoesNotExist:
            return JsonResponse({"message":"User not found"}, status=404)
        credit_score_val = credit_score(request.data['customer_id'])
        interest_rate = request.data['interest_rate']
        if credit_score_val > 50:
            interest_rate = request.data['interest_rate']
        elif 50 > credit_score_val > 30:
            interest_rate = 12
        elif 30 > credit_score_val > 10:
            interest_rate = 16
        elif 10 > credit_score_val:
            return JsonResponse({"message":"Loan not approved"}, status=400)
        else:
            return JsonResponse({"message":"Loan not approved"}, status=400)
        
        #calculate the monthly installment
        monthly_installment = request.data['loan_amount'] * interest_rate / (1 - (1 + interest_rate) ** (-request.data['tenure']))
        return JsonResponse({"customer Id":request.data['customer_id'],"approval":True,"interest_rate":request.data['interest_rate'], "corrected_interest_rate":interest_rate, "tenure":request.data['tenure'], "monthly_installment":monthly_installment}, status=200)
    

class create_loan(APIView):

    def post(self, request):
        customer_id = request.data['customer_id']
        loan_amount = request.data['loan_amount']
        tenure = request.data['tenure']
        interest_rate = request.data['interest_rate']
        monthly_installment = request.data['loan_amount'] * interest_rate / (1 - (1 + interest_rate) ** (-request.data['tenure']))
        try:
            user = User.objects.get(id=customer_id)
        except User.DoesNotExist:
            return JsonResponse({"message":"User not found"}, status=404)
        loan = Loan(user=user, loan_amount=loan_amount, tenure=tenure, interest_rate=interest_rate, emi=monthly_installment, start_date=datetime.now(), end_date=datetime.now() + timedelta(days=tenure*30))
        loan.save()
        return JsonResponse({"loan_id":loan.id,"customer_id":customer_id,"loan_approved":True, "message":"Loan approved & successfully created", "monthly_installment":monthly_installment}, status=201)

class ViewLoan(APIView):

    def get(self, request, id):
        try:
            loan = Loan.objects.get(id=id)
        except:
            return JsonResponse({"message":"Loan not found"}, status=404)
        serializer = LoanSerializer(loan)
        return Response(serializer.data, status=status.HTTP_200_OK)    

class ViewLoans(APIView):

    def get(self, request, id):
        try:
            user = User.objects.get(id=id)
        except:
            return JsonResponse({"message":"User not found"}, status=404)
        loans = Loan.objects.filter(user=user)
        serializer = LoanSerializer(loans, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)