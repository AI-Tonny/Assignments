from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import Shoe
from .forms import ShoeForm


def shoe_list(request):
    shoes = Shoe.objects.all()
    return render(request, 'shoes/shoe_list.html', {'shoes': shoes})


def shoe_detail(request, pk):
    shoe = get_object_or_404(Shoe, pk=pk)
    return render(request, 'shoes/shoe_detail.html', {'shoe': shoe})


def shoe_create(request):
    if request.method == 'POST':
        form = ShoeForm(request.POST)
        if form.is_valid():
            shoe = form.save()
            messages.success(request, f'Shoe "{shoe.manufacture or "ID #" + str(shoe.id)}" created successfully!')
            return redirect('shoe_detail', pk=shoe.id)
    else:
        form = ShoeForm()
    return render(request, "shoes/shoe_form.html", {'form': form})


def shoe_update(request, pk):
    shoe = get_object_or_404(Shoe, pk=pk)
    if request.method == "POST":
        form = ShoeForm(request.POST, instance=shoe)
        if form.is_valid():
            form.save()
            messages.success(request, f'Shoe "{shoe.manufacture or "ID #" + str(shoe.id)}" updated successfully!')
    else:
        form = ShoeForm(instance=shoe)
    return render(request, 'shoes/shoe_form.html', {'form': form})

def shoe_delete(request, pk):
    shoe = get_object_or_404(Shoe, pk=pk)
    if request.method == 'POST':
        shoe_name = shoe.manufacture or f"ID #{shoe.id}"
        shoe.delete()
        messages.success(request, f'Shoe "{shoe_name}" has been deleted successfully!')
        return redirect('shoe_list')
    return render(request, 'shoes/shoe_confirm_delete.html', {'shoe': shoe})
