from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound
from .models import Privilege
from django.utils.crypto import get_random_string

def check_privilege(req):
    if req.headers.get("Privilege-Owner",None):
        return redirect("your_privilege", p_id = req.headers["Privilege-Owner"])

    if req.method == "POST":
        priv = Privilege() 
        priv.save()
        return redirect("your_privilege", p_id = priv.privilege_owner)

    return render(req,"privilege.html",{"priv":None, "noUpdate": False})

def check_your_privilege(req, p_id):
    privilege = Privilege.objects.filter(privilege_owner=p_id).first()
    if not privilege:
        req.status = 404
        return render(req, "reset.html", {})     
    if req.method == "POST":
        if privilege.check_privilege():
            privilege.save()
        else:
            req.stats = 403
            return render(req, "privilege.html", {"priv": privilege, "noUpdate":True})
    return render(req, "privilege.html", {"priv": privilege, "noUpdate":False})