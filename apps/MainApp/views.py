from django.contrib import auth
from django.shortcuts import render, redirect


def main_home(req):
    if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password']
        try:
            user = auth.authenticate(username=username, password=password)
            auth.login(req, user)
            if user is not None and user.is_active:
                if user.is_admin:
                    return redirect('/admin')
                else:
                    if str(user.id_typoUsuario) == 'mesero':
                        return redirect('/meseros')
                    else:
                        return redirect('/cajeros')
        except:
            print(req)
    else:
        return render(req, 'main/index.html')
