from django.contrib import auth, messages
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
                    print(user.id_typoUsuario)
                    if str(user.id_typoUsuario) == 'MESERO':
                        return redirect('/meseros')
                    else:
                        return redirect('/cajeros')
            else:
                messages.error(req, 'Usaurio no valido')
                return redirect('main:mainHome')
        except:
            print(req)
    else:
        return render(req, 'main/index.html')
