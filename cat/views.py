from asgiref.sync import sync_to_async
from django.http import HttpResponse
import asyncio

# Create your views here.
async def async_view(request):
    print('QQQQQQQQ')
    await asyncio.sleep(30)
    print('WWWWWWWW')
    return HttpResponse(f"time taken async 30sec.")