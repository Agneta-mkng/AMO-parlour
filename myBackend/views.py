from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def services(request):
    data={
        "message":"These are the services offered by AMO parlour",
        "services":[
           {"name":"Manicure","price":"Ksh 700"},
           {"name":"Pedicure","price":"Ksh 700"},
           {"name":"Dreadlock installation","price":"Ksh 3500"},
           {"name":"Massage","price":"Ksh 2000"},
           {"name":"Twist out","price":"Ksh 300"}
        ]
    }
    return Response(data)
