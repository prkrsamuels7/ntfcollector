from django.shortcuts import render
from .models import Nft
# Create your views here.

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def nfts_index(request):
  nfts = Nft.objects.all()
  return render(request, 'nfts/index.html', { 'nfts': nfts })